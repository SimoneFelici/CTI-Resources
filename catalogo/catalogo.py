from requests_html import HTMLSession
from datetime import datetime
from googletrans import Translator
from urllib.parse import urljoin
import xlsxwriter
from keywords import keywords

def get_quarter(month):
    return (month - 1) // 3 + 1

def get_month_in_quarter(month):
    return (month - 1) % 3 + 1

session = HTMLSession()
translator = Translator()
i = 5
data = []
current_date = datetime.now()
processed_links = set()

while i > 0:
    r = session.get(f'https://catalogodefraudes.rnp.br/?page={i}')
    print(i)
    links = []
    base_url = 'https://catalogodefraudes.rnp.br'
    for a_tag in r.html.find('a'):
        href = a_tag.attrs.get('href')
        if href and "frauds" in href:
            full_link = urljoin(base_url, href)
            if full_link not in processed_links:
                links.append(full_link)
                processed_links.add(full_link)
    for link in reversed(links):
        print(link)
        r = session.get(link)
        raw_date = r.html.xpath('//*[@id="text-page"]/h4[2]/text()', first=True)
        text = r.html.xpath('//*[@id="text-page"]/p/text()', first=True)
        date = raw_date.split(':')[1].strip()
        date = datetime.strptime(date, '%d/%m/%y')
        year = date.year
        month = date.month
        quarter = get_quarter(month)
        month_in_quarter = get_month_in_quarter(month)
        translated_text = translator.translate(text, src='pt', dest='it').text
        
        severity = "medium"
        sector = ""
        damage = ""
        tag = ""
        
        for keyword, changes in keywords.items():
            if keyword.lower() in translated_text.lower():
                severity = changes.get("severity", severity)
                sector = changes.get("sector", sector)
                tag = changes.get("tag", tag)
                damage = changes.get("damage", damage)
                break
        
        data.append(['many', 'all', '', 'Brazil', 'attacco', 'cybercrime', damage, month_in_quarter, quarter, year, sector, 'Phishing/Social Engineering', 
                     severity, '', '', '', tag, translated_text, '', '', 'Simone Felici', link, current_date, 'unknown', 
                     'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 
                     'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'NO', '' ])
    
    i -= 1

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})

for row_num, row_data in enumerate(data):
    for col_num, cell_value in enumerate(row_data):
        if col_num == 22:
            worksheet.write_datetime(row_num, col_num, cell_value, date_format)
        else:
            worksheet.write(row_num, col_num, cell_value)

workbook.close()