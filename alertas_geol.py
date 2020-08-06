# Por favor reestructuren esto, las "configuraciones" globales de latitud y longitud son irrelevantes (tormenta.py)
import json
import csv
import urllib.error
from urllib.request import urlopen  # recheckear esto


def alertas_nacional():
    """Muestra todas las alertas existentes a nivel nacional"""
    with urlopen("https://ws.smn.gob.ar/alerts/type/AL") as page:
        source = page.read()
    alertas = json.loads(source)

    for datos in alertas:
        print('Tipo de alerta: ', datos['title'], '\n')
        print('Descripcion: ', datos['description'].replace(".", ".\n"))
        for zona in datos['zones'].values():
            print('Zona: ', zona)
        print('\n----------------------------\n')


def ingresar_lat_long():  # toda esta funcion se puede reestructurar con un loop for pero la deje asi por claridad
    # debido que no consume muchos recursos ni son tantas lineas de codigo
    negative = False
    lat = input("Ingrese la latitud deseada: ")
    if "-" in lat:  # todo este baile con lo del negativo es pq "-" no es un caracter numerico, si bien La Arg toda
        # lat/lon es negativa, de esta manera se  podria implementar para paises en los que necesariamente no sea asi.
        lat = lat.lstrip('-')
        negative = True
    while not lat.isnumeric():
        print(f"{lat} no es un valor valido reintentelo:")
        lat = input("Ingrese la latitud deseada: ")
    if negative:
        lat = "-" + lat
    lat = round(float(lat))

    negative = False
    lon = input("Ingrese la longitud deseada: ")
    if "-" in lon:
        lon = lon.lstrip('-')
        negative = True
    while not lon.isnumeric():
        print(f"{lon} no es un valor valido reintentelo:")
        lon = input("Ingrese la longitud deseada: ")
    if negative:
        lon = "-" + lon
    lon = round(float(lon))
    return [lat, lon]


def coordenadas_a_provincia(informacion_de_provincias, lat, lon):  # "actual" que...? -F
    ubicacion = []
    existe_ubicacion = False
    while not existe_ubicacion:  # while not existe_ubicacion: (-F)
        for ciudad in informacion_de_provincias:  # Nombres descriptivos! Un tipo no dice nada -F
            if round(float(ciudad["lat"])) == lat and round(float(ciudad["lon"])) == lon:
                ubicacion = [ciudad["name"], ciudad["province"], lat, lon]
                existe_ubicacion = True

        if not existe_ubicacion:  # if not existe_ubicacion (-F)
            print("\nLas coordenadas ingresadas no son validas, ingrese nuevamente.")
            print("\nLas posibles lat/long en las provincias son:")
            for ciudad in informacion_de_provincias:
                print(f'Provincia: {ciudad["province"]}, Ciudad: {ciudad["name"]} ,lat:{round(float(ciudad["lat"]))}'
                      f', long: {round(float(ciudad["lon"]))}')
            # Quizas convenga listar todas las lat/lon de actual..? -F
            coordenadas = ingresar_lat_long()
            lat = coordenadas[0]
            lon = coordenadas[1]

    return ubicacion


# Diccionario o CSV!!! -F
def ubicador(lat, long, user_province):
    lat_en_provincia = None
    long_en_provincia = None
    print([lat, long, user_province])
    try:
        with open('Provincias_secciones.csv', 'r') as provincias_csv:
            provincias = csv.reader(provincias_csv)
            for provincia in provincias:
                if user_province == provincia[0]:
                    if int(provincia[2]) <= lat <= int(provincia[1]):
                        lat_en_provincia = "norte"
                    elif int(provincia[3]) <= lat <= int(provincia[2]):
                        lat_en_provincia = "sur"
                    if int(provincia[4]) <= long <= int(provincia[5]):
                        long_en_provincia = "oeste"
                    elif int(provincia[5]) <= long <= int(provincia[6]):
                        long_en_provincia = "este"
        print([lat_en_provincia, long_en_provincia])
        return [lat_en_provincia, long_en_provincia]
    except FileNotFoundError as error:
        print("No se pudo encontrar el archivo csv 'Provincias_secciones.csv' por favor asegurese que este esté en el "
              "mismo directorio que tormenta.py, tras hacerlo reinicie el programa")
        print(error)


def imprimir_alertas(ubicacion, coordenadas, alertas):
    lista_alertas = []
    for dicc in alertas:
        for zona in dicc["zones"]:
            if ubicacion[1] in dicc["zones"][zona] and (
                    coordenadas[0] in dicc["zones"][zona] or coordenadas[1] in dicc["zones"][zona]):
                lista_alertas.append(dicc["title"])

    if len(lista_alertas) >= 1:
        print(f"\nAlertas en {ubicacion[0]}, {ubicacion[1]} son:")
        print(".", '\n.'.join(lista_alertas))
    else:
        print(f"\nLa geolocalizacion {ubicacion[0]} no sufre ninguna alerta")


def mostrar_alertas_puntuales(lat, lon):  # main
    try:
        with urlopen(
                "https://ws.smn.gob.ar/map_items/weather") as response_informacion_de_provincias:  # link estado actual
            informacion_de_provincias_json = response_informacion_de_provincias.read()  # convierto a bytes lo obtenido en response a un str,
        informacion_de_provincias = json.loads(
            informacion_de_provincias_json)  # aca termino de convertir lo obtenido de la pagina web en un dict de python
        with urlopen("https://ws.smn.gob.ar/alerts/type/AL") as response_alertas:
            alertas_source = response_alertas.read()  # convierto a bytes lo obtenido en response a un str,
        alertas = json.loads(alertas_source)
        opcion_usuario = input("\nDesea usar la geolocalizacion actual? ('si'/'no')?:")
        while opcion_usuario != "si" and opcion_usuario != "no":
            opcion_usuario = input("\nLa opcion ingresada no es valida, ingrese una nueva:")
        if opcion_usuario == "no":
            lat_lon = ingresar_lat_long()
            lat = lat_lon[0]
            lon = lat_lon[1]             
        ubicacion = coordenadas_a_provincia(informacion_de_provincias, lat, lon)
        lat = ubicacion[2]
        lon = ubicacion[3]
        coordenadas = ubicador(lat, lon, ubicacion[1])
        imprimir_alertas(ubicacion, coordenadas, alertas)

    except urllib.error.URLError or socket.gaierror:
        print("Checke su conexion a internet por favor, el programa tormenta.py necesita de internet para funcionar,"
              "si su conexion a internet esta funcionando puede ser que el servidor del servicio meteorologico de la "
              "ciudad este teniendo problemas, en tal caso intente más tarde.")

