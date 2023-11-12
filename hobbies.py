#Crea un programa que pida por teclado (input) los datos de tus tres hobbies 
#favoritos y los mismos se guarden en un
#archivo que se llame miHobbieFavorito.txt.
#EXTRA: Hazlo con un for o un while para no repetir tanto…

hobbies = []

while len(hobbies) < 3:
    hobby = input("Escribe un hobby: ")
    hobbies.append(hobby)

print(hobbies)

f = open("miHobbieFavorito.txt", "w")

for i in hobbies:
    f.write(f" {i} -")
    
f.close
