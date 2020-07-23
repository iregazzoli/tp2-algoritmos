import cv2 
'''En HSV los rangos de colores van H -> (0-180), V->(0-255), S ->(0,255) '''
def detectar_rojo(imagen, imagen_hsv):
    '''Recibe la imagen original y la transformada a HSV, hace una mascara u copia de la foto buscando los colores segun el rango del color,
    y despues convierte la mascara a 1 y 0 y dependiendo si el color está o no en la imagen resuelve.  '''
    
    mascara1 = cv2.inRange(imagen_hsv, (110,100,20), (130,255,255))
    mascara2 = cv2.inRange(imagen_hsv, (175,100,20), (180,255,255)) 
    mascara = cv2.bitwise_or(mascara1, mascara2 )
    if cv2.countNonZero(mascara) > 0:
        print("\n-Tormentas de fuerte intensidad")
    
    elif cv2.countNonZero(mascara) == 0:
        return "no_rojo"

def detectar_verde(imagen, imagen_hsv):
    '''Recibe la imagen original y la transformada a HSV, hace una mascara u copia de la foto buscando los colores segun el rango del color,
    y despues convierte la mascara a 1 y 0 y dependiendo si el color está o no en la imagen resuelve.'''
    
    mascara1 = cv2.inRange(imagen_hsv, (40,100,20), (70,255,255)) 
    mascara = cv2.bitwise_or(mascara1, mascara1 )
    if cv2.countNonZero(mascara) > 0:
        print("\n-Tormentas débiles")
    elif cv2.countNonZero(mascara) == 0:
        return "no_verde"    
    
def detectar_azul(imagen, imagen_hsv):
    '''Recibe la imagen original y la transformada a HSV, hace una mascara u copia de la foto buscando los colores segun el rango del color,
    y despues convierte la mascara a 1 y 0 y dependiendo si el color está o no en la imagen resuelve.  '''
    
    mascara1 = cv2.inRange(imagen_hsv, (80,100,20), (130,255,255)) 
    mascara = cv2.bitwise_or(mascara1, mascara1 )
    if cv2.countNonZero(mascara) > 0:
        print("\n-Lloviznas o lluvias débiles")
    
    elif cv2.countNonZero(mascara) == 0:
        return "no_azul"

def detectar_amarillo(imagen, imagen_hsv):
    '''Recibe la imagen original y la transformada a HSV, hace una mascara u copia de la foto buscando los colores segun el rango del color,
    y despues convierte la mascara a 1 y 0 y dependiendo si el color está o no en la imagen resuelve.  '''
    
    mascara1 = cv2.inRange(imagen_hsv, (80,100,20), (130,255,255)) 
    mascara = cv2.bitwise_or(mascara1, mascara1 )
    if cv2.countNonZero(mascara) > 0:
        print("\n-Lluvias moderadas a intensas")
    
    elif cv2.countNonZero(mascara) == 0:
        return "no_amarillo"

def detectar_rosa(imagen, imagen_hsv):
    '''Recibe la imagen original y la transformada a HSV, hace una mascara u copia de la foto buscando los colores segun el rango del color,
    y despues convierte la mascara a 1 y 0 y dependiendo si el color está o no en la imagen resuelve.  '''
    
    mascara1 = cv2.inRange(imagen_hsv, (140,100,20), (165,255,255)) 
    mascara = cv2.bitwise_or(mascara1, mascara1 )
    if cv2.countNonZero(mascara) > 0:
        print("\n-Tormentas fuertes y granizo")
    
    elif cv2.countNonZero(mascara) == 0:
        return "no_rosa"

def analizar_imagen(): #main
    nombre_imagen = input("\nIngrese el nombre del archivo de imagen: ")
    
    if ".png" not in nombre_imagen:
        print("\n¡Error!. Debe añadir la extension del archivo (.png).")
        nombre_imagen = input("\nIntente nuevamente.\nIngrese el nombre del archivo de imagen: ")
    
    imagen = cv2.imread(nombre_imagen)
    imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) #pasar de BGR(Azul,Verde,Rojo) a HSV(matiz,saturacion,brillo) para trabajar con mas colores
    print("\nLas alertas identificadas son: ")
    detectar_rojo(imagen, imagen_hsv)
    detectar_verde(imagen, imagen_hsv)
    detectar_azul(imagen, imagen_hsv)
    detectar_amarillo(imagen, imagen_hsv)
    detectar_rosa(imagen, imagen_hsv)
    
    if detectar_rojo(imagen, imagen_hsv) == "no_rojo" and detectar_verde(imagen, imagen_hsv) == "no_verde" and detectar_azul(imagen, imagen_hsv) == "no_azul" and detectar_amarillo(imagen, imagen_hsv) == "no_amarillo" and detectar_rosa(imagen, imagen_hsv) == "no_rosa":
        print("\nNo hay alertas de lluvias y/o tormentas.")
