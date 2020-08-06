import matplotlib.pyplot as plt
import csv
import pandas as pd


# No es necesario, pero quizas convenga hacer una funcion generica que le pases argumentos como la tabla de datos,
# el rango, el nombre de los "labels" y asi seguimos, de vuelta, no es necesario, pero para hacerlas mas abstractas conviene -F
def graficar_temp(data_frame):
    max_t = data_frame[["Year", "Max Temperature"]].groupby("Year",
                                                            as_index=False).mean()  # groupby lo que hace es agrupar la informacion de la columna "Max/Min temp" segun los valores de la columna "year"
    min_t = data_frame[["Year", "Min Temperature"]].groupby("Year",
                                                            as_index=False).mean()  # en criollo seria agarra las temp agrupalas segun el anio y desp hace el promedio
    plt.plot(max_t["Year"], max_t["Max Temperature"], "r-", label="Max")
    plt.plot(min_t["Year"], min_t["Min Temperature"], "b-", label="Min")
    plt.plot(max_t["Year"], max_t["Max Temperature"], "ro")
    plt.plot(min_t["Year"], min_t["Min Temperature"], "bo")
    # plt.plot(["2015","2016","2017","2018","2019"], [25, 24, 22, 27, 29], "r-", label="Max") #valores hardcodeado para testear
    # plt.plot(["2015","2016","2017","2018","2019"], [17, 14, 20, 18, 23], "b-", label="Min")
    # plt.plot(["2015","2016","2017","2018","2019"], [25, 24, 22, 27, 29], "ro")
    # plt.plot(["2015","2016","2017","2018","2019"], [17, 14, 20, 18, 23], "bo")
    plt.ylabel('Tempetura')
    plt.xlabel('año')
    plt.legend(loc="best")
    plt.grid()
    plt.show()


def graficar_hum(data_frame):
    humedad = data_frame[["Year", "Relative Humidity"]].groupby("Year", as_index=False).mean()
    plt.plot(humedad["Year"], humedad["Relative Humidity"], "c-", label="Hum")
    plt.plot(humedad["Year"], humedad["Relative Humidity"], "co")
    plt.ylabel('humedad')
    plt.xlabel('Año')
    plt.legend(loc="best")
    plt.grid()
    plt.show()


def graficar_mm(data_frame):
    mm = data_frame[["Year", "Precipitation"]].groupby("Year", as_index=False).mean()
    plt.plot(mm["Year"], mm["Precipitation"], "m-", label="mm")
    plt.plot(mm["Year"], mm["Precipitation"], "mo")
    plt.ylabel('mm de lluvia')
    plt.xlabel('Año')
    plt.legend(loc="best")
    plt.grid()
    plt.show()


def graficar_temp_max(data_frame):
    max_t = data_frame[["Year", "Max Temperature"]].groupby("Year", as_index=False).mean()
    plt.plot(max_t["Year"], max_t["Max Temperature"], "r-", label="T-Max")
    plt.plot(max_t["Year"], max_t["Max Temperature"], "ro")
    plt.ylabel('Tempetura_Max')
    plt.xlabel('Año')
    plt.legend(loc="best")
    plt.grid()
    plt.show()


def graficador():  # main
    # Quizas darle al usuario la opcion de dar otro nombre de archivo? -F
    # Y si el archivo no existe, muy probablemente todo esto rompa, aviso. -F
    print("A continuacion ingrese el nombre del archivo csv en el siguiente formato: nombre.csv, asegurece que el "
          "archivo este en el mismo directorio que el programa tormenta")
    archivo_usuario = input(
        "Ingrese el nombre del archivo:")  # RECORDAR COLOCAR EL NOMBRE DEL ARCHIVO EN LA LINEA DE ABAJO!!
    try:
        data_frame = pd.read_csv(archivo_usuario, index_col=False)  # abre el archivo csv como data frame de pandas, 'index_col=False saca el primer index vacio de la primera fila'
        data_frame["Year"] = data_frame["Date"].apply(lambda x: x[-4:])  # apply le pasas una funcion y le ejecuta a cada elemento de la columna. (es un map pero para cada fila)
        print(
            "\n1) Tempeturas promedio de los ultimos 5 años.\n2) Humedad promedio de los ultimos 5 años.\n3) Milímetros máximos de lluvia de los ultimos 5 años.\n4) Temperatura máxima de los ultimos 5 años.")
        opcion = input("\n¿Qué gráfico desea ver?\n Ingrese el numero de la opción que desea: ")
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
            print(f'\n¡Error!, la opción "{opcion}" no es válida. Intente nuevamente')
            print(
                "\n1) Tempeturas promedio de los ultimos 5 años.\n2) Humedad promedio de los ultimos 5 años.\n3) Milímetros máximos de lluvia de los ultimos 5 años.\n4) Temperatura máxima de los ultimos 5 años.")
            opcion = input("\n¿Qué gráfico desea ver?\n Ingrese el numero de la opción que desea: ")

        if opcion == "1":
            graficar_temp(data_frame)
        elif opcion == "2":
            graficar_hum(data_frame)
        elif opcion == "3":
            graficar_mm(data_frame)
        elif opcion == "4":
            graficar_temp_max(data_frame)
    except FileNotFoundError as error:
        print("No se pudo encontrar el archivo ingresado, asegurese que este"
        "bien escrito o que se encuentre en el repositorio,")
        print(error)

