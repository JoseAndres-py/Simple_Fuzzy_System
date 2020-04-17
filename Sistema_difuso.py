
import numpy as np
import matplotlib.pyplot as plt
import argparse

def Trapezoidal(init=10,max_up=40,max_down=60,end=80,maxValue = 1.0,universo_discurso=100,step=1):

    function = np.zeros(int(universo_discurso/step))
    function[int(max_up/step):int(max_down/step)] = maxValue
    #Puntos de ascenso
    min = int(init/step)
    max = int(max_up/step)
    inc = 0;
    #Desenso
    for i in range(min,max):
        function[i] = inc
        inc += maxValue/(max-min)
    # Puntos de descenso
    max = int(max_down/step)
    min = int(end/step)
    inc = maxValue;
    # Descenso
    for i in range(max,min):
        function[i] = inc
        inc -= maxValue/(min-max)

    return function

def Triangular(init=10,max=40,end=80,maxValue = 1.0,universo_discurso=100,step=1):

    function = np.zeros(int(universo_discurso/step))
    #Puntos de ascenso
    min = int(init/step)
    inc = 0;
    #Desenso
    for i in range(min,max):
        function[i] = inc
        inc += maxValue/(max-min)
    # Puntos de descenso
    min = int(end/step)
    inc = maxValue;
    # Descenso
    for i in range(max,min):
        function[i] = inc
        inc -= maxValue/(min-max)

    return function
if __name__ == "__main__":

    maxValue = 1
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--costo", help="Costo del Vehiculo")
    parser.add_argument("-k", "--Kilometraje", help="Kilometraje del Vehiculo")
    args = parser.parse_args()

    steps = 1  # Pasos del Universo discurso

    # Establecer conjuntos difusos de la entrada (Precio)
    ud_P = 100 # Universo de discurso
    Barato = Trapezoidal(0, 0, 30, 70, 1.0, ud_P, steps)
    Estandar = Triangular(25, 60, 85, 1.0, ud_P, steps)
    Costoso = Trapezoidal(55, 80, 100, 100, 1.0, ud_P, steps)

    # Establecer conjuntos difusos de la entrada (Kilometros
    ud_Km = 300 # Universo de discurso
    Bajo = Trapezoidal(0, 0, 50, 200, 1.0, ud_Km, steps)
    Medio = Trapezoidal(50, 100, 200, 300, 1.0, ud_Km, steps)
    Alto = Triangular(200, 300, 300, 1.0, ud_Km, steps)

    # Establecer conjuntos difusos de la salida (%)
    ud_Out = 100 # Universo de discurso
    Comprar = Trapezoidal(0, 0, 30, 80, 1.0, ud_Out, steps)
    noComprar = Triangular(50, 100, 100, 1.0, ud_Out, steps)

    #Graficas conjuntos difusos de la entrada (Precio)
    plt.subplot(3, 1, 1)
    plt.plot(range(0,ud_P,steps),Barato)
    plt.plot(range(0,ud_P,steps),Estandar)
    plt.plot(range(0,ud_P,steps),Costoso)
    plt.xlabel('Precio')
    #plt.ylabel('y axis label')
    plt.title('Conjuntos difusos')
    plt.legend(['Barato', 'Estandar','Costoso'])

    #Graficas conjuntos difusos de la entrada (Kilometraje)
    plt.subplot(3, 1, 2)
    plt.plot(range(0,ud_Km,steps),Bajo)
    plt.plot(range(0,ud_Km,steps),Medio)
    plt.plot(range(0,ud_Km,steps),Alto)
    plt.xlabel('Kilometraje')
    #plt.ylabel('y axis label')
    plt.legend(['Bajo', 'Medio','Alto'])

    #Graficas conjuntos difusos de la salida
    plt.subplot(3, 1, 3)
    plt.plot(np.arange(0,ud_Out/100,steps/100),Comprar)
    plt.plot(np.arange(0,ud_Out/100,steps/100),noComprar)
    #plt.ylabel('y axis label')
    plt.legend(['Comprar', 'No Comprar'])

    plt.show()
