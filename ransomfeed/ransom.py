import sys
import importlib
from requests_html import HTMLSession
from datetime import datetime
import xlsxwriter
from config.group_defaults import group_defaults
import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()

# Funzione per determinare il trimestre in base al mese
def get_quarter(month):
    return (month - 1) // 3 + 1

# Funzione per determinare il mese all'interno del trimestre
def get_month_in_quarter(month):
    return (month - 1) % 3 + 1

# Funzione per ottenere lo stato e la regione della vittima utilizzando l'API di Google Maps
def get_state(victim, config):
    google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')

    if not google_maps_api_key:
        print("Error: GOOGLE_MAPS_API_KEY not found in .env file")
        return 'Unknown', 'Unknown'

    gmaps = googlemaps.Client(key=google_maps_api_key)
    places_result = gmaps.places(query=f"{victim} {config.COUNTRY}")
    if places_result['status'] == 'OK' and places_result['results']:
        place = places_result['results'][0]
        place_details = gmaps.place(place_id=place['place_id'])
        if place_details['status'] == 'OK':
            address_components = place_details['result']['address_components']
            
            # Gestione speciale per la Spagna
            if config.COUNTRY.lower() == 'spain':
                state = next((comp['long_name'] for comp in address_components if 'administrative_area_level_2' in comp['types']), '')
            else:
                state = next((comp['long_name'] for comp in address_components if 'administrative_area_level_1' in comp['types']), '')
            
            state = config.STATE_TRANSLATIONS.get(state, state)
            region = next((r for r, states in config.REGIONS.items() if state in states), '')
            return region, state
        
    return '', ''

def main(country, ransom_id):
    # Importazione dinamica della configurazione specifica del paese
    try:
        config = importlib.import_module(f'config.{country.lower()}_config')
    except ImportError:
        print(f"Configuration for {country} not found.")
        sys.exit(1)

    s = HTMLSession()
    response = s.get(config.URL)
    table = response.html.xpath('//div/table/tbody/tr')
    data = []
    current_date = datetime.now()
    current_date = current_date.strftime("%d/%m/%Y")

    # Elaborazione di ogni riga della tabella
    for row in reversed(table):
        cells = row.find('td')
        if int(cells[0].text) >= int(ransom_id):
            id = cells[0].text
            date_raw = cells[1].text
            victim = cells[2].text
            group = cells[3].text
            
            # Conversione e formattazione della data
            date = datetime.strptime(date_raw, '%Y-%m-%d %H:%M:%S')
            year = date.year
            month = date.month
            quarter = get_quarter(month)
            month_in_quarter = get_month_in_quarter(month)

            # Ottenimento della regione e dello stato se l'API è abilitata
            if config.API:
                region, state = get_state(victim, config)
            else:
                region, state = '', ''

            common_data = config.get_common_data(victim, region, state, month_in_quarter, quarter, year)

            # Gestione speciale per la Spagna
            if country.lower() == 'spain':
                spain_specific_data = config.get_spain_specific_data(state)
            else:
                spain_specific_data = ['', '']

            # Creazione della riga di dati in base al gruppo di ransomware
            if group in group_defaults:
                group_values = group_defaults[group]
                group_name = group_values[0]
                data.append(common_data + [
                    group_name, '',
                    f"L'azienda {victim} è stata colpita da un attacco ransomware sferrato dalla cybergang {group_name}",
                    '', '', 'Simone Felici',
                    f'https://ransomfeed.it/index.php?page=post_details&id_post={id}',
                    current_date
                ] + spain_specific_data + list(group_values[1:]))
            else:
                data.append(common_data + [
                    group, '',
                    f"L'azienda {victim} è stata colpita da un attacco ransomware sferrato dalla cybergang {group}",
                    '', '', 'Simone Felici',
                    f'https://ransomfeed.it/index.php?page=post_details&id_post={id}',
                    current_date
                ] + spain_specific_data + [
                    'unknown', 'unknown', 'unknown', 'unknown', 'unknown',
                    'unknown', 'unknown', 'unknown', 'unknown', 'unknown',
                    'Data from Local System', 'unknown', 'unknown', 'Data Encrypted for Impact', 'NO', ''
                ])

    # Creazione e scrittura del file Excel
    new_file = f"output_{config.COUNTRY}.xlsx"
    workbook = xlsxwriter.Workbook(new_file)
    worksheet = workbook.add_worksheet('Details')

    date_format = workbook.add_format({'num_format': 'mm/dd/yyyy'})

    for row_idx, row_data in enumerate(data):
        for col_num, cell_value in enumerate(row_data):
            if isinstance(cell_value, datetime):
                worksheet.write_datetime(row_idx, col_num, cell_value, date_format)
            elif isinstance(cell_value, str) and cell_value.startswith('http'):
                worksheet.write_url(row_idx, col_num, cell_value)
            else:
                worksheet.write(row_idx, col_num, cell_value)

    workbook.close()

    print(f"File salvato come {new_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 ransom.py <country> <ransom_id>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])