from math import gamma
import random
from random import seed, randint

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
    juego(0, 1, True)
    