COUNTRY = 'Canada'
URL = 'https://ransomfeed.it/stats.php?page=country-list&country=Canada&y=0'
API = True

STATE_TRANSLATIONS = {
    'Québec': 'Quebec',

}

REGIONS = {
    'Atlantic Provinces': ['New Brunswick', 'Nova Scotia', 'Prince Edward Island', 'Newfoundland and Labrador'],
    'Central Canada': ['Ontario', 'Quebec'],
    'Prairie Provinces': ['Alberta', 'Saskatchewan', 'Manitoba'],
    'West Coast': ['British Columbia'],
    'Northern Territories': ['Yukon', 'Northwest Territories', 'Nunavut']
}

def get_common_data(victim, region, state, month_in_quarter, quarter, year):
    return [
        victim, region, state, 'incidente', 'cybercrime', 'furto dati',
        month_in_quarter, quarter, year, '', 'Malware', 'high', '',
        'ransomware'
    ]
