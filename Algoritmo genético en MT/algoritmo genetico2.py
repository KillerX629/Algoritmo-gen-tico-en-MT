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


def aptitud_turing(individuo):
    MT = maquinaDeTuring(5)
    individuo.append('F')
    MT.cargarCinta(0, individuo)
    MT.cargarCinta(1, [7, 6, 8, 2,'F'])#pesos de los items
    MT.cargarCinta(2, [4, 5, 6, 3,'F'])#valores de los items
    MT.cargarCinta(3, ['P',0, 0, 0, 0,'F'])#esta cinta es para guardar el peso total de la mochila
    MT.cargarCinta(4, ['P',0, 0, 0, 0,'F'])#esta cinta es para guardar el valor total de la mochila
    MT.estado = 'Aptitud'
    MT.ejecutar()
    individuo.remove('F')
    apt_total = 0
    peso_total = 0
    MT.cinta[3].lista.remove('P')
    MT.cinta[3].lista.remove('F')
    MT.cinta[4].lista.remove('P')
    MT.cinta[4].lista.remove('F')
    for i in range(4):        
        apt_total += MT.cinta[4].lista[i]
        peso_total += MT.cinta[3].lista[i]
    return apt_total if peso_total <= 20  else 0




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


def mutacion_de_turing(individuo):
    MT = maquinaDeTuring(2)
    cintaCambio =[]
    for i in range(4):
        if random.random() < 0.1:
            cintaCambio.append(1)
        else:
            cintaCambio.append(0)
    cintaCambio.append('F')
    individuo.append('F')
    MT.cargarCinta(1, individuo)
    MT.cargarCinta(0, cintaCambio)
    MT.estado = 'Mutacion'
    MT.ejecutar()
    MT.cinta[1].lista.remove('F')
    return(MT.cinta[1].lista)
    
    
    


def mutacion(individuo):
    for i in range(4):
        if random.random() < 0.1:
            individuo[i] = 1 if individuo[i] == 0 else 0
    return individuo

#creamos una funcion que ordena la poblacion de mayor a menor aptitud
def seleccion_de_poblacion(poblacion):
    poblacion.sort(key=aptitud_turing, reverse=True)
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
    tasaCruce = 0.5
    tasaMutacion = 0.25
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
                hijos[i] = mutacion_de_turing(hijos[i])
        poblacion = poblacion + hijos
        print("\n")
        mejor_individuo(poblacion)
        input("Pulsa enter para continuar")


if __name__ == '__main__':
    main()