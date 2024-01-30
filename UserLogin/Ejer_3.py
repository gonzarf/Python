file = open("nuevo.txt", "w")
file.write("Me he creado!")
file.close()

file = open("nuevo.txt", "r")
print(file.read())
