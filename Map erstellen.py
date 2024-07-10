import pandas as pd
import folium

# Datei Pfad
geocoded_file_path = r'C:\Users\roess\Desktop\geokodiert.xlsx'

# Geokodierte Daten einlesen
data = pd.read_excel(geocoded_file_path)

# Karte initialisieren
m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=12)

# Marker zur Karte hinzufügen
for idx, row in data.iterrows():
    if pd.notna(row['Latitude']) and pd.notna(row['Longitude']):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Name']}<br>{row['Address']}<br><a href='{row['Website']}'>{row['Website']}</a>",
            tooltip=row['Name']
        ).add_to(m)

# Karte speichern
map_output_path = r'C:\Users\roess\Desktop\interaktive_karte.html'
m.save(map_output_path)
print(f"Interaktive Karte wurde in {map_output_path} gespeichert.")
