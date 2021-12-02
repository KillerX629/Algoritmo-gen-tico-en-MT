from MT_classes import *

class individuo:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None
    




"""define la funcion aptitud del algoritmo genético como el valor mas bajo dada una funcion F"""
def aptitud(F, individuo):
    return F(individuo)


"""define una funcion que dada una lista de individuos, le asigna un valor a cada uno de ellos"""
def evaluar(F, individuos):
    for i in range(len(individuos)):
        individuos[i].fitness = aptitud(F, individuos[i])

def generar_gen():
    return random.randint(-1000,1000)

"""crear una funcion que genere n cantidad de individuos y devuelva una lista"""

def generar_individuos(n):
    individuos = []
    for i in range(n):
        individuos.append(individuo(generar_gen()))
    return individuos




if __name__ == '__main__':
    #preguntar al usuario cuantos individuos quiere generar
    n = int(input("Cuantos individuos quiere generar? "))
    nuevaLista = generar_individuos(n)

   #inicializamos la maquina de turing
    MT = maquinaDeTuring()
    MT.cinta.append('P')
    for i in range(len(nuevaLista)):
        MT.cinta.append(nuevaLista[i])
    MT.cinta.append('F')

    #ejecutamos la maquina de turing
    MT.ejecutar()

    