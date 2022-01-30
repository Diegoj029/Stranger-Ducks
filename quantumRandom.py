from random import choice
import qsharp
from Qrng import RandomNumberInRange

def qrandrange(mini,maxim):
    x = RandomNumberInRange.simulate(max=maxim)

    while x < mini:
        x = RandomNumberInRange.simulate(max=maxim)

    return x

def qchoice(lista):
    index = qrandrange(0,len(lista)-1)
    return lista[index]


# for i in range(100):
#     print(qrandrange(30,750))

# lista = list(range(0,100,3))
# print('-*-*-*-*-*-*-*-*')
# print(lista)
# for i in range(5):
#     print(qchoice(lista))