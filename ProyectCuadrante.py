
#Programa que identifica el cuadrante de una coordenada

#Se deifine una variable booleans para decidir si se cierra el ciclo o se termina la ejecucion
seguir = True

#Se declara un diccionario para definir que tipos de cuadrantes se tienen
cuadrantes = {
    1: "Cuadrante I",
    2: "Cuadrante II",
    3: "Cuadrante III",
    4: "Cuadrante IV"
}

while seguir == True:

    print("Programa para identificar el cuadrante por coordenadas")
    
    #Declaramos una lista vacia para agregar los valores de x , y
    puntos = []

    #Se define cuantas coordenadas desea capturar el usuario
    num_coordenadas = int(input("\n¿Cuantas coordenadas desea ingresar? "))

    print("\nIngrese las coordenadas del punto (x, y), considrando que ninguna puede ser 0")
    
   
    #Se evalua que la informacion que se ingrese sean numeros
    try:
            for i in range(num_coordenadas):
                #Se obtine los valores de x , y para cada coodenada
                print(f"\nIngrese los valores x, y para la coordenada {i + 1}")
                x = float(input("Ingrese el valor de x: "))
                y = float(input("Ingrese el valor de y: "))
            
                #Se evalua que el valor ingresado no sea 0 en x o y
                if x == 0 or y == 0:
                    print("\nError: Ninguna coordenada puede ser 0. Intente nuevamente.")
                    continue

                #Se define a que cuadrante pertenece los valores ingresados
                if x > 0 and y > 0:
                    cuadrante = 1
                elif x < 0 and y > 0:
                    cuadrante = 2
                elif x < 0 and y < 0:
                    cuadrante = 3
                elif x > 0 and y < 0:
                    cuadrante = 4
    
                #Se agrega los valores x, y y al cuadrante que pertence en la lista
                puntos.append((x,y,cuadrantes[cuadrante]))
    
    except ValueError:
            print("\nError: Por favor ingrese valores numéricos válidos.")
            continue
    a = 1
    #Se imprime los resultados obtenidos de todas las coordenadas capturadas
    for i in puntos:
         print (f"El cuadrante de la coordenada {a} es: {i}")
         a+=1
 
    #Se pregunta al usuario si desea genear otro bloque de coordenadas
    continuar = input("\nDesea ingresar otras coordenadas (Y/N)?: ")

    if continuar == "N" or continuar == "n":
        puntos.clear()
        break