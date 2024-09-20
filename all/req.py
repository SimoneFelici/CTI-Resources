import requests
import re
import json
from datetime import datetime
import xlsxwriter

current_date = datetime.now()
current_date = current_date.strftime('%d/%m/%Y')

def get_quarter(month):
    return (month - 1) // 3 + 1

def get_month_in_quarter(month):
    return (month - 1) % 3 + 1

url = "https://us-east-1-renderer-read.knack.com/v1/scenes/scene_13/views/view_15/records"

querystring = {
    "callback": "jQuery172011181171911219212_1725380946652",
    "format": "both",
    "page": "1",
    "rows_per_page": "8",
    "sort_field": "field_2",
    "sort_order": "desc",
}

headers = {
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "x-knack-application-id": "6013171b60be8f001cb27363",
    "x-knack-rest-api-key": "renderer"
    }

response = requests.get(url, headers=headers, params=querystring)

json_text = re.search(r'\(\{.*\}\)', response.text).group(0)[1:-1]
data = json.loads(json_text)
excel = []

for record in reversed(data.get("records", [])):
    date = record.get("field_2")

    date = datetime.strptime(date, '%m/%d/%Y')
    year = date.year
    month = date.month
    quarter = get_quarter(month)
    month_in_quarter = get_month_in_quarter(month)

    title = record.get("field_5")
    desc = record.get("field_3")
    link = desc.split("<a href=\"")[1].split("\">")[0]

    print("Year:", year)
    print("Quarter:", quarter)
    print("Month in Quarter:", month_in_quarter)

    print("Title:", title)
    print("Description:", desc)
    print("Link:", link)
    print('----------')

    excel.append([title, month_in_quarter, quarter, year, desc, link, current_date])

workbook = xlsxwriter.Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()

date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})

for row_num, row_data in enumerate(excel):
    for col_num, cell_value in enumerate(row_data):
        if row_num != 0 and col_num == 22:
            worksheet.write(row_num, col_num, datetime.strptime(cell_value, '%d/%m/%Y'), date_format)
        else:
            worksheet.write(row_num, col_num, cell_value)

workbook.close()