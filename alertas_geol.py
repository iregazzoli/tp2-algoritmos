import json
from urllib.request import urlopen

def coordenadas_a_provincia(actual, lat, lon):
    ubicacion = []
    existe_ubicacion = False
    while existe_ubicacion == False:
        for dicc in actual:
            if round(float(dicc["lat"])) == lat and round(float(dicc["lon"])) == lon:
                ubicacion = [dicc["name"], dicc["province"]]
                existe_ubicacion = True

        if existe_ubicacion == False:
            print("\nLas coordenadas ingresadas no son validas, ingrese nuevamente.")
            lat = round(float(input("Ingrese la latitud deseada: ")))
            lon = round(float(input("Ingrese la longitud deseada: ")))
    return ubicacion

def ubicador(lat, long, province):
    if province == "Jujuy":
        if -23 <= lat <= -22:
            lat_en_provincia = "norte"
        elif -24.5 <= lat < -23 :
            lat_en_provincia = "sur"
        if -67 <= long < -65.5:
            long_en_provincia = "oeste"
        elif -65.5 <= long <= -64.1:
            long_en_provincia = "este"
    elif province == "Salta":
        if -24 <= lat <= -22:
            lat_en_provincia = "norte"
        elif -26.1 <= lat < -24 :
            lat_en_provincia = "sur"
        if -68.5 <= long < -65:
            long_en_provincia = "oeste"
        elif -65 <= long <= -62.3:
            long_en_provincia = "este"
    elif province == "Formosa":
        if -24.7 <= lat <= -22.5:
            lat_en_provincia = "norte"
        elif -26.7 <= lat < -24.7 :
            lat_en_provincia = "sur"
        if -62.3 <= long < -60:
            long_en_provincia = "oeste"
        elif -60 <= long <= -57.7:
            long_en_provincia = "este"
    elif province == "Tucumán":
        if -26.9 <= lat <= -26.06:
            lat_en_provincia = "norte"
        elif -27.8 <= lat < -26.9:
            lat_en_provincia = "sur"
        if -66.15 <= long < -65.3:
            long_en_provincia = "oeste"
        elif -65.3 <= long <= -64.6:
            long_en_provincia = "este"
    elif province == "Catamarca":
        if -27.1 <= lat <= -25.2:
            lat_en_provincia = "norte"
        elif -29.7 <= lat < -27.1:
            lat_en_provincia = "sur"
        if -68.9 <= long < -67:
            long_en_provincia = "oeste"
        elif -67 <= long <= -65:
            long_en_provincia = "este"
    elif province == "La Rioja":
        if -29.5 <= lat <= -27.7:
            lat_en_provincia = "norte"
        elif -31.9 <= lat < -29.5:
            lat_en_provincia = "sur"
        if -69.5<= long < -67.4:
            long_en_provincia = "oeste"
        elif -67.4 <= long <= -65.5:
            long_en_provincia = "este"
    elif province == "San Juan":
        if -30.6 <= lat <= -28.4:
            lat_en_provincia = "norte"
        elif -32.2 <= lat < -30.6:
            lat_en_provincia = "sur"
        if -70 <= long < -68.7:
            long_en_provincia = "oeste"
        elif -68.7 <= long <= -67.1:
            long_en_provincia = "este"
    elif province == "Santiago del Estero":
        if -27.4 <= lat <= -25.7:
            lat_en_provincia = "norte"
        elif -29.5 <= lat < -27.4:
            lat_en_provincia = "sur"
        if -65.1 <= long < -63.4:
            long_en_provincia = "oeste"
        elif -63.4<= long <= -61.7:
            long_en_provincia = "este"
    elif province == "Chaco":
        if -26.2 <= lat <= -24.2:
            lat_en_provincia = "norte"
        elif -28 <= lat < -26.2:
            lat_en_provincia = "sur"
        if -63.3 <= long < -60.9:
            long_en_provincia = "oeste"
        elif -60.9 <= long <= -58.4:
            long_en_provincia = "este"
    elif province == "Corrientes":
        if -28.7 <= lat <= -27.3:
            lat_en_provincia = "norte"
        elif -30.5 <= lat < -28.7:
            lat_en_provincia = "sur"
        if -59.5 <= long < -57.6:
            long_en_provincia = "oeste"
        elif -57.6 <= long <= -55.7:
            long_en_provincia = "este"
    elif province == "Misiones":
        if -26.8 <= lat <= -25.6:
            lat_en_provincia = "norte"
        elif -28 <= lat < -26.8:
            lat_en_provincia = "sur"
        if -56 <= long < -54.7:
            long_en_provincia = "oeste"
        elif -54.7 <= long <= -53.7:
            long_en_provincia = "este"
    elif province == "Buenos Aires":
        if -36 < lat < -33:
            lat_en_provincia = "norte"
        elif -41 < lat < -36 :
            lat_en_provincia = "sur"
        if -60 < long < -56:
            long_en_provincia = "oeste"
        elif -64 < long < -60:
            long_en_provincia = "este"

    elif province == "La Pampa":
        if -39 < lat < -36:
            lat_en_provincia = "norte"
        elif -41 < lat < -39 :
            lat_en_provincia = "sur"
        if -66 < long < -63:
            long_en_provincia = "oeste"
        elif -68 < long < -66:
            long_en_provincia = "este"

    elif province == "Neuquén":
        if -37 < lat < -34:
            lat_en_provincia = "norte"
        elif -39 < lat < -37 :
            lat_en_provincia = "sur"
        if -70 < long < -67:
            long_en_provincia = "oeste"
        elif -72 < long < -70:
            long_en_provincia = "este"

    elif province == "Río Negro":
        if -40 < lat < -38:
            lat_en_provincia = "norte"
        elif -42 < lat < -40 :
            lat_en_provincia = "sur"
        if -67 < long < -62:
            long_en_provincia = "oeste"
        elif -72 < long < -67:
            long_en_provincia = "este"

    elif province == "Chubut":
        if -44 < lat < -42:
            lat_en_provincia = "norte"
        elif -46 < lat < -44 :
            lat_en_provincia = "sur"
        if -69 < long < -63:
            long_en_provincia = "oeste"
        elif -73 < long < -69:
            long_en_provincia = "este"

    elif province == "Santa Cruz":
        if -49 < lat < -46:
            lat_en_provincia = "norte"
        elif -53 < lat < -49 :
            lat_en_provincia = "sur"
        if -70 < long < -65:
            long_en_provincia = "oeste"
        elif -74 < long < -70:
            long_en_provincia = "este"

    elif province == "Tierra del Fuego, Antártida e Islas del Atlántico Sur":
        if -54 < lat < -53:
            lat_en_provincia = "norte"
        elif -56 < lat < -54 :
            lat_en_provincia = "sur"
        if -67 < long < -64:
            long_en_provincia = "oeste"
        elif -69 < long < -67:
            long_en_provincia = "este"

    elif province == "Mendoza":
        if -35 < lat < -31:
            lat_en_provincia = "norte"
        elif -37 < lat < -35 :
            lat_en_provincia = "sur"
        if -68 < long < -66:
            long_en_provincia = "oeste"
        elif -71 < long < -68:
            long_en_provincia = "este"

    elif province == "San Luis":
        if -34 < lat < -32:
            lat_en_provincia = "norte"
        elif -36 < lat < -34 :
            lat_en_provincia = "sur"
        if -66 < long < -64:
            long_en_provincia = "oeste"
        elif -68 < long < -66:
            long_en_provincia = "este"

    elif province == "Córdoba":
        if -32 < lat < -29:
            lat_en_provincia = "norte"
        elif -35 < lat < -32 :
            lat_en_provincia = "sur"
        if -64 < long < -61:
            long_en_provincia = "oeste"
        elif -66 < long < -64:
            long_en_provincia = "este"

    elif province == "Santa Fe":
        if -31 < lat < -27:
            lat_en_provincia = "norte"
        elif -35 < lat < -31 :
            lat_en_provincia = "sur"
        if -61 < long < -59:
            long_en_provincia = "oeste"
        elif -63 < long < -61:
            long_en_provincia = "este"

    elif province == "Entre Ríos":
        if -32 < lat < -29:
            lat_en_provincia = "norte"
        elif -34 < lat < -32 :
            lat_en_provincia = "sur"
        if -59 < long < -57:
            long_en_provincia = "oeste"
        elif -61 < long < -59:
            long_en_provincia = "este"
    return[lat_en_provincia, long_en_provincia]

def imprimir_alertas(ubicacion, coordenadas, alertas):
    lista_alertas = []
    for dicc in alertas:
        for zona in dicc["zones"]:
            if ubicacion[1] in dicc["zones"][zona] and (coordenadas[0] in dicc["zones"][zona] or coordenadas[1] in dicc["zones"][zona]):
                lista_alertas.append(dicc["title"])

    if len(lista_alertas)>=1:
        print(f"\nAlertas en {ubicacion[0]}, {ubicacion[1]} son:")
        print(".", '\n.'.join(lista_alertas))
    else:
        print(f"\nLa geolocalizacion {ubicacion[0]} no sufre ninguna alerta")

def mostrar_alertas_puntuales(lat , lon): #main
    with urlopen("https://ws.smn.gob.ar/map_items/weather") as response_actual: # link estado actual
        actual_source = response_actual.read()  # convierto a bytes lo obtenido en response a un str,
    estado_actual = json.loads(actual_source)
    with urlopen("https://ws.smn.gob.ar/alerts/type/AL") as response_alertas:
        alertas_source = response_alertas.read()  # convierto a bytes lo obtenido en response a un str,
    alertas = json.loads(alertas_source)
    opcion_usuario = input("\nDesea usar la geolocalizacion actual? ('si'/'no')?:")
    while opcion_usuario != "si" and opcion_usuario != "no":
        opcion_usuario = input("\nLa opcion ingresada no es valida, ingrese una nueva:")
    if opcion_usuario == "no":
        lat = round(float(input("\nIngrese la latitud deseada: ")))
        lon = round(float(input("\nIngrese la longitud deseada: ")))
    ubicacion = coordenadas_a_provincia(estado_actual, lat, lon)
    coordenadas = ubicador(lat, lon, ubicacion[1])
    imprimir_alertas(ubicacion, coordenadas, alertas)


