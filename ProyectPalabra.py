#Programa para identificar la longitud de una palabra
#que debe tener 8 caracteres



seguir = True
palabras= []


#Iniciamos el ciclo para ejecutar el programa, las veces que el usuario quiera hacerlo
while seguir == True:    

    #Se solicita la cadena al usuario
    cadena = input("Inytoduce tu palabra: ")
    
    #Declaramos una variable que tenga asignado el tamaño de la cadena
    numero = len(cadena)

    #Se valida que exista una palabra
    if numero == 0:
     print("No escribiste ninguna palabra")
     continue

    #Evaluamos si la cadena se encuentra en el rango de 4 a 8 caracteres y si cumple se imprime que es correcta
    if numero >= 4 and numero <= 8:
        print (f"La palabra {cadena} tiene {numero} caracteres y es correcta")

    #Si el numero de caracteres es menor a 4 se eviaque hace falta caracteres
    elif numero < 4:
        
        print(f"Hace falta letras. {cadena} Solo tiene {numero} letras")

    #Si el numero de caracteres es mayor a 8 se evalua que exede de caracteres y se envia el mensaje
    elif numero > 8:
        
        print (f"Sobran letras. {cadena} Tiene  {numero} letras")
        

    #Preguntsamos al usuario si desea continuar
    continuar = input("Desea intentar con otra palabra (Y/N)?: ")
    
    #Agregamos la palabra a na lista
    palabras.append(cadena)

    #En caso de que no se desee continuar se muestra las palabras ingresadas y se termina la ejecución
    if continuar == "N" or continuar == "n":
        print(f"Tus palabras fueron: {palabras}")
        break
    
    