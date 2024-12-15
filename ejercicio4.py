#Loteria primitiva

lista_loteria = []

for i in range(6):
    numeros = int(input("Ingrese los números ganadores de la lotería primitiva separados por una coma: "))
    lista_loteria.append(numeros)
    lista_loteria.sort()
    print(lista_loteria)