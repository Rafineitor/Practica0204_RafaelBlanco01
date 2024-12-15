#Asignaturas reprobadas

asig = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
lista_nota = []
lista_rep = []
for i in asig:
    print("Introduce la nota sacada en:",i)
    nota = int(input(""))
    lista_nota.append(nota)
for i in range(len(lista_nota)):
    if lista_nota[i]<5:
        lista_rep.append(asig[i])
print("Las asignaturas reprobadas son:",lista_rep)