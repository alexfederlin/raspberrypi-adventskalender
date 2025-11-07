import requests
import time

# --- DEINE POSITION (Hier kannst du experimentieren!) ---
# Wir nutzen Frankfurt als Beispiel:
LATITUDE = 50.11 # Breitengrad (Norden/Süden)
LONGITUDE = 8.68 # Längengrad (Osten/Westen)

# Die Basis-URL der Open-Meteo API. 
# Wir fragen nach der stündlichen Temperatur und dem Wettercode (WMO code)
URL = (
    f"[https://api.open-meteo.com/v1/forecast](https://api.open-meteo.com/v1/forecast)?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}&"
    f"hourly=temperature_2m,weather_code&" # Diese Werte wollen wir
    f"timezone=Europe%2FBerlin" # Wichtig für die korrekte Uhrzeit
)

# --- ÜBERSETZUNG (WMO Wettercode -> Text) ---
# Die API gibt Zahlen aus, die wir übersetzen müssen!
WMO_CODES = {
    0: "Klarer Himmel ☀️",
    1: "Überwiegend klar",
    3: "Bewölkt ☁️",
    45: "Nebel",
    51: "Leichter Nieselregen",
    61: "Leichter Regen 🌧️",
    63: "Mäßiger Regen",
    65: "Starker Regen",
    71: "Leichter Schneefall ❄️",
    95: "Leichtes Gewitter ⛈️"
    # HINWEIS: Es gibt noch viele mehr, aber das sind die wichtigsten
}

print("Starte Wetter-Abfrage... Warte auf Antwort vom Server.")

try:
    # 1. Die Bestellung aufgeben (maximal 10 Sekunden warten)
    response = requests.get(URL, timeout=10)
    response.raise_for_status() # Stellt sicher, dass kein HTTP-Fehler vorliegt
    
    # 2. Die Antwort in ein Python-Format umwandeln
    data = response.json()
    
    # 3. Die Daten aus dem JSON-Baum holen (sehr spezifisch!)
    
    # Die aktuelle Temperatur ist die erste (Index 0) in der Liste 'hourly' -> 'temperature_2m'
    aktuelle_temp_aussen = data["hourly"]["temperature_2m"][0]
    
    # Der aktuelle Wettercode ist die erste (Index 0) in der Liste 'hourly' -> 'weather_code'
    aktueller_code = data["hourly"]["weather_code"][0]
    
    # Wir übersetzen den Code in einen Text
    wetter_text = WMO_CODES.get(aktueller_code, "Unbekanntes Wetter")
    
    print("\n--- Wetterdaten Draußen ---")
    print(f"Position: {LATITUDE}, {LONGITUDE}")
    print(f"Aktuelle Außentemperatur: {aktuelle_temp_aussen:.1f} °C")
    print(f"Wetter: {wetter_text}")

except Exception as e:
    print("\nFEHLER! Konnte Wetterdaten nicht abrufen.")
    print("Mögliche Ursache: Keine Internetverbindung oder falsche API-URL.")
    print(e)
