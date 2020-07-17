import matplotlib.pyplot as plt
import csv
import pandas as pd

def graficar_temp(data_frame):
    data_frame["Year"] = data_frame["Date"].apply(lambda x: x[-4:]) #apply le pasas una funcion y le ejecuta a cada elemento de la columna. (es un map pero para cada fila)
    max_t = data_frame[["Year","Max Temperature"]].groupby("Year",as_index=False).mean() #en el archivo csv hay solo dos posibles anios (2013, 2014), esta linea dice toma la columna "year", "Max/Min Temperature"
    min_t = data_frame[["Year","Min Temperature"]].groupby("Year",as_index=False).mean() #y con esos dos agrupamelos con groupby segun pertencen a un anio u el otro y despues haceme el promedio
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
    data_frame["Year"] = data_frame["Date"].apply(lambda x: x[-4:]) #apply le pasas una funcion y le ejecuta a cada elemento de la columna. (es un map pero para cada fila)
    humedad = data_frame[["Year","Relative Humidity"]].groupby("Year",as_index=False).mean()
    plt.plot(humedad["Year"], humedad["Relative Humidity"], "c-", label="Hum")
    plt.plot(humedad["Year"], humedad["Relative Humidity"], "co")
    plt.ylabel('humedad')
    plt.xlabel('Año')
    plt.legend(loc="best")
    plt.grid()
    plt.show()

def graficar_mm(data_frame):
    data_frame["Year"] = data_frame["Date"].apply(lambda x: x[-4:]) #apply le pasas una funcion y le ejecuta a cada elemento de la columna. (es un map pero para cada fila)
    mm = data_frame[["Year","Precipitation"]].groupby("Year",as_index=False).mean()
    plt.plot(mm["Year"], mm["Precipitation"], "m-", label="mm")
    plt.plot(mm["Year"], mm["Precipitation"], "mo")
    plt.ylabel('mm de lluvia')
    plt.xlabel('Año')
    plt.legend(loc="best")
    plt.grid()
    plt.show()

def graficar_temp_max(data_frame):
    data_frame["Year"] = data_frame["Date"].apply(lambda x: x[-4:]) #apply le pasas una funcion y le ejecuta a cada elemento de la columna. (es un map pero para cada fila)
    max_t = data_frame[["Year","Max Temperature"]].groupby("Year",as_index=False).mean()
    plt.plot(max_t["Year"], max_t["Max Temperature"], "r-", label="T-Max")
    plt.plot(max_t["Year"], max_t["Max Temperature"], "ro")
    plt.ylabel('Tempetura_Max')
    plt.xlabel('Año')
    plt.legend(loc="best")
    plt.grid()
    plt.show()


def main():
    data_frame = pd.read_csv("weather.csv",index_col=False) #abre el archivo csv como data frame de pandas, 'index_col=False saca el primer index vacio de la primera fila'
    print("[1] Tempeturas promedio de los ultimos 5 años\n \
    [2] Humedad promedio de los ultimos 5 años\n \
    [3] Milímetros máximos de lluvia de los ultimos 5 años\n \
    [4] Temperatura máxima de los ultimos 5 años\n")
    opcion = input("¿Qué gráfico desea ver?:\n")
    if opcion == "1":
        graficar_temp(data_frame)
    elif opcion == "2":
        graficar_hum(data_frame)
    elif opcion == "3":
        graficar_mm(data_frame)
    elif opcion == "4":
        graficar_temp_max(data_frame)
    else:
        print("la opción no es valida")



main()
