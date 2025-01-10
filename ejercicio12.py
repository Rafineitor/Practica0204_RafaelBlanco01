#Media y desviacion tipica.

numeros = input("Introduce varios números separados por comas: ")
numeros2 = numeros.split(",")
numeros3 = [int(i) for i in numeros2]

media = sum(numeros3)/len(numeros3) #media

desviacion = (sum((i - media)**2 for i in numeros3)/len(numeros3))**0.5

print("La media de los numeros es:",media)
print ("La desviacion tipica de los numeros es:",desviacion)



