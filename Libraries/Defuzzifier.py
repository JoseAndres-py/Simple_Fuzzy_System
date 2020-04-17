
import numpy as np
import matplotlib.pyplot as plt
import Fuzzifier as fz

def centroidMethod(finalArea,uDiscurse):
    #Centroid Method
    xGravitynum = 0
    xGravityden = 0
    for idx,x in enumerate(uDiscurse):
        xGravitynum += x*finalArea[idx]
        xGravityden +=finalArea[idx]

    return xGravitynum/xGravityden

if __name__ == "__main__":

    Valor = 50
    Km = 100

    div = 5

    steps = 1  # Pasos del Universo discurso
    # Establecer conjuntos difusos de la entrada (Precio)
    ud_P = 100 # Universo de discurso
    parBarato=([45, 2.6, 0])
    parEstandar=[60,60/div]
    parCostoso=([30, 3, 100])

    # Establecer conjuntos difusos de la entrada (Kilometraje)
    ud_Km = 300 # Universo de discurso
    parBajo=([120, 2, 0])
    parMedio=([70, 2, 160])
    parAlto=([300, 200/div])

    # Obtener valores ingresados por el usuario
    Valor = int(input('Elija un valor del Vehiculo : '))
    #Evalua en valor en el rango
    while not (Valor>=0 and Valor<=ud_P):
        print('Elija un valor correcto ....')
        Valor = int(input('Elija un valor del Vehiculo : '))

    #Evalua en kilometraje en el rango
    Km = int(input('Elija un kilometraje del Vehiculo : '))
    while not (Km>=0 and Km<=ud_Km):
        print('Elija un valor correcto ....')
        Km = int(input('Elija un kilometraje del Vehiculo : '))

    UBarato=fz.Campana(Valor,parBarato)
    UEstandar=fz.Gauss(Valor,parEstandar)
    UCostoso=fz.Campana(Valor,parCostoso)

    UBajo=fz.Campana(Km,parBajo)
    UMedio=fz.Campana(Km,parMedio)
    UAlto=fz.Gauss(Km,parAlto)

    # Establecer conjuntos difusos de la salida (%)
    salida=np.arange(0,1,0.01)

    parCompra=([0.37, 2, 0.1])
    parNoCompra=([1, 1/div])

    Comprar=fz.Campana(salida,parCompra)
    noComprar=fz.Gauss(salida,parNoCompra)

    #Graficas conjuntos difusos de la entrada (Precio)
    plt.subplot(3, 1, 1)
    plt.plot(range(0,ud_P,steps),fz.Campana(np.arange(0,ud_P,steps),parBarato))
    plt.plot(range(0,ud_P,steps),fz.Gauss(np.arange(0,ud_P,steps),parEstandar))
    plt.plot(range(0,ud_P,steps),fz.Campana(np.arange(0,ud_P,steps),parCostoso))
    plt.xlabel('Precio')
    #plt.ylabel('y axis label')
    plt.title('Conjuntos difusos')
    plt.legend(['Barato', 'Estandar','Costoso'])

    #Graficas conjuntos difusos de la entrada (Kilometraje)
    plt.subplot(3, 1, 2)
    plt.plot(range(0,ud_Km,steps),fz.Campana(np.arange(0,ud_Km,steps),parBajo))
    plt.plot(range(0,ud_Km,steps),fz.Campana(np.arange(0,ud_Km,steps),parMedio))
    plt.plot(range(0,ud_Km,steps),fz.Gauss(np.arange(0,ud_Km,steps),parAlto))
    plt.xlabel('Kilometraje')
    #plt.ylabel('y axis label')
    plt.legend(['Bajo', 'Medio','Alto'])

    #Graficas conjuntos difusos de la salida
    plt.subplot(3, 1, 3)
    plt.plot(salida,Comprar)
    plt.plot(salida,noComprar)
    #plt.ylabel('y axis label')
    plt.legend(['Comprar', 'No Comprar'])

    plt.show()

    #Segunda Parte

    #Base de Reglas (Bajo, Medio, Alto)
    Reglas = [[Comprar,Comprar,noComprar],   # Barato
              [Comprar,noComprar,noComprar],  # Estandar
              [noComprar,noComprar,noComprar]] # Costoso
    Precios = [UBarato,UEstandar,UCostoso] # i
    Kilometraje = [UBajo,UMedio,UAlto]     # j

    finalArea = fz.fuzzy(Reglas,Precios,Kilometraje)

    #Defuzzi
    xGravity = centroidMethod(finalArea,salida)

    plt.plot(salida,finalArea)
    plt.axvline(x=xGravity, color='k', linestyle='--')
    plt.axis([0,1,0,1.1])
    plt.legend(['Ouput Fuzzy', 'Gravity Center'])
    plt.show()
