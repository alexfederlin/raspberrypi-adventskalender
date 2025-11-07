# 01_Anleitungen/Tag_18_Die_Wettervorhersage.md

## 📅 Tag 18: Die Wettervorhersage! 🌤️

Gestern hast du gelernt, wie man Live-Daten (die Zeit) aus dem Internet abruft. Heute wenden wir dieses Wissen auf den eigentlichen Zweck deiner Station an: die **Wettervorhersage für draußen!**

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Heute nutzen wir die **Open-Meteo API**, um Vorhersagedaten abzurufen.

### 🎯 Das Ziel des Tages

Wir bauen den Code von Tag 17 aus. Dein Pi fragt eine professionelle Wetter-API ab und zeigt die **aktuelle Außentemperatur** und eine **einfache Vorhersage** (z.B. Regen oder Sonne) im Terminal an.

### 🔌 Schritte (Hardware)

* **Nichts zu tun!** Der Pi muss nur **mit dem WLAN verbunden** sein, damit die API-Abfrage funktioniert.

---

### 💻 Schritte (Software)

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_18/` und öffne die Datei **`Tag_18.py`**.
3.  **Code ansehen:**

    * Wir definieren eine **geografische Position** (Längen- und Breitengrad). Wir nehmen die Mitte von Deutschland (z.B. Frankfurt: 50.1°N, 8.7°E).
    * Die `URL` ist sehr lang, weil wir genau festlegen, welche Daten wir wollen (Temperatur, Wettercode und Zeit).
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Im Shell-Fenster solltest du die aktuelle **Außentemperatur** und eine lesbare **Wetterbeschreibung** für die gewählte geografische Position sehen. Dein Pi kann jetzt seine lokale Messung mit globalen Daten vergleichen!

### 🧪 Experimentier-Zone!

* **Challenge 1: Deine Heimatstadt**
    * **Herausforderung:** Finde die Längen- und Breitengrade deiner eigenen Stadt (einfach googeln!) und ersetze die Werte in Zeile 10 (`LATITUDE`) und Zeile 11 (`LONGITUDE`). Starte den Code neu!
* **Challenge 2: Die Vorhersage**
    * Die API liefert einen stündlichen Forecast. Der Index `[0]` in Zeile 43 und 46 liefert die **aktuelle** Stunde.
    * **Herausforderung:** Wie änderst du den Code so, dass er die Temperatur für **morgen um 12 Uhr** anzeigt?
    * **Tipp:** Wenn der Code zur Mittagszeit läuft, ist Index `[12]` oft die Vorhersage für die gleiche Stunde morgen. Probiere es mit Index `[24]` (24 Stunden später).
* **Challenge 3 (Experte): Kombiniertes Display**
    * **Herausforderung:** Kombiniere den Code von heute mit dem Dashboard von Tag 15.
    * Du könntest den **Taster** jetzt umschalten lassen zwischen:
        1.  **DRINNEN** (BME280-Daten)
        2.  **DRAUSSEN** (API-Daten)