# ⚙️ Vorbereitungs-Checkliste (Für den Schenkenden)

Dies ist die Checkliste für die Vorbereitung und tägliche Durchführung des Raspberry Pi Adventskalenders.

---

## I. Digitales Setup (Vor dem 1. Advent)

Diese Schritte bereiten das Repository für den Beschenkten vor.

| Schritt | Detail | Erledigt |
| :--- | :--- | :--- |
| **1. Beschenkten-Repo erstellen** | **Neues**, leeres GitHub-Repo anlegen (z.B. `Adventskalender_Pi_Tage`). | [ ] |
| **2. Authentifizierung** | **Personal Access Token (PAT)** auf GitHub erstellen (Settings -> Developer Settings). Dieses Token dient als Passwort für den `gh repo clone`-Befehl. | [ ] |
| **3. Tag 2 Code pushen** | Den Ordner `Tag_02/` (mit `Tag_02_Anleitung.md` & `Tag_02.py`) aus dem Master-Repo in das Beschenkten-Repo kopieren und pushen (`git push`). | [ ] |
| **4. Tag 2 Türchen** | Die Notiz für **Tag 2** vorbereiten: **Repo-Link**. Diese Notiz kommt zusammen mit der Hardware für Tag 2 (falls vorhanden) in das Türchen. | [ ] |

---

## II. Hardware & System-Setup (Vor dem 1. Advent)

Diese Schritte müssen einmalig durchgeführt werden, um den Raspberry Pi vorzubereiten.

| Schritt | Detail | Erledigt |
| :--- | :--- | :--- |
| **1. Pi OS installieren** | **Raspberry Pi OS** (mit Desktop) auf die SD-Karte spielen. | [ ] |
| **2. Grund-Setup & Updates** | Pi einmal hochfahren, WLAN konfigurieren, Sprache/Tastatur einstellen und alle Updates durchführen: `sudo apt update && sudo apt upgrade`. | [ ] |
| **3. Software installieren** | Sicherstellen, dass **`gh`** (`sudo apt install gh`) und die **`Thonny IDE`** (meist vorinstalliert) vorhanden sind. | [ ] |
| **4. gh config** | Um das git repo zu clonen, muss ein API Key in der env Variable GH_TOKEN exportiert werden (e.g. in `~/.bashrc` setzen)| [ ] |
| **4. Tag 1 Türchen** | Pi herunterfahren, SD-Karte entnehmen und in das Türchen für **Tag 1** legen. | [ ] |
| **5. Hardware verpacken** | Alle 23 weiteren Hardware-Komponenten (gemäß `00_Teileliste.md`) in die vorbereiteten Schachteln (`04_Verpackung_Printables/`) verpacken. | [ ] |




---

## III. Tägliche Durchführung (Jeden Abend ab Tag 2)

Diese Schritte müssen jeden Abend durchgeführt werden, um den nächsten Tag freizuschalten.

| Schritt | Detail | Erledigt |
| :--- | :--- | :--- |
| **10. Dateien kopieren** | Den neuen Ordner (z.B. `Tag_03/`) aus dem Master-Repo (`01_Anleitungen/` + `02_Code/`) in das lokale **Beschenkten-Repo** kopieren. | [ ] |
| **11. Git Push** | Änderungen im Beschenkten-Repo committen und pushen: `git add .`, `git commit -m "Tag 03 freigeschaltet"`, `git push`. | [ ] |
| **12. Türchen-Notiz** | Eine kleine Notiz für das Türchen des nächsten Tages vorbereiten: *"Aufgabe: `git pull` ausführen, um die neue Anleitung zu laden!"* (Diese Notiz wird zur Hardware des Tages gelegt). | [ ] |