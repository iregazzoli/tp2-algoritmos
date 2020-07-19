import json
from urllib.request import urlopen


def imprimir_alertas(provincia, avisos, alertas):
    for dicc in alertas:
        location_in_dicc = False
        for ubicacion in dicc["zones"]:
            if provincia in dicc["zones"][ubicacion]:
                location_in_dicc = True
        if location_in_dicc:
            print(f"Las alertas en {provincia} son:", {dicc["title"]}) #aca el tema es que imprime n lineas como diccionarios triaga el http del json
        else:
            print(f"la ubicacion '{provincia} no sufre ninguna alerta'")


def mostrar_alertas_puntuales():
    with urlopen("https://ws.smn.gob.ar/alerts/type/AC") as response_avisos:
        avisos_source = response_avisos.read()  # convierto a bytes lo obtenido en response a un str
    avisos = json.loads(avisos_source) #LA PAGINA DE MIERDA DEVUELVE COSAS CUANDO SE LE CANTA (SUELE TIRAR [])
    with urlopen("https://ws.smn.gob.ar/alerts/type/AL") as response_alertas:
        alertas_source = response_alertas.read()  # convierto a bytes lo obtenido en response a un str,
    alertas = json.loads(alertas_source)
    # lat = input("Ingrese la latitud deseada")
    # long = input("Ingrese la longitud deseada")
    # llamado al conversor de geolocalizacion a ciudad/provincia (lat, long)
    imprimir_alertas("Chubut", avisos, alertas)


mostrar_alertas_puntuales()
