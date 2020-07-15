#PUNTO 5
import json
from urllib.request import urlopen

def eliminar_tildes(palabra):
    '''. Recibe una palabra.
    . Devuelve la palabra sin tildes.
    '''
    palabra = palabra.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    return palabra

def comprobar_datos(pronostico, ubicacion):
    '''Comprueba que la ciudad y provincia ingresada por el usuario exista en las
       ciudades y provincias del pronostico
    . Recibe la informacion del pronostico y una lista llamada ubicacion con la
    ciudad y provincia ingresada por el usuario.
    . En caso de existir esa ubicacion, la retorna.
    '''
    continuar = True
    while continuar == True:
        for zona in pronostico:
            if eliminar_tildes(zona['name'].lower()) in ubicacion[0] and eliminar_tildes(zona['province'].lower()) in ubicacion[1]:
                continuar = False
        
        if continuar == True:
            print("Los datos ingresados no son validos, ingrese nuevamente")
            ciudad = input("Ingrese ciudad: ")
            provincia = input("Ingrese provincia: ")
            ubicacion = [eliminar_tildes(ciudad.lower()), eliminar_tildes(provincia.lower())]
    return ubicacion

def mostrar_pronostico(pronostico, ubicacion):
    '''Recibe informacion del pronostico y lo muestra para una ubicacion determinada.
    '''
    for zona in pronostico:
        if eliminar_tildes(zona['name'].lower()) in ubicacion[0] and eliminar_tildes(zona['province'].lower()) in ubicacion[1]:
            print(f"Pronostico de {zona['name']},{zona['province']} a {zona['weather']['day']} dias")
            print(".Temperatura en la mañana: ", zona['weather']['morning_temp'])
            print(".Pronostico de la mañana: ", zona['weather']['morning_desc'].replace(".",".\n"))
            print(".Temperatura en la tarde: ", zona['weather']['afternoon_temp'])
            print(".Pronostico de la tarde: ", zona['weather']['afternoon_desc'].replace(".",".\n"))

def pronostico_extendido(): #main
    with urlopen("https://ws.smn.gob.ar/map_items/forecast/1") as page:
        source = page.read()
    un_dia = json.loads(source)
    with urlopen("https://ws.smn.gob.ar/map_items/forecast/2") as page:
        source = page.read()
    dos_dias = json.loads(source)
    with urlopen("https://ws.smn.gob.ar/map_items/forecast/3") as page:
        source = page.read()
    tres_dias = json.loads(source)
    
    ciudad = input("Ingrese ciudad: ")
    provincia = input("Ingrese provincia: ")
    ubicacion = [eliminar_tildes(ciudad.lower()), eliminar_tildes(provincia.lower())]
    ubicacion = comprobar_datos(un_dia, ubicacion)
    
    print("")
    mostrar_pronostico(un_dia, ubicacion)
    mostrar_pronostico(dos_dias, ubicacion)
    mostrar_pronostico(tres_dias, ubicacion)
    
    pause = input("Presione una tecla para continuar...")

pronostico_extendido()
