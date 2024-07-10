import pandas as pd
from geopy.geocoders import Nominatim
import time

# Datei Pfad
file_path = r'C:\Users\roess\Desktop\1.xlsx'

# Daten einlesen
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Geocoder initialisieren
geolocator = Nominatim(user_agent="geoapiExercises")

# Funktion zum Geokodieren
def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Fehler bei der Geokodierung der Adresse {address}: {e}")
    return None, None

# Spalten für die Koordinaten hinzufügen
data['Latitude'] = None
data['Longitude'] = None

# Adressen geokodieren
for idx, row in data.iterrows():
    lat, lon = geocode_address(row['Address'])
    data.at[idx, 'Latitude'] = lat
    data.at[idx, 'Longitude'] = lon
    time.sleep(1)  # Pause einlegen, um die Geocoding-API nicht zu überlasten

# Ergebnis in eine neue Excel-Datei speichern
output_file_path = r'C:\Users\roess\Desktop\geokodiert.xlsx'
data.to_excel(output_file_path, index=False)
print(f"Geokodierte Daten wurden in {output_file_path} gespeichert.")

