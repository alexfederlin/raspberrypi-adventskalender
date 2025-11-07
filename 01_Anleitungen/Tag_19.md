# 01_Anleitungen/Tag_19_Der_Nachrichten_Ticker.md

## 📅 Tag 19: Der Nachrichten-Ticker! 📰

Deine Wetterstation kann jetzt Live-Daten (deine Innentemperatur) und globale Daten (die Außentemperatur) anzeigen. Heute erweitern wir die Anzeige um den spannendsten Inhalt des Internets: **aktuelle Schlagzeilen!**

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Wir nutzen die **`feedparser`**-Bibliothek, um Nachrichten über **RSS-Feeds** abzurufen.

### 🎯 Das Ziel des Tages

Wir bringen den Pi dazu, einen **RSS-Feed** zu lesen. RSS ist ein Standardformat, das Zeitungen und Blogs verwenden, um ihre neuesten Überschriften zur Verfügung zu stellen.

Am Ende zeigt dein Programm die **fünf neuesten Schlagzeilen** im Terminal an (und du weißt, wie du sie auf das Display bekommst!).

### 🔌 Schritte (Hardware)

* **Nichts zu tun!** Der Pi muss nur **mit dem WLAN verbunden** sein.

---

### 💻 Schritte (Software)

#### Die Schlagzeilen abrufen

Wir nutzen heute den RSS-Feed der **BBC News Top Stories** (oder einen anderen Feed deiner Wahl, wenn dieser nicht funktioniert, aber dieser ist sehr stabil).

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_19/` und öffne die Datei **`Tag_19.py`**.
3.  **Code ansehen:**
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Im Shell-Fenster sollte der Name des News-Feeds und dann eine nummerierte Liste der **fünf neuesten Schlagzeilen** erscheinen. Dein Pi ist jetzt ein Nachrichten-Ticker!

### 🧪 Experimentier-Zone!

Du kannst jetzt alle Arten von Feeds in deine Station integrieren (Sport, Technik, lokale Nachrichten, wenn sie einen RSS-Feed anbieten).

* **Challenge 1: Deine eigene Quelle**
    * **Herausforderung:** Suche online nach einem RSS-Feed, der dich interessiert (z.B. von einer Tech-Seite oder einer Sport-Zeitung) und ersetze die `RSS_URL` in Zeile 10 durch die neue Adresse.
* **Challenge 2: Der Ticker**
    * Das Display deiner Station ist sehr schmal. Große Überschriften passen nicht.
    * **Herausforderung:** Baue den Code so um, dass er die erste Schlagzeile (`feed.entries[0].title`) in einer `for`-Schleife **Buchstabe für Buchstabe** ausgibt, um einen Laufticker zu simulieren.
* **Challenge 3 (Experte): Integration ins Display**
    * **Herausforderung:** Kombiniere den Code von heute mit dem Dashboard von Tag 15.
    * Füge einen **dritten Modus** ( `ANZEIGE_MODUS = 2`) hinzu, der mit dem **Taster** angewählt werden kann und dann die erste Schlagzeile auf dem **OLED-Display** anzeigt.