import requests
import re
import json
from datetime import datetime
import xlsxwriter

current_date = datetime.now()
current_date = current_date.strftime('%d/%m/%Y')

# Funzione per determinare il trimestre in base al mese
def get_quarter(month):
    return (month - 1) // 3 + 1

# Funzione per determinare il mese all'interno del trimestre
def get_month_in_quarter(month):
    return (month - 1) % 3 + 1

# URL dell'API da cui recuperare i dati
url = "https://us-east-1-renderer-read.knack.com/v1/scenes/scene_13/views/view_15/records"

# Parametri della query per la richiesta API
querystring = {
    "callback": "jQuery172011181171911219212_1725380946652",
    "format": "both",
    "page": "1",
    "rows_per_page": "8",
    "sort_field": "field_2",
    "sort_order": "desc",
}

# Headers necessari per l'autenticazione e l'identificazione dell'applicazione
headers = {
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "x-knack-application-id": "6013171b60be8f001cb27363",
    "x-knack-rest-api-key": "renderer"
    }

# Esecuzione della richiesta GET
response = requests.get(url, headers=headers, params=querystring)

# Estrazione del JSON dalla risposta utilizzando una regular expression
json_text = re.search(r'\(\{.*\}\)', response.text).group(0)[1:-1]
data = json.loads(json_text)
excel = []

# Elaborazione di ogni record nel JSON
for record in reversed(data.get("records", [])):
    date = record.get("field_2")

    # Conversione e formattazione della data
    date = datetime.strptime(date, '%m/%d/%Y')
    year = date.year
    month = date.month
    quarter = get_quarter(month)
    month_in_quarter = get_month_in_quarter(month)

    title = record.get("field_5")
    desc = record.get("field_3")
    # Estrazione del link dalla descrizione
    link = desc.split("<a href=\"")[1].split("\">")[0]

    print("Year:", year)
    print("Quarter:", quarter)
    print("Month in Quarter:", month_in_quarter)
    print("Title:", title)
    print("Description:", desc)
    print("Link:", link)
    print('----------')

    # Aggiunta dei dati elaborati alla lista per l'Excel
    excel.append([title, month_in_quarter, quarter, year, desc, link, current_date])

# Creazione del file Excel
workbook = xlsxwriter.Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()

date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})

# Scrittura dei dati nel file Excel
for row_num, row_data in enumerate(excel):
    for col_num, cell_value in enumerate(row_data):
        # Gestione speciale per la colonna della data (colonna 22)
        if row_num != 0 and col_num == 22:
            worksheet.write(row_num, col_num, datetime.strptime(cell_value, '%d/%m/%Y'), date_format)
        else:
            worksheet.write(row_num, col_num, cell_value)

workbook.close()