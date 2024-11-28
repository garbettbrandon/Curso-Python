print("Ejercicios ficheros\n")

line1 = "Es mi primera línea."

line2 = "Es mi segunda línea."

line3 = "Es mi tercera línea."

line4 = "¡Es el final del fichero!"

# Crea un fichero vacío llamado primerfichero.txt sin usar with.
fichero = open("primerfichero.txt", "w")

# Crea un segundo fichero vacío llamado segundofichero.txt usando with.
with open("segundofichero.txt", "w") as f:
    pass
print("Ficheros creados correctamente.")

# Escribe line1 en primerfichero.txt.
fichero.write(line1)

# Escribe line2, line3 y line4 en segundofichero.txt cada uno en una línea.
with open("segundofichero.txt", "w") as f:
    f.write(line2 + "\n")
    f.write(line3 + "\n")
    f.write(line4)

print("Ficheros escritos correctamente.")

# Lee primerfichero.txt y añade su contenido al final de segundofichero.txt.
with open("segundofichero.txt", "a") as f:
    with open("primerfichero.txt", "r") as f2:
        f.write(f2.read())

print("Ficheros concatenados correctamente.")
