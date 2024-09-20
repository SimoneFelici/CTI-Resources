COUNTRY = 'Spain'
URL = 'https://ransomfeed.it/stats.php?page=country-list&country=Spain&y=0'
API = True

STATE_TRANSLATIONS = {
    'Guipúzcoa': 'Gipuzkoa',
    'Illes Balears': 'Baleares',
    'Balearic Islands': 'Baleares',
    'Seville': 'Sevilla',
    'Bizkaia': 'Vizcaya',
}

PROVINCIAS = [
    'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Alicante', 'Málaga', 'Murcia', 'Cádiz', 'Vizcaya', 'Baleares',
    'A Coruña', 'Las Palmas', 'Asturias', 'Santa Cruz de Tenerife', 'Zaragoza', 'Pontevedra', 'Granada', 'Tarragona',
    'Córdoba', 'Girona', 'Gipuzkoa', 'Almería', 'Toledo', 'Badajoz', 'Navarra', 'Jaén', 'Cantabria', 'Castellón',
    'Huelva', 'Valladolid', 'Ciudad Real', 'León', 'Lleida', 'Cáceres', 'Albacete', 'Burgos', 'Salamanca', 'Lugo',
    'Álava', 'La Rioja', 'Ourense', 'Guadalajara', 'Huesca', 'Cuenca', 'Zamora', 'Palencia', 'Ávila', 'Segovia',
    'Teruel', 'Soria', 'Melilla', 'Ceuta'
]

COMUNIDADES_AUTONOMAS = [
    'Comunidad de Madrid', 'Cataluña', 'Comunidad Valenciana', 'Andalucía', 'Región de Murcia', 'País Vasco',
    'Islas Baleares', 'Galicia', 'Canarias', 'Principado de Asturias', 'Aragón', 'Castilla-La Mancha', 'Extremadura',
    'Navarra', 'Cantabria', 'Castilla y León', 'La Rioja', 'Melilla', 'Ceuta'
]

REGIONS = {
    'nord': ['A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Asturias', 'Cantabria', 'Álava', 'Gipuzkoa', 'Vizcaya', 
             'Navarra', 'La Rioja', 'Huesca', 'Teruel', 'Zaragoza', 'Barcelona', 'Girona', 'Lleida', 'Tarragona'],
    'centro': ['Ávila', 'Burgos', 'León', 'Palencia', 'Salamanca', 'Segovia', 'Soria', 'Valladolid', 'Zamora', 
               'Madrid', 'Albacete', 'Ciudad Real', 'Cuenca', 'Guadalajara', 'Toledo', 'Badajoz', 'Cáceres', 
               'Alicante', 'Castellón', 'Valencia', 'Baleares'],
    'sud': ['Almería', 'Cádiz', 'Córdoba', 'Granada', 'Huelva', 'Jaén', 'Málaga', 'Sevilla', 'Murcia', 
            'Ceuta', 'Melilla', 'Las Palmas', 'Santa Cruz de Tenerife']
}

def get_area_geografica(provincia):
    for area, provincias in REGIONS.items():
        if provincia in provincias:
            return area
    return ''

def get_comunidad_autonoma(provincia):
    provincia_to_comunidad = {
        'Madrid': 'Comunidad de Madrid',
        'Barcelona': 'Cataluña',
        'Valencia': 'Comunidad Valenciana',
        'Sevilla': 'Andalucía',
        'Alicante': 'Comunidad Valenciana',
        'Málaga': 'Andalucía',
        'Murcia': 'Región de Murcia',
        'Cádiz': 'Andalucía',
        'Vizcaya': 'País Vasco',
        'Baleares': 'Islas Baleares',
        'A Coruña': 'Galicia',
        'Las Palmas': 'Canarias',
        'Asturias': 'Principado de Asturias',
        'Santa Cruz de Tenerife': 'Canarias',
        'Zaragoza': 'Aragón',
        'Pontevedra': 'Galicia',
        'Granada': 'Andalucía',
        'Tarragona': 'Cataluña',
        'Córdoba': 'Andalucía',
        'Girona': 'Cataluña',
        'Gipuzkoa': 'País Vasco',
        'Almería': 'Andalucía',
        'Toledo': 'Castilla-La Mancha',
        'Badajoz': 'Extremadura',
        'Navarra': 'Navarra',
        'Jaén': 'Andalucía',
        'Cantabria': 'Cantabria',
        'Castellón': 'Comunidad Valenciana',
        'Huelva': 'Andalucía',
        'Valladolid': 'Castilla y León',
        'Ciudad Real': 'Castilla-La Mancha',
        'León': 'Castilla y León',
        'Lleida': 'Cataluña',
        'Cáceres': 'Extremadura',
        'Albacete': 'Castilla-La Mancha',
        'Burgos': 'Castilla y León',
        'Salamanca': 'Castilla y León',
        'Lugo': 'Galicia',
        'Álava': 'País Vasco',
        'La Rioja': 'La Rioja',
        'Ourense': 'Galicia',
        'Guadalajara': 'Castilla-La Mancha',
        'Huesca': 'Aragón',
        'Cuenca': 'Castilla-La Mancha',
        'Zamora': 'Castilla y León',
        'Palencia': 'Castilla y León',
        'Ávila': 'Castilla y León',
        'Segovia': 'Castilla y León',
        'Teruel': 'Aragón',
        'Soria': 'Castilla y León',
        'Melilla': 'Melilla',
        'Ceuta': 'Ceuta'
    }
    return provincia_to_comunidad.get(provincia, 'unknown')

def get_common_data(victim, region, state, month_in_quarter, quarter, year):
    comunidad_autonoma = get_comunidad_autonoma(state)
    area_geografica = get_area_geografica(state)
    return [
        victim,                 # Vittima
        area_geografica,        # area geografica
        COUNTRY,                # Country
        'incidente',            # incidente/attacco/violazione privacy
        'cybercrime',           # tipologia
        'furto dati',           # danno
        month_in_quarter,       # mese
        quarter,                # Quarto
        year,                   # anno
        '',                     # Tipologia Vittima
        'Malware',              # tecniche di attacco
        'high',                 # severity
        '',                     # ( se Malware : nome )
        'ransomware'            # ( se Malware : tipo )
    ]

def get_spain_specific_data(state):
    comunidad_autonoma = get_comunidad_autonoma(state)
    return [state, comunidad_autonoma]