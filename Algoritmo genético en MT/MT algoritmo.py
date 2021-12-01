from MT_classes import *

"""define la funcion aptitud del algoritmo genético como el valor mas bajo dada una funcion F"""
def aptitud(F, individuo):
    return F(individuo)