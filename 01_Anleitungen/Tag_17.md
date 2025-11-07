# 01_Anleitungen/Tag_17_Online_Gehen.md

## 📅 Tag 17: Online gehen! Deine Wetterstation holt die Weltzeit! 🌐

Dein Alarm-System ist genial! Es reagiert perfekt auf seine *lokale* Umgebung. Aber eine echte Wetterstation muss auch wissen, was *draußen* in der Welt passiert. Heute verbinden wir deinen Pi mit dem Internet, um die **echte, aktuelle Uhrzeit** abzurufen.

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Heute ist ein reiner "Netzwerk-Code"-Tag.

### 🎯 Das Ziel des Tages

Wir bringen dem Pi bei, Daten aus dem Internet zu holen. Dazu benutzen wir die `requests`-Bibliothek, um eine **API** (eine Datenschnittstelle) abzufragen.

Wir fragen die **Time API** nach der aktuellen Zeit in der Zeitzone **Europe/Amsterdam**.

### 🔌 Schritte (Hardware)

* **Nichts zu tun!** Außer... **stelle sicher, dass dein Raspberry Pi mit dem WLAN verbunden ist!** (Das kleine WLAN-Symbol oben rechts sollte verbunden aussehen).

---

### 💻 Schritte (Software)

#### Teil A: Den "Bestell-Assistenten" (requests) installieren

Damit Python "Bestellungen" (requests) aufgeben kann, braucht es einen Assistenten, die `requests`-Bibliothek.

1.  **Terminal öffnen.**
2.  Installiere die Bibliothek mit `pip` (dem Paketmanager für Python):
    ```bash
    sudo pip3 install requests
    ```

#### Teil B: Die Live-Uhrzeit abfragen

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_17/` und öffne die Datei **`Tag_17.py`**.
3.  **Code ansehen:**
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Im Shell-Fenster sollte (nach einer kurzen Lade-Pause) die **komplette Antwort (JSON)** des Servers und dann die **exakte Uhrzeit** für Amsterdam stehen. Dein Pi ist jetzt online und kann Live-Daten aus dem Internet abrufen!

### 🧪 Experimentier-Zone!

* **Challenge 1: Deine Zeitzone**
    * **Herausforderung:** Kannst du die Zeitzone im `URL`-String so ändern, dass die Zeit für eine andere Stadt oder dein eigenes Land angezeigt wird?
    * **Tipp:** Ersetze `Europe%2FAmsterdam` z.B. durch `Europe%2FBerlin` oder `America%2FNew_York`. (Das `%2F` steht einfach nur für den Schrägstrich `/`).
* **Challenge 2 (Experte): Live-Uhr auf dem Display!**
    * Das ist die Vorbereitung für morgen!
    * **Herausforderung:** Kombiniere den Code von heute mit dem Code von **Tag 13 (Display)**.
    * Du musst die Abfrage (`requests.get`) in eine **`while True`-Schleife** packen und die `aktuelle_uhrzeit` auf deinem **OLED-Display** anzeigen. *Warte aber mindestens 60 Sekunden* zwischen den Abfragen (`time.sleep(60)`), um den Server nicht zu überlasten!