/* Zet het clubmailadres pas in de pagina als de browser JavaScript draait.
   Het adres staat dus nergens als leesbare tekst in de HTML-bron. Geen bibliotheek. */
(function () {
  var spots = document.querySelectorAll("span.mailadres");
  for (var i = 0; i < spots.length; i++) {
    var s = spots[i];
    var adres = s.getAttribute("data-g") + String.fromCharCode(64) +
                s.getAttribute("data-d") + "." + s.getAttribute("data-t");
    var a = document.createElement("a");
    a.href = "mail" + "to:" + adres;
    a.textContent = adres;
    s.textContent = "";
    s.appendChild(a);
  }
})();
