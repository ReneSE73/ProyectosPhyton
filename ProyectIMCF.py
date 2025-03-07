#Calculo del IMC
#Autor: René Soriano Estrada
#Matricula 010705999
#Universidad UTEL.

#Biernvenida
print("""
            Calculadora de indice de masa muscular
      
            Mediante el sistema métrico.

      Por favor brindanos los siguientes datos...
      """)

#Pedimos la información al usuario
nombre = input("Introduce tu nombre: ")
aPaterno = input("Introduce tu apellido paterno: ")
aMaterno = input("Introduce tu apellido materno: ")


print()
print(f"Mucho gusto \033[1m{nombre.upper()}\033[0m a continuación:")


edad  = int(input("Introduce tu edad: "))

#Pedimos vaores para el cálculo
pesoKilos = float(input("Introduce tu peso en kilos: "))    
estatura = float(input("Introduce tu estatura en metros: "))
        

#Se realiza el cálculo del IMC como los kilos dividido entre la estatura a cuadrado
imcResultado = pesoKilos / (estatura**2)

print("")
#Se imprime la información introducida del usuario
print("La información que se ingreso:")
print(f"Nombre completo: \t\t \033[1m{nombre.upper()} {aPaterno.upper()} {aMaterno.upper()}\033[0m") 
print("Nos indica una edad de: \t\033[1m" + str(edad) + " años \033[0m")

#Le indicamos si es mayor de edad
if (edad > 18):
    print ("\t\t\t\t\033[1mUsted es mayor de edad.\033[0m")
else :
    print ("\t\t\t\t\033[1musted es menor de edad\033[0m")

print("Reportando un peso de: \t\t\033[1m" + str(pesoKilos) + " Kg \033[0my una estatura de: \033[1m" + str(estatura)+ "\033[0m metros")

#Se imprime el resultao del IMC
print(f"Obtenemos su IMC:\t\t\033[1m{round(imcResultado,2)}" )

#Se clasifica de acuerdo al IMC
tipoClasificacion = ""

if imcResultado>0 and imcResultado <= 18.49 :
    tipoClasificacion = "Peso bajo"
    
elif imcResultado > 18.50 and imcResultado <= 24.99:
    tipoClasificacion = "Peso normal"
elif imcResultado > 25 and imcResultado <= 29.99:
    tipoClasificacion = "Sobrepeso"
elif imcResultado > 30 and imcResultado <= 34.99:
    tipoClasificacion = "Obesidad Leve"
elif imcResultado > 35 and imcResultado <= 39.99:
    tipoClasificacion = "Obesidad media"
elif imcResultado > 40:
    tipoClasificacion = "Obesidad morbida"
    

#Se imprie la clasificacion de el valor obtenido de IMC
print("\033[0mClasifica con: \033[1m \t\t" + tipoClasificacion)


