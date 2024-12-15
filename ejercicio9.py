#Vocales en palabra

vocal = ["a","e","i","o","u"]
palabra = input("Ingrese una palabra: ")
palabra1 = list(palabra)
for i in vocal:
    if i in palabra1:
        cuenta = palabra1.count(i)
        print(i,"aparece en",cuenta,"ocasion(es)")