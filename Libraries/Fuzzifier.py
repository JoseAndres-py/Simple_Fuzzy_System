
import numpy as np
import math
import matplotlib.pyplot as plt


def Trapezoidal(value,t):

    return np.maximum(0,np.minimum((np.minimum((value-t[0])/(t[1]-t[0]),(t[3]-value)/(t[3]-t[2]))),1))

def Triangular(value,t):

    return np.maximum(0,np.minimum((value-t[0])/(t[1]-t[0]),(t[2]-value)/(t[2]-t[1])))

def Gauss(value,t):

    return np.exp(-0.5*(((value-t[0])/t[1])**2))

def Campana(value,t):

    return (1/(1+np.absolute(((value-t[2])/t[0])**(2*t[1]))))

def fuzzy(rules,funMembership1,funMembership2):

    areaFinal = np.zeros(len(rules[0][0]))

    for i in range(len(funMembership1)):
        for j in range(len(funMembership2)):
            #Obtiene Minimo valueMem1 (And)
            areaFinal = np.maximum(areaFinal,np.minimum(min(funMembership1[i],funMembership2[j]), rules[i][j]))
    return areaFinal

if __name__ == "__main__":

    Valor = 50
    Km = 100

    steps = 1  # Pasos del Universo discurso
    # Establecer conjuntos difusos de la entrada (Precio)
    ud_P = 100 # Universo de discurso
    parBarato=np.array([-1,0,30,70])
    parEstandar=[25,60,85]
    parCostoso=([50,80,100,101])

    # Establecer conjuntos difusos de la entrada (Kilometraje)
    ud_Km = 300 # Universo de discurso
    parBajo=([-1, 0, 50, 200])
    parMedio=([50, 100, 200, 300])
    parAlto=([200, 300, 301])


    UBarato=Trapezoidal(Valor,parBarato)
    UEstandar=Triangular(Valor,parEstandar)
    UCostoso=Trapezoidal(Valor,parCostoso)

    UBajo=Trapezoidal(Km,parBajo)
    UMedio=Trapezoidal(Km,parMedio)
    UAlto=Triangular(Km,parAlto)

    # Establecer conjuntos difusos de la salida (%)
    salida=np.arange(0,1,0.01)

    parCompra=([-0.1, 0, 0.3, 0.8])
    parNoCompra=([0.5, 1, 1.1])

    Comprar=Trapezoidal(salida,parCompra)
    noComprar=Triangular(salida,parNoCompra)

    #Graficas conjuntos difusos de la entrada (Precio)
    plt.subplot(3, 1, 1)
    plt.plot(range(0,ud_P,steps),Trapezoidal(np.arange(0,ud_P,steps),parBarato))
    plt.plot(range(0,ud_P,steps),Triangular(np.arange(0,ud_P,steps),parEstandar))
    plt.plot(range(0,ud_P,steps),Trapezoidal(np.arange(0,ud_P,steps),parCostoso))
    plt.xlabel('Precio')
    #plt.ylabel('y axis label')
    plt.title('Conjuntos difusos')
    plt.legend(['Barato', 'Estandar','Costoso'])

    #Graficas conjuntos difusos de la entrada (Kilometraje)
    plt.subplot(3, 1, 2)
    plt.plot(range(0,ud_Km,steps),Trapezoidal(np.arange(0,ud_Km,steps),parBajo))
    plt.plot(range(0,ud_Km,steps),Trapezoidal(np.arange(0,ud_Km,steps),parMedio))
    plt.plot(range(0,ud_Km,steps),Triangular(np.arange(0,ud_Km,steps),parAlto))
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

    finalArea = fuzzy(Reglas,Precios,Kilometraje)

    RR=finalArea*salida
    COG1=sum(RR)
    COG2=sum(finalArea)

    COG=COG1/COG2

    plt.figure(1)
    plt.plot(salida,Comprar,salida,noComprar)
    plt.axis([0,1,0,1.1])
    plt.grid(True)


    plt.figure(3)
    plt.plot(salida,finalArea)
    plt.axvline(x=COG, linestyle='--')
    plt.axis([0,1,0,1.1])
    plt.grid(True)

    plt.show()

    print(finalArea)
