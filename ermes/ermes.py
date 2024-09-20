import requests
import xlsxwriter
from datetime import datetime

# Funzioni per ottenere trimestre e mese nel trimestre
def get_quarter(month):
    return (month - 1) // 3 + 1

def get_month_in_quarter(month):
    return (month - 1) % 3 + 1

# Fai la richiesta GET
response = requests.get("https://api.wowphishing.ermessecurity.com/list")
data = response.json()

# Crea un file Excel e un foglio di lavoro
workbook = xlsxwriter.Workbook("output.xlsx")
worksheet = workbook.add_worksheet()

# Definisci l'intestazione
worksheet.write(0, 0, "URL")
worksheet.write(0, 1, "Brand")
worksheet.write(0, 2, "Month")
worksheet.write(0, 3, "Quarter")

# Inserisci i dati
row = 1
for item in reversed(data):
    detection_date = item.get("timeline", {}).get("detection")
    detection_datetime = datetime.fromisoformat(detection_date)
    month = detection_datetime.month
    quarter = get_quarter(month)
    month_in_quarter = get_month_in_quarter(month)
    
    worksheet.write(row, 0, item.get("url"))
    worksheet.write(row, 1, item.get("brand"))
    worksheet.write(row, 2, month_in_quarter)
    worksheet.write(row, 3, quarter)
    
    row += 1

workbook.close()