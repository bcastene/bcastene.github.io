# Website BC Astene (bcastene.github.io)

Doel: eenvoudige, mobielvriendelijke clubwebsite, gratis gehost op GitHub Pages. Pagina's zijn Markdown-bestanden; GitHub zet ze zelf om (Jekyll). Geen build-stap, geen GitHub Actions, geen kosten.

## Bestanden

- `index.md`, `speeluren.md`, `lid-worden.md`, `contact.md`, `privacy.md`: de vijf pagina's (tekst).
- `_layouts/default.html`: kop, menu en voet, op één plaats.
- `_data/menu.yml`: het menu.
- `_config.yml`: sitenaam, beschrijving, sitenaam en beschrijving (geen mailadres meer).
- `assets/style.css`: alle opmaak. `assets/logo.png`: clublogo in de kop. `assets/favicon.svg`: eenvoudig icoontje (BC).
- `assets/mail.js`: klein eigen script (geen bibliotheek) dat het clubmailadres op de contactpagina samenstelt en er een klikbare link van maakt.
- `controle.py` en deze `README.md`: voor jou en mij, ze verschijnen niet op de site.

Secrets: geen. De site gebruikt geen cookies, geen analytics, geen externe lettertypes of bibliotheken.

## Voor je publiceert

Er staan geen open `[?]` meer in de teksten. Enige externe links (toegelaten in `controle.py`, lijst `TOEGELATEN_EXTERN`): https://www.gegevensbeschermingsautoriteit.be en https://badminton.vlaanderen/privacy-policy/. De vragen staan ook in de notitie `BC Astene - Website` in de vault.

## 1. Repository aanmaken

1. Ga naar https://github.com en log in als `bcastene`.
2. Klik rechtsboven op het plusje (+) en kies **New repository**. Of ga rechtstreeks naar https://github.com/new
3. Bij **Repository name** typ je exact `bcastene.github.io` (kleine letters, geen spaties).
4. Kies **Public**.
5. Vink niets aan bij README, .gitignore of license.
6. Klik op **Create repository**.

## 2. Bestanden uploaden

1. Je zit nu op de lege repository: https://github.com/bcastene/bcastene.github.io
2. Klik op de link **uploading an existing file**. Of kies **Add file** > **Upload files**.
3. Sleep de inhoud van de map `BCAsteneSite` naar het venster: de bestanden `index.md`, `speeluren.md`, `lid-worden.md`, `contact.md`, `privacy.md`, `_config.yml` en de mappen `_layouts`, `_data`, `assets`. Sleep dus de bestanden en mappen zelf, niet de map `BCAsteneSite` eromheen.
4. Wacht tot alle bestanden in de lijst staan. Controleer dat de mappen met hun inhoud erbij staan.
5. Laat onderaan **Commit directly to the main branch** staan en klik op **Commit changes**.

Tip: bestanden die met een punt of underscore beginnen (`_config.yml`, `_layouts`, `_data`) worden door sommige bestandsbeheerders verborgen. Staan ze niet in de lijst, zet dan in je bestandsbeheerder "verborgen bestanden tonen" aan.

## 3. GitHub Pages aanzetten

1. Ga naar https://github.com/bcastene/bcastene.github.io/settings/pages
2. Bij **Build and deployment** > **Source** kies je **Deploy from a branch**.
3. Bij **Branch** kies je `main` en de map `/ (root)`. Klik op **Save**.
4. Wacht 1 tot 3 minuten en laad de pagina opnieuw. Bovenaan staat dan "Your site is live at https://bcastene.github.io/".
5. Controleer https://bcastene.github.io/ en https://bcastene.github.io/privacy.html (dat adres gebruikt de Google-app).

Toont de site na enkele minuten niets of een foutmelding? Kijk dan op https://github.com/bcastene/bcastene.github.io/actions of er een rode fout staat en geef de tekst aan Benson.

## 4. Een tekst aanpassen in de browser

1. Ga naar https://github.com/bcastene/bcastene.github.io en klik op het bestand, bv. `speeluren.md`.
2. Klik rechtsboven op het potloodje (**Edit this file**).
3. Pas de tekst aan. Het stuk tussen de twee `---` bovenaan laat je staan, tenzij je de titel of beschrijving van de pagina wil wijzigen.
4. Klik rechtsboven op **Commit changes...** en dan in het venster op **Commit changes**.
5. Na 1 tot 2 minuten staat de wijziging op de site.

Opmaak in de tekst: `## Titel` voor een tussentitel, `**vet**`, een regel die met `- ` begint voor een opsomming, `[tekst](contact.html)` voor een verwijzing naar de contactpagina.

Tik het mailadres NOOIT zelf in een tekst en maak geen `mailto:`-link: dan kunnen spam-scrapers het lezen. Verwijs naar de contactpagina.

## 5. Een pagina toevoegen

1. Ga naar https://github.com/bcastene/bcastene.github.io, kies **Add file** > **Create new file**.
2. Bij de naam typ je bv. `evenementen.md`.
3. Plak dit in het tekstvak en pas aan:

   ```
   ---
   layout: default
   title: "Evenementen"
   description: "Korte beschrijving voor Google."
   permalink: /evenementen.html
   ---

   # Evenementen

   Je tekst hier.
   ```

4. Klik **Commit changes...** en bevestig.
5. Voeg de pagina toe aan het menu: open `_data/menu.yml`, klik op het potloodje en voeg onderaan toe (let op de twee spaties voor `url`):

   ```
   - title: Evenementen
     url: /evenementen.html
   ```

6. Commit. De pagina staat na 1 tot 2 minuten op https://bcastene.github.io/evenementen.html

Een pagina verwijderen: open het bestand, klik op de drie puntjes rechtsboven, **Delete file**, commit. Haal ze ook uit `_data/menu.yml`.

## Mailadres tegen spam-scrapers

Het clubmailadres staat nergens als tekst of `mailto:` in de bronbestanden. Alle pagina's en de voet verwijzen naar de contactpagina. Daar staat een lege plek (`<span class="mailadres" data-g=... data-d=... data-t=...>`) met de adresdelen; `assets/mail.js` zet ze samen tot een klikbare link met de tekst van het adres. Zonder JavaScript staat er "bcastene [at] gmail [punt] com". Het adres wijzigen: pas de drie `data-`-delen in `contact.md` aan. Dit houdt eenvoudige scrapers tegen die enkel de HTML-bron lezen; scrapers die JavaScript uitvoeren kunnen het adres nog wel vinden. De `?v=`-nummers in de layout (nu `20261019-4`) verhoog je bij elke wijziging aan `style.css`, `logo.png` of `mail.js`, tegen oude kopies in de browsercache. 

## Logo

Het clublogo staat in `assets/logo.png` (1470 x 595 px, bijgesneden uit het origineel van 1920 x 1080, kleuren en vorm ongewijzigd, witte achtergrond). `_layouts/default.html` toont het in de kop met `alt="BC Astene"` en een link naar de startpagina. De hoogte (52 px gsm, 60 px pc) staat in `assets/style.css` (`.logo`), de breedte volgt automatisch. Het originele bestand blijft buiten de site bewaard (`/srv/benson/Scripts/BCAsteneSite-bron/logo-origineel.png`) en hoort niet in de repository. Een ander logo: upload het als `assets/logo.png` en pas eventueel `width` en `height` in de layout aan.

## Controle zonder Jekyll (voor Benson en Bodo)

`python3 -I controle.py` in deze map. Controleert front matter, menu en permalinks, interne links, externe verwijzingen, zichtbare `[?]` en of de layout nette HTML geeft. Vereist Python met PyYAML (staat op de server). Dit is niet de echte omzetting: die gebeurt pas op GitHub.

## Wat GitHub zelf doet

GitHub Pages bewaart de gewone toegangslogs van zijn servers en kan een IP-adres zien. De site zelf zet geen cookies en laadt niets van derden. Houd dat in gedachten bij de zin op de privacypagina.
