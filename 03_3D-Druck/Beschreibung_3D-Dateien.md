# 03_3D_Druck/Beschreibung_3D-Dateien.md

## 🧱 3D-Druck-Vorlagen (STL-Dateien)

Dieser Ordner enthält alle STL-Dateien, die für das Gehäuse der Wetter- und Nachrichtenstation notwendig sind. Das Design ist so ausgelegt, dass die Komponenten (Raspberry Pi, Display, Breadboard-Prototyp) ohne Klebstoff oder spezielle Werkzeuge gesteckt und verschraubt werden können.

### 1. Gehaeuse_Boden.stl

| Detail | Beschreibung |
| :--- | :--- |
| **Zweck** | Die Basis der Station. Hält den Raspberry Pi und bietet Platz für die Kabelführung sowie Befestigungspunkte für die Abstandshalter. |
| **Druck-Hinweise** | **Filament:** PLA empfohlen. **Layer-Höhe:** 0.2 mm. **Infill:** 15–20%. **Stützen (Supports):** Wahrscheinlich nicht nötig, es sei denn, die Ausschnitte für die Ports sind überhängend. |
| **Montage** | Der Raspberry Pi wird mit 4 M2.5-Schrauben/Abstandshaltern im Boden befestigt. |

### 2. Gehaeuse_Front_Display.stl

| Detail | Beschreibung |
| :--- | :--- |
| **Zweck** | Die Frontplatte des Gehäuses. Sie enthält eine präzise Aussparung für das I2C-Display (z.B. SSD1306) und ein kleines Loch für den Taster. |
| **Druck-Hinweise** | **Filament:** PLA empfohlen. **Layer-Höhe:** 0.15 mm (für feineres Detail um das Display). **Infill:** 100% (für Stabilität). **Stützen:** Nicht nötig. |
| **Montage** | Das Display wird von hinten in die Fassung gesteckt. Der Taster wird in die dafür vorgesehene Öffnung eingesetzt. |

### 3. Gehaeuse_Deckel.stl

| Detail | Beschreibung |
| :--- | :--- |
| **Zweck** | Der obere Abschluss des Gehäuses. Dient als Schutz und kann individuelle Design-Elemente wie Lüftungsschlitze oder ein Logo enthalten. |
| **Druck-Hinweise** | **Filament:** Kann für das Projekt am Tag 19 das neue, spezielle Filament sein. **Layer-Höhe:** 0.2 mm. **Infill:** 10–15%. **Stützen:** Nicht nötig. |
| **Montage** | Wird als Letztes auf den Boden und die Frontplatte aufgesetzt und verschließt die Elektronik. |

---

### ⚠️ Wichtiger Hinweis für Tag 19 (Das 3D-Druck-Projekt)

Die STL-Dateien sollten **vor dem 19. Tag** gedruckt werden, da das Drucken mehrere Stunden dauern kann. Am **Tag 19** ist das Türchen mit dem **neuen Filament** gefüllt. Die Anleitung an diesem Tag ermutigt dazu, entweder den Gehäuse-Deckel in der neuen Farbe zu drucken oder ein ganz **eigenes Zubehörteil** (z.B. eine Antenne, eine kleine Figur oder eine Halterung für das Breadboard) zu entwerfen und zu drucken.