#!/usr/bin/env python3
"""Controle van de BC Astene-site zonder Jekyll. Draaien: python3 controle.py
Controleert: front matter, permalinks vs menu, interne links, externe verwijzingen,
Obsidian-markering, zichtbare [?], en of de layout nette HTML geeft (met nagebootste Liquid).
Dit vervangt de echte Jekyll-omzetting niet."""
import html.parser, re, sys
from pathlib import Path
import yaml

root = Path(__file__).parent
fouten = []
# Enige toegelaten externe links (GBA en privacyverklaring Badminton Vlaanderen)
TOEGELATEN_EXTERN = {"https://www.gegevensbeschermingsautoriteit.be",
                     "https://badminton.vlaanderen/privacy-policy/"}
def fout(t): fouten.append(t)

config = yaml.safe_load((root / "_config.yml").read_text())
menu = yaml.safe_load((root / "_data/menu.yml").read_text())
paginas = {}
for md in sorted(root.glob("*.md")):
    if md.name in config["exclude"]:
        continue
    tekst = md.read_text()
    m = re.match(r"---\n(.*?)\n---\n(.*)", tekst, re.S)
    if not m:
        fout(f"{md.name}: geen front matter"); continue
    fm = yaml.safe_load(m.group(1))
    for sleutel in ("layout", "title", "description", "permalink"):
        if not fm.get(sleutel):
            fout(f"{md.name}: front matter mist {sleutel}")
    paginas[md.name] = (fm, m.group(2))

permalinks = {fm["permalink"] for fm, _ in paginas.values()}
for item in menu:
    if item["url"] not in permalinks:
        fout(f"menu wijst naar onbekende pagina {item['url']}")
for p in permalinks - {i["url"] for i in menu}:
    fout(f"pagina {p} staat niet in menu (mag bewust)")

if "privacy.md" in paginas and paginas["privacy.md"][0]["permalink"] != "/privacy.html":
    fout("privacy moet op /privacy.html uitkomen")
if "index.md" in paginas and paginas["index.md"][0]["permalink"] != "/index.html":
    fout("index moet op /index.html uitkomen")

# interne links en externe verwijzingen
alles = {n: (root / n).read_text() for n in
         [*paginas, "_layouts/default.html", "assets/style.css", "assets/favicon.svg", "_config.yml", "_data/menu.yml"]}
for naam, tekst in alles.items():
    if "==" in tekst and naam.endswith(".md"):
        fout(f"{naam}: Obsidian-markering == gevonden")
    for url in re.findall(r"https?://[^\s)\"'<>]+", tekst):
        if url != "http://www.w3.org/2000/svg" and url not in TOEGELATEN_EXTERN:   # xmlns in favicon, geen verzoek
            fout(f"{naam}: externe verwijzing {url}")
    for link in re.findall(r"\]\(([^)]+)\)", tekst):
        if link.startswith("mailto:"):
            fout(f"{naam}: mailto-link in de bron ({link})")
        elif link in TOEGELATEN_EXTERN:
            pass
        elif "/" + link.lstrip("/") not in permalinks:
            fout(f"{naam}: link naar onbekende pagina {link}")
    if re.search(r"\b(\+32|BE\d\d ?\d{4})", tekst):
        fout(f"{naam}: lijkt op gsm of IBAN")

# anti-spam: het letterlijke adres en mailto: mogen nergens in de sitebestanden staan
for pad in [*paginas, "_layouts/default.html", "_config.yml", "_data/menu.yml", "assets/mail.js", "assets/style.css"]:
    tekst = (root / pad).read_text()
    if re.search(r"@\s*gmail|mailto:", tekst, re.I):
        fout(f"{pad}: letterlijk mailadres of mailto: gevonden (hoort enkel samengesteld door mail.js)")
if 'data-g="bcastene"' not in paginas["contact.md"][1] or "[at]" not in paginas["contact.md"][1]:
    fout("contact.md: samenstel-span of noscript-tekst ontbreekt")

# layout nabootsen: Liquid vervangen en HTML laten parsen
layout = alles["_layouts/default.html"]
class Controle(html.parser.HTMLParser):
    leeg = {"meta", "link", "br", "img"}
    def __init__(s): super().__init__(); s.stack = []
    def handle_starttag(s, t, a):
        if t not in s.leeg: s.stack.append(t)
    def handle_endtag(s, t):
        if not s.stack or s.stack.pop() != t: fout(f"layout: sluittag </{t}> klopt niet")
for fm, body in paginas.values():
    h = layout
    h = re.sub(r"\{% for item.*?%\}(.*?)\{% endfor %\}",
               lambda m: "".join(re.sub(r"\{%.*?%\}", "", m.group(1)).replace("{{ item.url | relative_url }}", i["url"]).replace("{{ item.title }}", i["title"]) for i in menu),
               h, flags=re.S)
    h = re.sub(r"\{%.*?%\}", "", h)
    h = re.sub(r"\{\{ content \}\}", "<p>x</p>", h)
    h = re.sub(r"\{\{.*?\}\}", "x", h)
    c = Controle(); c.feed(h)
    if c.stack: fout(f"layout: niet gesloten tags {c.stack}")
    break

print("Pagina's:", ", ".join(sorted(permalinks)))
open_vragen = sum(t.count("[?") for n, t in alles.items() if n.endswith(".md"))
print("Zichtbare [?] in teksten:", open_vragen)
for f in fouten: print("LET OP:", f)
sys.exit(1 if [f for f in fouten if "mag bewust" not in f] else 0)
