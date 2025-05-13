import random
import matplotlib.pyplot as plt

# Simulación de la máquina de Galton
def canicas(num_canicas=3000, num_niveles=12):
    """ 
        Simula el paso de canicas a través de una máquina de Galton.
        Se definene 3000 canicas y 12 niveles.
        Cada canica tiene una probabilidad del 50% de ir a la izquierda o a la derecha en cada nivel.
        Al final, se cuenta cuántas canicas terminan en cada posición.
        Devuelve una lista con el número de canicas en cada posición final.
        num_canicas: Número de canicas a simular (default: 3000)
        num_niveles: Número de niveles en la máquina (default: 12)
        resultados: Lista con el número de canicas en cada posición final.
        
    """
    contenedor = [0] * (num_niveles + 1)  # Inicializa una lista para contar las posiciones finales
    
    # Simula el paso de cada canica a través de los niveles
    # Cada canica tiene una probabilidad del 50% de ir a la izquierda o a la derecha
    for _ in range(num_canicas):
        posicion = 0  # Posición inicial de la canica   
        for _ in range(num_niveles):
            
            # Simula una bifurcación: 0 = izquierda, 1 = derecha
            posicion += random.choice([0, 1])
        contenedor[posicion] += 1

    return contenedor

def histograma(resultados):
    """ 
        Crea un histograma de los resultados de la simulación.
        resultados: Lista con el número de canicas en cada posición final.
        Ejemplo de uso:
        resultados = canicas()
        histograma(resultados)
    """
    
    # Definimos los niveles de la máquina
    niveles = list(range(len(resultados)))

    #Obtenemos el total de canicas lanzadas
    canicas_totales = sum(resultados) 

    #Obtenemos el numero de niveles para mostrarlo en el titulo
    num_niveles = len(resultados) - 1

    plt.bar(niveles, resultados, color='orange', edgecolor='black')  
    plt.xlabel('Cantidad de canicas')
    plt.ylabel('Distribución de canicas')
    plt.title(f'Simulación de Máquina de Galton con ({canicas_totales} canicas en {num_niveles} niveles)')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Ejecutar simulación y mostrar resultados
if __name__ == "__main__":

    canicas_lanzar = input("¿Cuántas canicas quieres lanzar? ")
    num_niveles = input("¿Cuántos niveles quieres en la máquina? ")
    if canicas_lanzar.isdigit() and num_niveles.isdigit():

        # Llamar a la función canicas con los parámetros ingresados por el usuario
        canicas_lanzar = int(canicas_lanzar)
        num_niveles = int(num_niveles)
        conjunto = canicas(num_canicas=canicas_lanzar, num_niveles=num_niveles)

        # Mostrar los resultados
        print("Matriz de resultados: ", conjunto)

        # Llamar a la función histograma para mostrar el histograma de los resultados
        histograma(conjunto)

        # Mostrar el total de canicas lanzadas con los valores por defecto
    else:
        conjunto = canicas()
        histograma(conjunto)