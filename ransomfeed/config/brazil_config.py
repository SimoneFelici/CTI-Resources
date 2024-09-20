COUNTRY = 'Brazil'
URL = 'https://ransomfeed.it/stats.php?page=country-list&country=Brazil&y=0'
API = True

STATE_TRANSLATIONS = {
    'Pará': 'Para',
    'Distrito Federal': 'Distretto Federale',
    'São Paulo': 'San Paolo'
}

REGIONS = {
    'nord': ['Acre', 'Amapá', 'Amazonas', 'Para', 'Rondônia', 'Roraima', 'Tocantins'],
    'nordest': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
    'centro': ['Distretto Federale', 'Goiás', 'Mato Grosso do Sul', 'Mato Grosso'],
    'sudest': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'San Paolo'],
    'sud': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
}

def get_common_data(victim, region, state, month_in_quarter, quarter, year):
    return [
        victim, region, state, COUNTRY, 'incidente', 'cybercrime', 'furto dati',
        month_in_quarter, quarter, year, '', 'Malware', 'high', '',
        'ransomware'
    ]
