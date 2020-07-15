import json
from urllib.request import urlopen

def alertas_nacional(): #main
    '''Muestra todas las alertas existentes a nivel nacional.
    '''
    with urlopen("https://ws.smn.gob.ar/alerts/type/AL") as page:
        source = page.read()
    alertas = json.loads(source)

    for datos in alertas:
        print('Tipo de alerta: ', datos['title'], '\n')
        print('Descripcion: ', datos['description'].replace(".",".\n"))
        for zona in datos['zones'].values():
            print('Zona: ', zona)
        print('\n----------------------------\n')
    
    opcion = input("Para volver al menu principal ingrese 0, para salir presione enter: ")

alertas_nacional()
