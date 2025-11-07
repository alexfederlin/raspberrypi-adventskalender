# 01_Anleitungen/Tag_02_Git_Klonen.md

## 📅 Tag 2: Das Code-Repository klonen ☁️

Herzlichen Glückwunsch zu Tag 1! Dein Pi ist startklar. Heute verbinden wir ihn mit unserem geheimen Projekt-Hauptquartier auf GitHub!

### 🎁 Inhalt des Türchens

* Eine **Notiz** mit einem **Link** (URL) und deinen persönlichen **Zugangsdaten** (Username & Token/Passwort).

### 🎯 Das Ziel des Tages

Heute lernst du ein super wichtiges Werkzeug für Programmierer kennen: **Git**.

Mit Git können wir unseren Code speichern und verwalten. Wir werden heute das "Repository" (unser Projekt-Archiv) von GitHub auf deinen Pi herunterladen (**klonen**). Von nun an holst du dir jeden Tag mit einem kurzen Befehl die neue Anleitung und den neuen Code aus diesem Repository.

### 💡 Schritte (ca. 20-25 Minuten)

1.  **Terminal öffnen:**
    * Starte deinen Pi (falls er aus ist).
    * Klicke auf das **schwarze Terminal-Icon** oben links in der Menüleiste. 
2.  **Zum Desktop wechseln:**
    * Wir wollen das Projekt an einen Ort legen, den du leicht findest. Tippe den folgenden Befehl ein und drücke `Enter`:
    ```bash
    cd Desktop
    ```
3.  **Das Projekt klonen:**
    * Jetzt kommt der Magie-Befehl! Benutze `gh repo clone` und den Link von deiner Notiz.
    * **WICHTIG:** Ersetze `[HIER_DEIN_LINK_EINFUEGEN]` mit dem echten Link von deinem Zettel!
    ```bash
    gh repo clone [HIER_DEIN_LINK_EINFUEGEN]
    ```
    * Drücke `Enter`.
4.  **Erfolg prüfen:**
    * Wenn alles geklappt hat, siehst du auf deinem Desktop einen **neuen Ordner**! Er heißt (wahrscheinlich) `Adventskalender_Pi_Tage`.
    * Du kannst das Terminal jetzt schließen.

### 💻 Erster Code-Test (mit Thonny)

Jetzt überprüfen wir, ob der erste Code da ist.

1.  **Thonny IDE starten:**
    * Klicke auf die **Himbeere** (Menü) oben links.
    * Gehe zu **"Programmierung"** und wähle **"Thonny Python IDE"**.
2.  **Datei öffnen:**
    * Gehe in Thonny auf **"Datei"** (File) -> **"Laden..."** (Load...).
    * Ein Dateimanager öffnet sich. Klicke auf **"Desktop"**.
    * Öffne den neuen Ordner **`Adventskalender_Pi_Tage`**.
    * Öffne den Ordner **`Tag_02`**.
    * Wähle die Datei **`Tag_02.py`** aus und klicke auf **"OK"**.
3.  **Code ausführen:**
    * Der Code wird dir jetzt im Hauptfenster angezeigt (z.B. `print("Willkommen!")`).
    * Klicke auf den **großen grünen "Play"-Button** (Run) in der Symbolleiste.
    
4.  **Erfolg!**
    * Im unteren Fenster (der "Shell") sollte jetzt die Nachricht erscheinen: "Git Klonen erfolgreich! Willkommen beim Projekt!" (oder eine ähnliche Nachricht).
    * **Du hast Tag 2 gemeistert!**
