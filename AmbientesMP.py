import copy
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage, TextArea
from time import sleep
from IPython.display import clear_output
import numpy as np
import pandas as pd
import random as rd
from PIL import Image, ImageDraw, ImageFont
import networkx as nx
from itertools import product, permutations
from nltk import Tree


def randMatrix(n): 
    
    matriz = np.zeros((n, n), dtype=int) # Crear una matriz vacía de n x n
    
    # Crear una lista de los números del 1 al n y mezclarla aleatoriamente
    numeros = list(range(1, n+1))
    np.random.shuffle(numeros)
    
    # Agregar los bloques a la matriz de manera aleatoria, asegurándote de que cada bloque tenga otro debajo de él
    while len(numeros)>0:
        for i in range(n):
            r = rd.randint(1, n) # para recorrer filas de manera aleatoria
            
            for j in range(r):
                
               if len(numeros)>0 : 
                 
                    if matriz[j][i] != 0: #si ya hay un bloque, seguir a la siguiente casilla  
                        continue
                   
                    if j == n - 1 and matriz[j][i] == 0:  # si la fila es la ultima, agregamos uno. (para tener bloques en el piso) 
                    
                        matriz[j][i] = numeros.pop()
                       
                    elif matriz[j+1][i] != 0:
                        
                        matriz[j][i] = numeros.pop()

    return matriz         



class BlockWorld:
    '''
    @Autores: Santiago Álvarez y María Fernanda Palacio
    
    '''
    
   


    def __init__(self, num_de_blocks=5, default=True):
        assert(num_de_blocks <= 10)
        self.num_de_blocks = num_de_blocks
        self.estado_inicial = randMatrix(num_de_blocks)
        self.estado_final = randMatrix(num_de_blocks)
        if self.estado_inicial.all()==self.estado_final.all():
            self.estado_final= randMatrix(num_de_blocks)
  

  


    def pintar_estado(self, estado):
        # Dibuja el mundo correspondiente al estado
        # Input: estado, que es una num_de_blocks-lista de num_de_blocks-listas
        n = len(estado)
        fig, axes = plt.subplots()

        # Dibujo el tablero
        step = 1.0 / n
        offset = 0.001
        tangulos = []

        # Borde del tablero
        tangulos.append(
            patches.Rectangle(
                (0, 0),
                0.998,
                0.998,
                facecolor="white",
                edgecolor="white",
                linewidth=2,
            )
        )

        # Creo las líneas del tablero, AL FINAL ESTO PODRIA ELIMINARSE
        for j in range(n):
            locacion = 0.0
            # Crea linea horizontal en el rectangulo
            tangulos.append(
                patches.Rectangle(*[(0, locacion), 1, 0.008], facecolor="black")
            )

        for t in tangulos:
            axes.add_patch(t)

        # Cargando imagenes de los bloques
        arr_img = Image.open("./BlockWorld/BloqueA.png")
        arr_img_2 = Image.open("./BlockWorld/BloqueB.png")
        arr_img_3 = Image.open("./BlockWorld/BloqueC.png")
        arr_img_4 = Image.open("./BlockWorld/BloqueD.png")
        arr_img_5 = Image.open("./BlockWorld/BloqueE.png")
        arr_img_6 = Image.open("./BlockWorld/BloqueF.png")
        arr_img_7 = Image.open("./BlockWorld/BloqueG.png")
        arr_img_8 = Image.open("./BlockWorld/BloqueH.png")
        arr_img_9 = Image.open("./BlockWorld/BloqueI.png")
        arr_img_10 = Image.open("./BlockWorld/BloqueJ.png")
        base_x = 335
        base_y = 220
        arr_img = arr_img.resize((int(base_x / n), int(base_y / n)))
        arr_img_2 = arr_img_2.resize((int(base_x / n), int(base_y / n)))
        arr_img_3 = arr_img_3.resize((int(base_x / n), int(base_y / n)))
        arr_img_4 = arr_img_4.resize((int(base_x / n), int(base_y / n)))
        arr_img_5 = arr_img_5.resize((int(base_x / n), int(base_y / n)))
        arr_img_6 = arr_img_6.resize((int(base_x / n), int(base_y / n)))
        arr_img_7 = arr_img_7.resize((int(base_x / n), int(base_y / n)))
        arr_img_8 = arr_img_8.resize((int(base_x / n), int(base_y / n)))
        arr_img_9 = arr_img_9.resize((int(base_x / n), int(base_y / n)))
        arr_img_10 = arr_img_10.resize((int(base_x / n), int(base_y / n)))
        imagebox = OffsetImage(arr_img)
        imagebox2 = OffsetImage(arr_img_2)
        imagebox3 = OffsetImage(arr_img_3)
        imagebox4 = OffsetImage(arr_img_4)
        imagebox5 = OffsetImage(arr_img_5)
        imagebox6 = OffsetImage(arr_img_6)
        imagebox7 = OffsetImage(arr_img_7)
        imagebox8 = OffsetImage(arr_img_8)
        imagebox9 = OffsetImage(arr_img_9)
        imagebox10 = OffsetImage(arr_img_10)
        imagebox.image.axes = axes
        imagebox2.image.axes = axes
        imagebox3.image.axes = axes
        imagebox4.image.axes = axes
        imagebox5.image.axes = axes
        imagebox6.image.axes = axes
        imagebox7.image.axes = axes
        imagebox8.image.axes = axes
        imagebox9.image.axes = axes
        imagebox10.image.axes = axes
        offsetX = step / 1.975
        offsetY = step / 1.975
        for i in range(n):
            for j in range(n):
                if estado[j, i] == 1:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 2:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox2,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 3:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox3,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 4:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox4,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 5:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox5,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 6:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox6,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 7:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox7,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 8:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox8,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 9:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox9,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)
                elif estado[j, i] == 10:
                    Y = (n - 1) - j
                    X = i
                    ab = AnnotationBbox(
                        imagebox10,
                        [(X * step) + offsetX, (Y * step) + offsetY],
                        frameon=False,
                    )
                    axes.add_artist(ab)

        axes.axis("off")
        return axes

    def pintar_camino(self, camino):
        # Input: lista con el camino de los estados
        # Output: plot con la forma de resolver las torres
        for estado in camino:
            clear_output(wait=True)
            self.pintar_estado(estado)
            plt.show()
            sleep(.5)

    def acciones_aplicables(self, estado):
        # Devuelve una lista de parejas que representan
        # las casillas vacías en las que es permitido
        # poner un bloque.
        # Input: estado, que es una np.matrix(8x8)
        # Output: lista de indices (x,y),(z,w) es decir,
        # el bloque en la posicion (x,y) puede moverse a la posición (z,w)
        # print("--- IN ACCIONES_APLICABLES ---")
        n = len(estado)
        indices_bloqueados = []
        for x in range(n):
            for y in range(n):
                if estado[y, x] != 0:
                    indices_bloqueados.append((x, y))
        casillas_piso = []
        for i in range(n):
            casillas_piso.append((i, n - 1))
        casillas_libres = []
        for i in indices_bloqueados:
            casillas_libres.append((i[0], i[1] - 1))
        # casillas_libres.remove((block[0], block[1] - 1))

        for i in casillas_piso:
            casillas_libres.append(i)

        casillas_libres = [x for x in casillas_libres if x not in indices_bloqueados]
        for i in casillas_libres:
            if i < (0, 0):
                casillas_libres.remove(i)

        casillas_encerradas = []
        for i in indices_bloqueados:
            if (i[0], i[1] - 1) in indices_bloqueados:
                casillas_encerradas.append(i)

        bloques_validos = [
            x for x in indices_bloqueados if x not in casillas_encerradas
        ]

        new_pos = []
        for i in bloques_validos:
            for j in casillas_libres:
                if j != (i[0], i[1] - 1):
                    new_pos.append((i, j))

        return new_pos

    def transicion(self, estado, indices):
        # Devuelve el tablero incluyendo un bloque en el indice
        # Input: estado, que es una np.matrix(8x8)
        #        indice, de la forma (x,y)
        # Output: estado, que es una np.matrix(8x8)
        # print("--- IN TRANSICION ---")
        s = copy.deepcopy(estado)
        x1, y1 = indices[0]
        x2, y2 = indices[1]
        s[y2, x2] = estado[y1, x1]
        s[y1, x1] = 0
        return s

    def transicion_inicial(self, estado, indices, valor):
        # Devuelve el tablero incluyendo una reina en el indice
        # Input: estado, que es una np.matrix(8x8)
        #        indice, de la forma (x,y)
        #        valor, valor numerico que representa el peso del bloque (A:1,B:2,C:3 etc.)
        # Output: estado, que es una np.matrix(8x8)
        # print("--- IN TRANSICION INICIAL---")
        n = len(estado)
        s = copy.deepcopy(estado)
        x = indices[0]
        y = indices[1]

        piso = []
        for i in range(n):
            piso.append((i, n - 1))

        if indices in piso:
            s[y, x] = valor
        elif s[y + 1, x] != 0:
            s[y, x] = valor
        else:
            raise ValueError("No se puede poner un bloque aqui!")
        return s

    def transicion_final(self, estado, indices, valor):
        # Devuelve el tablero incluyendo un bloque en el indice
        # Input: estado, que es una np.matrix(8x8)
        #        indice, de la forma (x,y)
        #        valor, valor numerico que representa el peso del bloque (A:1,B:2,C:3 etc.)
        # Output: estado, que es una np.matrix(8x8)
        # print("--- IN TRANSICION FINAL---")
        n = len(estado)
        s = copy.deepcopy(estado)
        x = indices[0]
        y = indices[1]

        piso = []
        for i in range(n):
            piso.append((i, n - 1))

        if indices in piso:
            s[y, x] = valor
        elif s[y + 1, x] != 0:
            s[y, x] = valor
        else:
            raise ValueError("No se puede poner un bloque aqui!")
        return s

    def test_objetivo(self, estado):
        # Devuelve True/False dependiendo si el estado
        # resuelve el problema o si no
        # Input: estado, que es una np.matrix(8x8)
        # Output: True/False
        # print("--- IN TEST_OBJETIVO ---")
        # print("Determinando si los bloques estan en forma del estado final")
        return (estado == self.estado_final)

    def codigo(self, estado):
        inicial = True
        for i in estado:
            for j in i:
                if inicial:
                    cadena = str(j)
                    inicial = False
                else:
                    cadena += "-" + str(j)
        return cadena

    def costo(self, estado, accion):
        return 1
