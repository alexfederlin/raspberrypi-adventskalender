import requests
import time

# Die API-Adresse, um die aktuelle Zeit in Amsterdam abzufragen
# ACHTUNG: Die URL muss exakt so sein (mit Groß-/Kleinschreibung und %2F)
URL = "https://timeapi.io/api/time/current/zone?timeZone=Europe%2FAmsterdam"

print(f"Verbinde mit: {URL}")
print("Mache eine 'GET'-Anfrage (Bestellung)...")

try:
    # 1. Die Bestellung aufgeben
    # Wir fragen mit einem Timeout, damit das Programm nicht ewig wartet
    response = requests.get(URL, timeout=10)
    
    # Sicherstellen, dass die Anfrage erfolgreich war (Code 200)
    response.raise_for_status() 
    
    # 2. Die Antwort in ein Python-Format (Dictionary) umwandeln
    data = response.json()
    
    # 3. Die Daten ansehen
    print("\n--- Antwort vom Server (JSON) ---")
    print(data)
    print("-----------------------------------")
    
    # 4. Nur die wichtigen Informationen heraussuchen
    aktuelle_uhrzeit = data["time"]
    datum = data["date"]
    
    print(f"\nDie Live-Uhrzeit ist: {aktuelle_uhrzeit} Uhr")
    print(f"Das Datum ist: {datum}")

except requests.exceptions.HTTPError as errh:
    print(f"\nFEHLER: HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"\nFEHLER: Verbindung fehlgeschlagen! WLAN verbunden? {errc}")
except Exception as e:
    print(f"\nFEHLER: Ein unerwarteter Fehler ist aufgetreten: {e}")
