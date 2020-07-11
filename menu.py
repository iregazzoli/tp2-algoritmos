def menu():
    print("----MENU PRINCIPAL----")
    opciones_principales = "1) Alertas." \
                           "\n2) Histórico de temperaturas y humedad de la zona fértil y productora" \
                           "de la Argentina." \
                           "\n3) Pronóstico extendido." \
                           "\n4) Ingresar una imagen de radar para saber si hay alertas." \
                           "\n5) Salir del programa"
    print(opciones_principales)
    eleccion = input("Ingrese el número de la opcion que desea: ")

    while(eleccion != "1" and eleccion != "2" and eleccion != "3"
            and eleccion != "4" and eleccion != "5"):
        print(f"¡Error!, la opcion {eleccion} no es valida, Intente nuevamente")
        print(opciones_principales)
        eleccion = input("Ingrese el número de la opcion que desea: ")

    if eleccion == "1":
            opciones_alerta = "\n1) Alertas en la geolocalizacion actual." \
                              "\n2) Alertas en una geolocalizacion ingresada manualmente" \
                              "\n3) Alertas a nivel nacional."
            eleccion_alertas = input("Ingrese el número de la opción"
                                     "que desea: ")
            print(opciones_alerta)
            while(eleccion_alertas != "1" and eleccion_alertas != "2" and
                    eleccion_alertas != "3" and eleccion_alertas != "4"):
                print(f"¡Error!, la opcion {eleccion_alertas} no es valida, Intente nuevamente")
                print(opciones_alerta)

            if eleccion == "1":
                print("funcion")
            elif eleccion == "2":
                print("funcion")
            elif eleccion == "3":
                print("funcion")

    elif eleccion == "2":
        opciones_t_h = "1) Gráfico con el promedio de temperaturas " \
                       "anuales de los ultimos 5 años." \
                       "\n2) Gráfico con el promedio de humedad de los ultimos 5 años." \
                       "\n3) Milímetros máximos de lluvia de los últimos 5 años." \
                       "\n4) Temperatura máxima de los últimos 5 años."
        print(opciones_t_h)
        eleccion_historico = input("Ingrese el número de la opción que desea: ")
        while(eleccion_historico != "1" and eleccion_historico != "2"
                and eleccion_historico != "3" and eleccion_historico != "4"):
            print(f"¡Error!, la opcion {eleccion_historico} no es valida, Intente nuevamente")
            print(opciones_t_h)
            eleccion_historico = input("Ingrese el número de la "
                                       "opción que desea: ")

    elif eleccion == "3":
        print("hay que hacer algo")

    elif eleccion == "4":
        print("hay que hacer algo")

    print("Adios")

def main():
    menu()
