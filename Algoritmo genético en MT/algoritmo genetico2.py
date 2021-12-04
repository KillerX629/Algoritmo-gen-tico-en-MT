"""un viajero debe elegir que llevar en su mochila, disponiendo de 4 elecciones:
 1. Bolsa de dormir,
 2. Bolsa de comida,
 3. equipo de camping,
 4. zapatos extra.
 
 además, cada uno de los ítems enumerados, tiene un peso y un valor.
 
 mediante un algoritmo genético, el viajero debe elegir los ítems que llevará en su mochila,
 sabiendo que el peso máximo de la mochila es de 20 kilos, y el valor mínimo de la mochila es de 100 dólares."""

from MT_classes import *
import random
#importamos una libreria para generar un GUI
from tkinter import *

def generar_poblacion(tamano_poblacion):
    poblacion = []
    for i in range(tamano_poblacion):
        poblacion.append(generar_individuo())
    return poblacion

def generar_individuo():
    individuo = []
    for i in range(4):
        individuo.append(random.randint(0, 1))
    return individuo

def calcular_aptitud(individuo):
    vPeso = [7, 6, 8, 2]#pesos de los items
    vValor = [4, 5, 6, 3]#valores de los items
    peso_total = 0
    valor_total = 0
    for i in range(4):
        if individuo[i] == 1:
            peso_total += vPeso[i]
            valor_total += vValor[i]
    return valor_total if peso_total <= 20  else 0

def cruce(padre, madre):
    corte = random.randint(0, 3)
    hijo = madre[:corte] + padre[corte:]
    return hijo


def cruceTuring(padre, madre):
    parentezco = [0, 0, 0, 0]

    MT = maquinaDeTuring(4)
    for i in range(4):
        if random.random() < 0.5:
            parentezco[i]+=1
    parentezco.append('F')
    MT.cargarCinta(0, parentezco)
    MT.cargarCinta(1, madre)
    MT.cargarCinta(2, padre)
    MT.cargarCinta(3, [0, 0, 0, 0]) #esta cinta es para guardar el hijo
    MT.estado = 'Cruce'
    MT.ejecutar()
    return(MT.cinta[3].lista)
    
    
    


def mutacion(individuo):
    for i in range(4):
        if random.random() < 0.1:
            individuo[i] = 1 if individuo[i] == 0 else 0
    return individuo

#creamos una funcion que ordena la poblacion de mayor a menor aptitud
def seleccion_de_poblacion(poblacion):
    poblacion.sort(key=calcular_aptitud, reverse=True)
    return poblacion[:100]

#creamos a una funcion que seleccione dos de los mejores individuos  de la poblacion al azar y los cruce
def seleccion_de_padres(poblacion):
    padres = []
    for i in range(2):
        padres.append(poblacion[random.randint(0, int(len(poblacion)/2))])
    return padres

#definimos una funcion que imprima el mejor individuo de la poblacion, con su aptitud y su peso
def mejor_individuo(poblacion):
    print("Mejor individuo: ", poblacion[0], " con aptitud: ", calcular_aptitud(poblacion[0]), " y peso: ", calcular_peso(poblacion[0]))

#definimos una funcion que calcule el peso de un individuo
def calcular_peso(individuo):
    vPeso = [7, 6, 8, 2]#pesos de los items
    peso_total = 0
    for i in range(4):
        if individuo[i] == 1:
            peso_total += vPeso[i]
    
    return peso_total






def main():
    tasaCruce = 0.8
    tasaMutacion = 0.1
    tamano_poblacion = 5
    poblacion = generar_poblacion(tamano_poblacion)
    for i in range(20):
        poblacion = seleccion_de_poblacion(poblacion)
        hijos = []
        for i in range(len(poblacion)):
            if random.random() < tasaCruce:
                padres = seleccion_de_padres(poblacion)
                hijos.append(cruceTuring(padres[0], padres[1]))
        for i in range(len(hijos)):
            if random.random() < tasaMutacion:
                hijos[i] = mutacion(hijos[i])
        poblacion = poblacion + hijos
        mejor_individuo(poblacion)


if __name__ == '__main__':
    main()