print("\n --------------- Ejercicios con if \n")

print("\nEjercicio 1 \n")

a = 10
b = 100

# Defina una estructura de control que imprima por pantalla “Es igual a 10” si a es igual a 10 y si no imprima “Es diferente de 10”.
if a == 10:
    print("Es igual a 10")
else:
    print("Es diferente de 10")

print("\nEjercicio 2 \n")
# Defina una estructura de control que imprima “Todos son igual a 10” si a y b son iguales a 10; si no imprima “Solo a es igual a 10” si a es igual a 10; si no imprima “B es igual a 10” si b es igual a 10; si no imprima “Ninguno es igual a 10”.

if a == 10 and b == 10:
    print("Todos son igual a 10")
elif a == 10:
    print("Solo a es igual a 10")
elif b == 10:
    print("B es igual a 10")
else:
    print("Ninguno es igual a 10")

print("\nEjercicio 3 \n")
# Defina una estructura de control que imprima “A y B son impares” si tanto a como b son impares; si no imprima “A y B no son impares”.

if a % 2 != 0 and b % 2 != 0:
    print("A y B son impares")
else:
    print("A y B no son impares")


print("\n --------------- Ejercicios con While \n")

print("\nEjercicio 1 \n")
# Asigna un valor a la variable i.
i = 0

print("\nEjercicio 2 \n")
# Defina una estructura de control que solo imprima i una vez.
if i == 0:
    print(i)

print("\nEjercicio 3 \n")
# Defina una estructura de control que imprima i solo si el valor de i es par.
if i % 2 == 0:
    print(i)

print("\nEjercicio 4\n")
# Asigna i el valor 0. Crea una estructura de control que vaya incrementando i mientras i sea menor de 10. Comprueba si el valor de i es 6 e imprime “Ejecución terminada” y finaliza el bucle.
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 6:
        print("Ejecución terminada")
        break

print("\n --------------- Ejercicios con for \n")

a = ["Hello", "World"]
b = ["Python", 3.9]
c = "HelloWordPython"

print("\nEjercicio 1 \n")
# Recorre todos los caracteres de c e imprímelos por pantalla.
for i in c:
    print(i)

print("\nEjercicio 2 \n")
# Muestra todos los valores de a.
for i in a:
    print(i)

print("\nEjercicio 3 \n")
# Muestra cada valor de a y b mostrando cada elemento de a con el de la misma posición de b sin utilizar los índices de posición.
for i in range(len(a)):
    print(a[i], b[i])

print("\nEjercicio 4 \n")
# Muestra en cada iteración el valor y su índice para los elementos de b.
for i in range(len(b)):
    print(b[i], i)


print("\n --------------- Ejercicios con listas por comprensión. \n")


print("\nEjercicio 1 \n")
# Crea una lista con los números del uno al 10 elevados al cuadrado.
for i in range(1, 11):
    print(i**2)

print("\nEjercicio 2 \n")
# Crea una lista con los números pares del 1 al 20.
for i in range(2, 21, 2):
    print(i)

print("\nEjercicio 3 \n")
# Dada una lista de palabras crea una nueva lista con todas las palabras en mayúsculas
for i in a:
    print(i.upper())


print("\nEjercicio 4\n")
# Dada una lista de números crear una nueva lista en la que se dupliquen los números impares.
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in num_list:
    if i % 2 != 0:
        print(i * 2)


print("\nEjercicio 5\n")
# Dada una lista de palabras crea una lista con la segunda letra de cada palabra.
words = ["Hello", "World", "Python"]

for i in words:
    print(i[1])


print("\nEjercicio 6\n")
# Dada una lista de listas crea una lista con los elementos de todas las listas.
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in listas:
    for j in i:
        print(j)
