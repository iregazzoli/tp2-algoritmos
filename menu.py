import alertas_geol
import alertas_nacional
import analisis_imagenes
import graficos
import pronostico_extendido

def menu():
    terminar_programa = False
    lat = round(float(input("\nIngrese la latitud en la que se encuentra: ")))
    lon = round(float(input("\nIngrese la longitud en la que se encuentra: ")))
    while terminar_programa == False:    
        print("----MENU PRINCIPAL----")
        opciones_principales = "\n1) Alertas." \
                             "\n2) Histórico de temperaturas y humedad de la zona fértil y productora de la Argentina." \
                             "\n3) Pronóstico extendido." \
                             "\n4) Ingresar una imagen de radar para saber si hay alertas." \
                             "\n5) Salir del programa"
        print(opciones_principales)
        eleccion = input("\nIngrese el número de la opcion que desea: ")

        while(eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5"):
            print(f'\n¡Error!, la opción "{eleccion}" no es válida. Intente nuevamente')
            print(opciones_principales)
            eleccion = input("\nIngrese el número de la opción que desea: ")

        if eleccion == "1":
            opciones_alerta = "\n1) Alertas en base a una geolocalización."
                            "\n2) Alertas a nivel nacional." \

            print(opciones_alerta)                
            eleccion_alertas = input("\nIngrese el número de la opción que desea: ")
            
            while(eleccion_alertas != "1" and eleccion_alertas != "2"):
                print(f'\n¡Error!, la opción "{eleccion_alertas}" no es válida. Intente nuevamente')
                print(opciones_alerta)
                eleccion_alertas = input("\nIngrese el número de la opción que desea: ")

            if eleccion_alertas == "1":
                alertas_geol.mostrar_alertas_puntuales(lat , lon)
            elif eleccion_alertas == "2":
                alertas_nacional.analisis_nacional()
                
            print("\n¿Desea volver al menu principal o terminar el programa?")
            continuar = input("\n1) Volver al menu principal.\n2)Terminar el programa.\nIngrese el numero de la opcion que desea: ")
            if continuar != "1" and continuar != "2":
                 print(f'\n¡Error!, la opción "{continuar}" no es válida. Intente nuevamente.')  
                 continuar = input("\n1) Volver al menu principal.\n2)Terminar el programa.\nIngrese el numero de la opcion que desea: ")
            if continuar == "1":
                terminar_programa = False
            elif continuar == "2":
                print("\nPrograma terminado.\n¡Adios!")
                terminar_programa = True    

        elif eleccion == "2":
            graficos.graficador()
            
            print("\n¿Desea volver al menu principal o terminar el programa?")
            continuar = input("\n1) Volver al menu principal.\n2)Terminar el programa.\nIngrese el numero de la opcion que desea: ")
            if continuar != "1" and continuar != "2":
                 print(f'\n¡Error!, la opción "{continuar}" no es válida. Intente nuevamente.')  
                 continuar = input("\n1) Volver al menu principal.\n2)Terminar el programa.\nIngrese el numero de la opcion que desea: ")
            if continuar == "1":
                terminar_programa = False
            elif continuar == "2":
                print("\nPrograma terminado.\n¡Adios!")
                terminar_programa = True                
        
        elif eleccion == "3":
            pronostico_extendido.pronostico_extendido()

            print("hay que hacer algo")
            print("\n¿Desea volver al menu principal o terminar el programa?")
            continuar = input("\n1) Volver al menu principal.\n2)Terminar el programa.\nIngrese el numero de la opcion que desea: ")
            if continuar != "1" and continuar != "2":
                 print(f'\n¡Error!, la opción "{continuar}" no es válida. Intente nuevamente.')  
                 continuar = input("\n1) Volver al menu principal.\n2)Terminar el programa.\nIngrese el numero de la opcion que desea: ")
            if continuar == "1":
                terminar_programa = False
            elif continuar == "2":
                print("\nPrograma terminado.\n¡Adios!")
                terminar_programa = True
            elif continuar == "2":
                print("\nPrograma terminado.\n¡Adios!")
                terminar_programa = True

        elif eleccion == "4":
            analisis_imagenes.analizar_imagen()
            
            print("\n¿Desea volver al menu principal o terminar el programa?")
            continuar = input("\n1) Volver al menu principal.\n2)Terminar el programa.\nIngrese el numero de la opcion que desea: ")
            if continuar != "1" and continuar != "2":
                 print(f'\n¡Error!, la opción "{continuar}" no es válida. Intente nuevamente.')  
                 continuar = input("\n1) Volver al menu principal.\n2)Terminar el programa.\nIngrese el numero de la opcion que desea: ")
            if continuar == "1":
                terminar_programa = False
            elif continuar == "2":
                print("\nPrograma terminado.\n¡Adios!")
                terminar_programa = True
            
        elif eleccion == "5":
            print("\nPrograma terminado.\n¡Adios!")
            terminar_programa = True    

def main():
    menu()

main()    
   
