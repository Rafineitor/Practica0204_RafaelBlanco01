#Asignaturas y notas

lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
lista2 = []

for i in range(len(lista)):
    nota = input("Ingrese la nota de la asignatura: "+lista[i])
    lista2.append(nota)
    print ("En",lista[i],"has sacado",lista2[i])
    
