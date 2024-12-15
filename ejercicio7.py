#Abecedario

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
abece =[]
for i in abc[0::3]:
    abece.append(i)
for i in abc[1::3]:
    abece.append(i)
abece.sort()
print(abece)
    