COUNTRY = 'China'
URL = 'https://ransomfeed.it/stats.php?page=country-list&country=China&y=0'
API = False
FILE = 'Threat Intelligence Cina.xlsx'

STATE_TRANSLATIONS = {

}

def get_common_data(victim, region, state, month_in_quarter, quarter, year):
    return [
        victim, COUNTRY, 'incidente', 'cybercrime', 'furto dati',
        month_in_quarter, quarter, year, '', 'Malware', 'high', '',
        'ransomware'
    ]
