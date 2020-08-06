import cv2

def detectar_color(imagen_hsv,hsv_min,hsv_max):
    '''Recibe la imagen ingresada por el usuario convertida de BGR (azul,verde,rojo) a HSV (matiz,saturacion,brillo) 
    para poder captar mas colores,y el rango en el que se encuentra el color, el hsv mínimo y el máximo.
    Aplica primero una mascara y luego otra más para convertir todos los datos de los colores a 0 y 1. Dependiendo si están o no
    devuelve True o False.'''

    mascara1 = cv2.inRange(imagen_hsv,hsv_min,hsv_max) 
    mascara = cv2.bitwise_or(mascara1, mascara1 )
    if cv2.countNonZero(mascara) > 0:
        return True
    elif cv2.countNonZero(mascara) == 0:
        return False

def mostrar_alertas(rojo,verde,azul,amarillo,rosa):
    '''Recibe los colores que se desean encontrar y dependiendo si están o no muestra por pantalla las tormentas que se identifican. '''
    print("\nLas alertas identificadas son: ")
    
    if not (rojo and verde and azul and amarillo and rosa):
        print("\nNo hay alertas de lluvias y/o tormentas.") 


    if rojo :
        print("\n-Tormentas de fuerte intensidad.")
    if verde :
        print("\n-Tormentas débiles.")
    if azul :
        print("\n-Lloviznas o lluvias débiles.")
    if amarillo :
        print("\n-Lluvias moderadas a intensas.")
    if rosa : 
        print("\n-Tormentas fuertes y granizo.")  

def analizar_imagen(): #main

    try:
        nombre_imagen = input("\nIngrese el nombre del archivo de imagen: ")
        
        if ".png" not in nombre_imagen:
            print("\n¡Error!. Debe añadir la extension del archivo (.png).")
            nombre_imagen = input("\nIntente nuevamente.\nIngrese el nombre del archivo de imagen: ")
        
        imagen = cv2.imread(nombre_imagen)
        imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

        rojo = detectar_color(imagen_hsv,(175,100,20),(180,255,255))
        verde = detectar_color(imagen_hsv,(40,100,20),(70,255,255))
        azul = detectar_color(imagen_hsv,(80,100,20),(130,255,255))
        amarillo = detectar_color(imagen_hsv,(20,100,20),(35,255,255))
        rosa = detectar_color(imagen_hsv,(140,100,20),(165,255,255))
        
        mostrar_alertas(rojo,verde,azul,amarillo,rosa)

    except cv2.error :
        print("\nEl archivo no existe o no se encuentra en la misma carpeta que Tormenta.py.")     
        print("\nGuarde el archivo .png en la misma carpeta que Tormenta.py y reinicie el programa.")


