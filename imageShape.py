from random import choice
import math
import numpy as np
import cv2

class imageShape:                                               #se crea la clase imageShape
    def __init__(self, width, height):                          # se crea el constructor y recibe los parámetros width y height
        self.width = width                                      # se almacena en el self el valor de width
        self.height = height                                    # se almacena en el self el valor de height

    def generateShape(self):                                    # se crea el método generateShape
        c_width = self.width / 2                                # se calcula la mitad del ancho de la imagen (x/2)
        c_height = self.height / 2                              # se calcula la mitad del alto de la imagen (y/2)
        n = [0, 1, 2, 3]                                        # se crea una lista con el número de figuras disponibles
        self.l = choice(n)                                      # se genera un número aleatorio uniformemente distribuido que toma los valores de n
        #self.l = 1

        if self.l == 0:                                                             # se pregunta por el valor de l
            # generación del triangulo
            img_triangle = np.zeros((self.height, self.width, 3), dtype="uint8")    # se crea una ventana de tamaño (width, height)
            lado_triangle = min(self.width, self.height)/2                          # se calcula el tamaño de los lados del triangulo
            h = ((math.sqrt(3))/2)*lado_triangle                                    # se encuentra el valor de la altura del triangulo

            # se encuentran los puntos(x, y) de los vertices del triangulo para que esté centrado en la ventana
            p1x = int(c_width)                                                      #se encuentra la parte entera de la componente x del vertice 1
            p1y = int(c_height-(h/2))                                               #se encuentra la parte entera de la componente y del vertice 1
            p1 = [p1x, p1y]                                                         #se encuentra el vertice 1 del triangulo

            p2x = int(c_width-(lado_triangle/2))                                    #se encuentra la parte entera de la componente x del vertice 2
            p2y = int(c_height+(h/2))                                               #se encuentra la parte entera de la componente y del vertice 2
            p2 = [p2x, p2y]                                                         #se encuentra el vertice 2 del triangulo

            p3x = int(c_width+(lado_triangle/2))                                    #se encuentra la parte entera de la componente x del vertice 3
            p3y = int(c_height+(h/2))                                               #se encuentra la parte entera de la componente y del vertice 3
            p3 = [p3x, p3y]                                                         #se encuentra el vertice 3 del triangulo

            pts = np.array([p1, p2, p3], np.int32)                                  # genera una lista con los vertices optenidos
            pts = pts.reshape((-1, 1, 2))                                           # Devuelve una matriz que contiene los mismos datos con una nueva forma

            triangle = cv2.polylines(img_triangle, [pts], True, (255, 255, 0),2)    # se crea la imagen del triangulo
            cv2.fillPoly(triangle, [pts], (255, 255, 0))                            # se rellena con color cyan el triangulo
            self.shape = triangle                                                   # se guarda en sefl.sahpe la imagen del triangulo
            self.nombre = 'triangle'                                                # se guarda en self.nombre un strig con el nombre la figura

        if self.l == 1:                                                             # se pregunta por el valor de l
            # generación del cuadrado
            img_square = np.zeros((self.height, self.width, 3), dtype="uint8")      # se crea una ventana de tamaño (width, height)
            lado_square = min(self.width, self.height) / 2                          # se calcula el tamaño de los lados del cuadrado

            # se encuentran los puntos(x, y) de los vertices del cuadrado para que esté centrado en la ventana
            s1x = int((c_width)-(lado_square/2))                                    #se encuentra la parte entera de la componente x del vertice 1
            s1y = int((c_height)-(lado_square/2))                                   #se encuentra la parte entera de la componente y del vertice 1
            s1 = (s1x, s1y)                                                         #se encuentra el vertice 1 del cuadrado

            s2x = int((c_width)+(lado_square/2))                                    #se encuentra la parte entera de la componente x del vertice 2
            s2y = int((c_height)+(lado_square/2))                                   #se encuentra la parte entera de la componente y del vertice 2
            s2 = (s2x, s2y)                                                         #se encuentra el vertice 2 del cuadrado (opuesto al 1)

            square = cv2.rectangle(img_square, s1, s2, (255, 255, 0), -1)           # se crea la imagen del cuadrado
            rote = cv2.getRotationMatrix2D((c_width,c_height),45,1)                 # se rota 45 grados la figura
            square_rote = cv2.warpAffine(square,rote,(self.width,self.height))      # se crea la imagen del cuadrado rotado
            self.shape = square_rote                                                # se guarda en sefl.sahpe la imagen del cuadrado
            self.nombre = 'square'                                                  # se guarda en self.nombre un strig con el nombre la figura

        if self.l == 2:                                                             # se pregunta por el valor de l
            #Rectangulo
            img_rectangle = np.zeros((self.height, self.width, 3), dtype="uint8")   # se crea una ventana de tamaño (width, height)
            lado_horizontal = self.width/2                                          # se calcula el tamaño del lado horizontal
            lado_vertical = self.height/2                                           # se calcula el tamaño del lado vertical

            # se encuentran los puntos(x, y) de los vertices del rectangulo para que esté centrado en la ventana
            r1x = int((c_width)-(lado_horizontal/2))                                #se encuentra la parte entera de la componente x del vertice 1
            r1y = int((c_height)-(lado_vertical/2))                                 #se encuentra la parte entera de la componente y del vertice 1
            r1 = (r1x, r1y)                                                         #se encuentra el vertice 1 del rectangulo

            r2x = int((c_width)+(lado_horizontal/2))                                #se encuentra la parte entera de la componente x del vertice 2
            r2y = int((c_height)+(lado_vertical/2))                                 #se encuentra la parte entera de la componente y del vertice 2
            r2 = (r2x, r2y)                                                         #se encuentra el vertice 2 del rectangulo (opuesto al 1)

            rectangle = cv2.rectangle(img_rectangle, r1, r2, (255, 255, 0), -1)     # se crea la imagen del rectangulo
            self.shape = rectangle                                                  # se guarda en sefl.sahpe la imagen del rectangulo
            self.nombre = 'rectangle'                                               # se guarda en self.nombre un strig con el nombre la figura

        if self.l == 3:                                                             # se pregunta por el valor de l
            #Circulo
            img_circle = np.zeros((self.height, self.width, 3), dtype="uint8")      # se crea una ventana de tamaño (width, height)
            radio = min(self.width, self.height)/4                                  # se encuentra el radio del circulo
            circle = cv2.circle(img_circle, (int(c_width), int(c_height)), int(radio), (255, 255, 0), -1) # se crea la imagen del circulo
            self.shape = circle                                                     # se guarda en sefl.sahpe la imagen del circulo
            self.nombre = 'circle'                                                  # se guarda en self.nombre un strig con el nombre la figura

    def showShape(self):                                                            # se crea el método showShape
        if self.shape is any:                                                       # se pregunta si self.shape no esta disponible
            wnd = np.zeros((self.height, self.width, 3), dtype="uint8")             # se crea una ventana de tamaño (width, height)
            cv2.imshow('no disponible', wnd)                                        # se muestra la ventana con nombre 'no disponible'
            cv2.waitKey(5000)                                                       # se muestra por 5 segundos
            cv2.destroyAllWindows()                                                 # se cierran las ventanas que esten abiertas

        else :                                                                      # si self.shape esta disponible
            cv2.imshow(self.nombre, self.shape)                                     # se muestra la figura creada con su nombre respectivo
            cv2.waitKey(5000)                                                       # se muestra por 5 segundos
            cv2.destroyAllWindows()                                                 # se cierran las ventanas que esten abiertas

    def getShape(self):                                                             # se crea el método getShape
        if self.l == 0:                                                             # se pregunta por el valor de l
            print('Imagen original =', self.nombre)                                 # se imprime el nombre de la imagen original

        if self.l == 1:                                                             # se pregunta por el valor de l
            print('Imagen original =', self.nombre)                                 # se imprime el nombre de la imagen original

        if self.l == 2:                                                             # se pregunta por el valor de l
            print('Imagen original =', self.nombre)                                 # se imprime el nombre de la imagen original

        if self.l == 3:                                                             # se pregunta por el valor de l
            print('Imagen original =', self.nombre)                                 # se imprime el nombre de la imagen original

    def whatShape(self):                                                            # se crea el método whatShape
        image_draw = self.shape.copy()                                              # se crea una copia de la imagen generada
        image_gray = cv2.cvtColor(self.shape, cv2.COLOR_BGR2GRAY)                   # se convierte a grices la imagen

        # se encuentran los contornos de la imagen
        ret, Ibw_shapes = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(Ibw_shapes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        clase = []                                                                  # se crea una lista vacía
        for idx, i in enumerate(contours):                                          # se encuentran los valores de los contornos
            color = (0, 255, 255)
            clase += [len(contours[idx])]                                           # se agregan los valores a la lista
            cv2.drawContours(image_draw, contours, idx, color, 5)                   # se muestran los contornos encontrados
        print(clase)
        # se encuentran los vertices
        canny = cv2.Canny(image_gray, 10, 150)
        canny = cv2.dilate(canny, None, iterations=1)
        canny = cv2.erode(canny, None, iterations=1)
        cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            epsilon = 0.01 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)
            vertices = len(approx)                                                  # se guarda el numero de vertices que se encontro en la imagen

        cv2.imshow("Image", image_draw)                                             # se muestra la imagen con los contornos
        cv2.waitKey(5000)                                                           # se muestra por 5 segundos

        if vertices == 4:                                                           # se pregunta si la clase tiene valor igual a 4
            nombre_detectado = 'square'                                             # si la clase tiene valor 4 se detecta un cuadrado
            print('Imagen detectada =', nombre_detectado)                           # se imprime el nombre de la imagen detectada

        if clase[0] == 8:                                                           # se pregunta si la clase tiene valor igual a 8
            nombre_detectado = 'rectangle'                                          # si la clase tiene valor 4 se detecta un rectangulo
            print('Imagen detectada =', nombre_detectado)                           # se imprime el nombre de la imagen detectada

        if vertices == 3:                                                           # se pregunta si los vertices son 3
            nombre_detectado = 'triangle'                                           # si los vertices son 3 se detecta un triangulo
            print('Imagen detectada =', nombre_detectado)                           # se imprime el nombre de la imagen detectada

        if vertices > 8:                                                            # se pregunta si los vertices son mayor a 8
            nombre_detectado = 'circle'                                             # si los vertices son 3 se detecta un circulo
            print('Imagen detectada =', nombre_detectado)                           # se imprime el nombre de la imagen detectada

        if nombre_detectado == self.nombre:                                         # se pregunta si el nombre de la imagen detectad es igual al de la original
            print('La clasificación realizada es correcta')                         # se imprime que la clasificación es correcta

        else:                                                                       # si los nombres son diferentes
            print('La clasificación realizada es incorrecta')                       # se imprime que la clasificación es incorrecta
