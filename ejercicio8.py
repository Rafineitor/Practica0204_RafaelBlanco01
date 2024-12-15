#Palindromo

palabra = input("Ingrese una palabra: ")
palabra1 = list(palabra)
palabra2 = list(palabra)
palabra2.reverse()

if palabra1 == palabra2:
    print("La palabra es un palindromo.")
else:
    print("La palabra no es un palindromo.")
