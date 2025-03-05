#Calculo del IMC
#Autor: René Soriano Estrada
#Matricula 010705999
#Universidad UTEL

print("""
Bienvenido ...
      El siguiente programa realiza el calculo de Indice de masa corporal (IMC)
      a partir de que se indique los kilos y la estatura


 """)

nombreNombre = input("¿Nombre del paciente?")
nombreApaterno = input("¿Apellido paterno?")
nombreAmaterno = input("¿Apellido materno?")

pesoKilos = float(input("Indiquenos el peso en kilos: "))
estatura = float(input("Indique la estatura e metros: "))

imcResultado = pesoKilos / (estatura**2)

print(f"{nombreNombre} {nombreApaterno} {nombreAmaterno}")
print(f"su indice de masa corporal es:{imcResultado}" )
