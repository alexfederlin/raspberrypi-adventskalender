import feedparser
import time

# Die URL des RSS-Feeds, den wir abfragen wollen
# Hier: BBC News Top Stories (sehr zuverlässig)
#RSS_URL = "http://feeds.bbci.co.uk/news/rss.xml"

# Alternative deutsche Quelle (oft stabil):
RSS_URL = "https://www.tagesschau.de/xml/rss2/"

print(f"Verbinde mit Nachrichten-Feed: {RSS_URL}")

try:
    # 1. Den Feed lesen und die Daten speichern
    # feedparser macht die ganze schwere Arbeit, das XML zu übersetzen
    feed = feedparser.parse(RSS_URL)
    
    # 2. Prüfen, ob der Abruf funktioniert hat
    if feed.status != 200 and feed.status != 301 and feed.status != 302:
        print("\nFEHLER: Konnte den Feed nicht abrufen (Status != 200).")
        print("Mögliche Ursache: Keine Internetverbindung oder Feed-URL ist falsch.")
    else:
        # 3. Die Gesamtanzahl der Einträge ausgeben
        print(f"\n--- {feed.feed.title} ---")
        print(f"Abgerufen. ({len(feed.entries)} aktuelle Meldungen)")
        
        # 4. Die ersten 5 Schlagzeilen durchlaufen
        print("\nDie 5 neuesten Schlagzeilen:")
        
        # Wir nehmen nur die ersten 5 Einträge (News-Artikel)
        for i in range(5):
            # Wir holen den Titel des i-ten Eintrags
            titel = feed.entries[i].title
            
            # Wir geben die Schlagzeile aus
            print(f"[{i+1}] {titel}")
            
        # Bonus: Zeige das Datum der letzten Aktualisierung
        #print(f"\nLetzte Aktualisierung: {feed.feed.published}")


except Exception as e:
    print(f"\nFEHLER: Ein unerwarteter Fehler ist aufgetreten: {e}")