
import numpy as np
import matplotlib.pyplot as plt
import Sistema_difuso as sd

if __name__ == "__main__":

    maxValue = 1
    steps = 1  # Pasos del Universo discurso

    # Establecer conjuntos difusos de la entrada (Precio)
    ud_P = 100 # Universo de discurso
    Barato = sd.Trapezoidal(0, 0, 30, 70, 1.0, ud_P, steps)
    Estandar = sd.Triangular(25, 60, 85, 1.0, ud_P, steps)
    Costoso = sd.Trapezoidal(55, 80, 100, 100, 1.0, ud_P, steps)

    # Establecer conjuntos difusos de la entrada (Kilometros
    ud_Km = 300 # Universo de discurso
    Bajo = sd.Trapezoidal(0, 0, 50, 200, 1.0, ud_Km, steps)
    Medio = sd.Trapezoidal(50, 100, 200, 300, 1.0, ud_Km, steps)
    Alto = sd.Triangular(200, 300, 300, 1.0, ud_Km, steps)

    # Establecer conjuntos difusos de la salida (%)
    ud_Out = 100 # Universo de discurso
    Comprar = sd.Trapezoidal(0, 0, 30, 80, 1.0, ud_Out, steps)
    noComprar = sd.Triangular(50, 100, 100, 1.0, ud_Out, steps)

    #Segunda Parte

    #Base de Reglas (Bajo, Medio, Alto)
    Reglas = [[Comprar,Comprar,noComprar],   # Barato
              [Comprar,noComprar,noComprar],  # Estandar
              [noComprar,noComprar,noComprar]] # Costoso
    Precios = [Barato,Estandar,Costoso] # i
    Kilometraje = [Bajo,Medio,Alto]     # j

    Valor = int(input('Elija un valor del Vehiculo : '))
    #Evalua en valor en el rango
    while not (Valor>=0 and Valor<ud_P):
        print('Elija un valor correcto ....')
        Valor = int(input('Elija un valor del Vehiculo : '))

    #Evalua en kilometraje en el rango
    Km = int(input('Elija un kilometraje del Vehiculo : '))
    while not (Km>=0 and Km<ud_Km):
        print('Elija un valor correcto ....')
        Km = int(input('Elija un kilometraje del Vehiculo : '))

    areaFinal = np.zeros(len(Reglas[0][0]))

    for i in range(len(Precios)):
        for j in range(len(Kilometraje)):
            #Obtiene Minimo Valor (And)
            mem = min([Precios[i][Valor],Kilometraje[j][Km]])
            function = np.ones(len(Reglas[i][j]))*mem
            print(Precios[i][Valor],' and ',Kilometraje[j][Km])
            #obtener funcion resultante
            result = []
            for idx,out in enumerate(Reglas[i][j]):
                result.append(min([function[idx],out]))
                areaFinal[idx] = max([min([function[idx],out]),areaFinal[idx]])


            plt.plot(np.arange(0,ud_Out/100,steps/100),Reglas[i][j])
            plt.plot(np.arange(0,ud_Out/100,steps/100),result,linestyle='--',color='r')
            plt.legend(['Conjunto difuso de Salida', 'Area resultante'])
            plt.show()

    plt.plot(np.arange(0,ud_Out/100,steps/100),areaFinal,linestyle='--',color='r')
    plt.legend(['Conjunto difuso de Salida', 'Area resultante'])
    plt.show()
