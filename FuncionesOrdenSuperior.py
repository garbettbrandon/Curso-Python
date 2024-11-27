from functools import reduce


print("Ejercicio 1\n")
#Define una función que devuelva una lista con el doble de todos los elementos de la lista inicial.
def doble_lista(lista):
    return [x * 2 for x in lista]

print(doble_lista([1, 2, 3, 4, 5]))

print("\nEjercicio 2\n")
#Define una función que eleve al cuadrado los elementos que sean pares.
def cuadrado_pares(lista):
    return [x * x for x in lista if x % 2 == 0]

print(cuadrado_pares([1, 2, 3, 4, 5]))  

print("\nEjercicio 3\n")
#Define una función que dada dos listas sume los elementos de la misma posición.
def sumar_listas(lista1, lista2):
    return [x + y for x, y in zip(lista1, lista2)]

print(sumar_listas([1, 2, 3], [4, 5, 6]))  

print("\nEjercicio 4\n")
#Define una función que dado una lista de strings devuelva una lista con el número de ‘a’ que aparece en cada string.
def contar_a(lista):
    return [len(list(filter(lambda x: x == 'a', x))) for x in lista]

def contar_a_alt(lista):
    resultado = []
    for palabra in lista:
        # Cuenta cuántas "a" hay en cada palabra
        conteo = palabra.count('a')
        resultado.append(conteo)
    return resultado

print(contar_a(["apple", "banana", "cherry", "date", "elderberry"]))
print(contar_a_alt(["apple", "banana", "cherry", "date", "elderberry"]))

print("\nEjercicio 5\n")
#Define una función que dado una lista sólo devuelva los elementos que son negativos.
def elementos_negativos(lista):
    return [x for x in lista if x < 0]

print(elementos_negativos([-1, 2, -3, 4, -5]))

print("\nEjercicio 6\n")
#Define una función que dado un string devuelva la lista de vocales que aparecen.
def vocales(string):
    return [x for x in string if x in 'aeiouAEIOU']

print(vocales("Hello World"))

print("\nEjercicio 7\n")
#Define una función que dado una lista devuelva la multiplicación de todos los elementos.
def multiplicar_lista(lista):
    return reduce(lambda x, y: x * y, lista)    

print(multiplicar_lista([1, 2, 3, 4, 5]))

print("\nEjercicio 8\n")
#Dado un string extraer los números que aparecen en el texto y devolver su suma.
def sumar_numeros(string):
    return reduce(lambda x, y: x + y, [int(x) for x in string if x.isdigit()])

print(sumar_numeros("Hello 123 World 456"))

