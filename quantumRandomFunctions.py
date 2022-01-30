from random import choice
import qsharp
from QuantumRandomNumberGenerator import RandomNumberInRange

def qrandrange(mini,maxim):
    x = RandomNumberInRange.simulate(max=maxim)

    while x < mini:
        x = RandomNumberInRange.simulate(max=maxim)

    return x

def qchoice(lista):
    index = qrandrange(0,len(lista)-1)
    return lista[index]


