# Changelog
## Einlesen & erste Veränderung
game.py code: xrange in range umschreiben, da fehler;
--> xrange nicht kompatibel in neuer Version

## Verbesserung der Codestruktur
### Gesamter Code außer run.py ist im game.py (Main) Code; Das wird geändert
* bilder in folder, einfachere struktur, ersetzen von verwirrenden variablennamen; 
* fonts in folder, umbennenung einfachere struktur;
* settings.py hinzugefügt; alle Bilder und Fonts werden da in Variablen gespeichert um im Main nur die Variablennamen aufzurufen; 
* loadingscreen.py hinzugefügt; mit Funktion zum Aufrufen im Main;
* menu.py hinzugefügt; Funktion zum Aufrufen im Main;

## Verbesserung der Gamedynamik
Mouseclick event hinzugefügt; Da Pfeiltasten auswahl extrem langsam ist; Bis zu 5 Sekunden um von Play auf Quit zu wechseln;

## Verbesserung des Gamedesigns
Bei großem Gewinn wird ein BigWin Bild eingefügt;
