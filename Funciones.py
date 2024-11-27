print("-------------------Ejercicios con funciones-----------------------\n")

print("\nEjercicio funciones 1\n")


# Define una función llamada showAnimal que reciba dos argumentos name y n_legs e imprima esta información por pantalla.
def show_animal(name, n_legs):
    print(f"El animal se llama {name} y tiene {n_legs} patas.")


show_animal("Perro", 4)

print("\nEjercicio funciones 2\n")
# Define una función que puede recibir cualquier número de argumentos e imprima cuántos argumentos ha recibido.


def show_args(*args):
    print(f"Se han recibido {len(args)} argumentos.")


show_args(1, 2, 3, 4, 5)

print("\nEjercicio funciones 3\n")
#Define una función que recibiendo dos números, devuelva la suma y la resta de ellos en una sola llamada.

def sum_and_subtract(a, b):
    return a + b, a - b

result = sum_and_subtract(5, 3)
print(f"La suma es {result[0]} y la resta es {result[1]}")

print("\nEjercicio funciones 4\n")
#Define una función que recibiendo dos números devuelva la multiplicación.

def multiply(a, b):
    return a * b

result = multiply(5, 3)
print(f"El resultado de la multiplicación es {result}")

print("\nEjercicio funciones 5\n")
#Define una función que recibiendo dos números devuelva el módulo.

def modulo(a, b):
    return a % b

result = modulo(5, 3)
print(f"El resultado del módulo es {result}")

print("\nEjercicio funciones 6\n")
#Define una función que recibiendo una función del ejercicio 4 o ejercicio 5 y dos valores numéricos devuelva su resultado.

def apply_function(function, a, b):
    return function(a, b)

result = apply_function(multiply, 5, 3)
print(f"El resultado de la multiplicación es {result}")

print("\nEjercicio funciones 7\n")
#Define una función que reciba el nombre y email de una persona. Si no recibe email, se asignará “Sin determinar”. La función debe imprimir el nombre y email de la persona.

def show_person(name, email="Sin determinar"):
    print(f"El nombre es {name} y el email es {email}")

show_person("Pepe")

print("\nEjercicio funciones 8\n")
#Define una función que recibiendo un entero positivo, irá sumando este número a su anterior hasta llegar a 0 y devolverá el resultado final.

def sum_to_zero(n):
    if n <= 0:
        return 0
    return n + sum_to_zero(n - 1)

result = sum_to_zero(5)
print(f"El resultado de la suma es {result}")