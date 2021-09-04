from math import gamma
import random
from random import seed, randint
import numpy

def juego(Ganadora, Seleccionada, cambio = False):
    assert Ganadora < 3
    assert Ganadora >= 0
    
    # Chabelo quita la puerta que no seleccionaste
    Descartada = next(i for i in range(3) if 
        i != Seleccionada and
        i != Ganadora)
    #El jugador decide cambiar
    if cambio: 
        Seleccionada = next(i for i in range(3) if
        i != Seleccionada and
        i != Descartada)

    return Seleccionada == Ganadora

if __name__ == '__main__':
    puertas = numpy.random.random_integers(0, 2, 10000)
    
    ganadores = [p for p in puertas if juego(1, p)]
    print("Porcentaje de ganadores sin cambio: " + str(len(ganadores)/len(puertas)))
    ganadores = [p for p in puertas if juego(1, p, True)]
    print("Porcentaje de ganadores con cambio: " + str(len(ganadores)/len(puertas)))
