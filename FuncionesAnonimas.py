print("Ejercicio 1\n")
# Define una función lambda que calcule el cuadrado de un número.
cuadrado = lambda x: x * x
print(cuadrado(5))

print("\nEjercicio 2\n")
# Define una función lambda que devuelva True si el cuadrado de un número es mayor que 999 si no devuelve False.
es_cuadrado_grande = lambda x: x * x > 999
print(es_cuadrado_grande(5))

print("\nEjercicio 3\n")
#Define una función lambda que reciba dos números y devuelva el resultado de su multiplicación.
multiplicar = lambda x, y: x * y
print(multiplicar(5, 3))

print("\nEjercicio 4\n")
#Utilizando la función sorted() y lambda ordena una lista de palabras teniendo en cuenta la segunda letra de cada palabra.
words = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_words = sorted(words, key=lambda x: x[1])
print(sorted_words)

