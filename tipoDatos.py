from datetime import datetime, time


print("Hello World")

#Define un número de tipo int.
x = 1

#Define un número de tipo float.
y = 1.0

#Define un número de tipo complex.
z = 1 + 2j
print(z)  

#Muestra por pantalla la parte real del número definido en el punto 3.
print("Valor real: ", z.real)

#Muestra por pantalla la parte imaginaria del número definido en el punto 3.
print("Valor imaginario: ", z.imag)

#Define una variable con valor True.
a = True

#Define una variable con valor False.
b = False

#Define una variable con valor True mediante un entero.
c = 1

print(a, b, c)

#Define una variable con un string con el valor “ Master Python”.
d = " Master Python"

#Muestra la longitud de la variable anterior.
print("Longitud de la variable d: ", len(d))

#Muestra el primer carácter del string.
print("El primer caracter es: ", d[0])

#Muestra el penúltimo carácter del string.
print("El penultimo caracter es: ", d[-2])

#Elimina los espacios iniciales del string.
print(d.lstrip())

#Muestra los caracteres en posiciones impares.
print("Caracteres en posiciones impares: ", d[1::2])

#Convierte todo el string en minúscula.
print("todo el string en minúscula: ", d.lower())

#Separa el string por espacios en blanco.
print("El string sepadado por espacios en blanco: ", d.split(" "))

#Reemplaza “python” por “JAVA”.
print("Remplazando Python por JAVA: ", d.replace("Python", "JAVA"))

print("\nEjercicios con listas \n")   

#Define una lista con los valores 10,20,'Hello',20.5
e = [10,20,'Hello',20.5]

#Añade “Word” al final de la lista.
e.append("Word")

#Añade “Python” al principio de la lista.
e.insert(0, "Python")

#Elimina el segundo valor de la lista.
e.pop(1)

#Crea una segunda lista con los valores 20, 40, ‘Bye’ (utiliza una forma diferente que en el inicio).   
#crea esa lista con list().
f = list([20, 40, 'Bye'])

#Une las dos listas.
e.extend(f)

#Muestra la lista final.
print("Lista final: ", e)

print("\nEjercicios con conjuntos \n")   

#Define un conjunto con los valores coche, motocicleta, bicicleta.
g = {"coche", "motocicleta", "bicicleta"}

#Añade avión al conjunto.
g.add("avión")

#Elimina coche del conjunto.   
g.remove("coche")

#Crea otro conjunto con los valores avión, coche, tractor (utiliza una forma diferente que en el punto 1).
h = set(["avión", "coche", "tractor"])

#Crea otro conjunto con los valores que se repitan en los conjuntos anteriores.
i = g.intersection(h)

#Muestra un conjunto con todos los valores que pertenecen al conjunto creado en el punto 1 y punto 4.
print("Conjunto con todos los valores que pertenecen al conjunto creado en el punto 1 y punto 4: ",g.union(i))

print("\nEjercicios con Diccionarios \n")   

#Para realizar este ejercicio tienes un diccionario con las claves: coche, motocicleta, camión y los valores: 10, 20 y 30 respectivamente.
j = {"coche": 10, "motocicleta": 20, "camión": 30}

#Define el diccionario usando dict().
k = dict({"coche": 10, "motocicleta": 20, "camión": 30})

#Muestra los valores del diccionario.
print("Valores del Diccionario: ",k.values())

#Muestra las claves del diccionario.
print("Claves del Diccionario: ",k.keys())

#Muestra el valor de coche.
print("El valor de coche es: ",k["coche"])

#Añade al diccionario avión con valor 100.
k["aviónaso"] = 100

#Muestra los elementos del diccionario.
print("Elementos del diccionario: ",k)

print("\nEjercicios con tuplas \n")    

#Para realizar este ejercicio crea una tupla con los siguientes valores: coche, motocicleta y camion.
l = ("coche", "motocicleta", "camion")

#Accede al primer y último elemento de la tupla e imprime sus valores.
print("El primer elemento es: ", l[0])

# Crea otra tupla de forma distinta a la del inicio con los valores: perro, gato y naranja.
m = tuple(["perro", "gato", "naranja"])

#Concatena las dos tuplas en una nueva con el nombre ‘tupla_concatenada’.
tupla_concatenada = l + m

#Cuenta el número de elementos de la tupla.
print("El numero de elementos de la tupla es: ", len(tupla_concatenada))

#Encuentra el índice del elemento perro dentro de ‘tupla_concatenada’.
print("El indice del elemento perro es: ", tupla_concatenada.index("perro"))

#Desempaqueta ‘tupla_concatenada’ en las variables (por este orden) tp1, tp2, tp3 y el resto en tp4.
tp1, tp2, tp3, *tp4 = tupla_concatenada

#Imprime los valores de las variables.
print(tp1, tp2, tp3, tp4)

#Añade un nuevo elemento a ‘tupla_concatenada’.
tupla_concatenada = tupla_concatenada + ("perro",)

#Muestra los elementos de ‘tupla_concatenada’.
print(tupla_concatenada)    

print("\nEjercicios con fechas \n")

# Para realizar estos ejercicios parte de dos listas, una con fechas representadas como cadenas en formato YYYY-MM-DD y otra con horas con cadenas en formato HH:MM:SS.

fechas = ['2024-09-09', '2023-08-15', '2022-07-01']
horas = ['14:30:00', '09:15:00', '23:59:59']

#Convierte cada cadena de la lista fechas a un objeto date.
fechas = [datetime.strptime(fecha, "%Y-%m-%d").date()  for fecha in fechas]

#Convierte cada cadena de la lista horas a un objeto time.
horas = [datetime.strptime(hora, "%H:%M:%S").time()  for hora in horas]

#Combina cada elemento de los objetos date y los objetos time de los dos ejercicios anteriores para crear una lista de objetos datetime.
fechas_y_horas = [datetime.combine(fecha, hora) for fecha, hora in zip(fechas, horas)]

for fecha_hora in fechas_y_horas:
    print(fecha_hora)

#Calcula los días de diferencia que hay entre los objetos date resultantes del ejercicio 1 y la fecha actual.
fecha_actual = datetime.now()
diferencia_en_dias = [fecha_actual.date() - fecha for fecha in fechas]

print("Días de diferencia: ", diferencia_en_dias)

#Sacando cada resultado en una linea distinta.
for diferencia in diferencia_en_dias:
    print(diferencia.days)

#Elige una fecha de los objetos date resultantes del ejercicio 1 y cambiar su año a 2025.
fecha_a_cambiar = fechas[0]
fecha_a_cambiar = fecha_a_cambiar.replace(year=2025)
print(fecha_a_cambiar)

#Convierte cada objeto datetime resultante del ejercicio 3 en una cadena con el formato DD/MM/YYYY HH:MM.
fechas_y_horas = [fecha_hora.strftime("%d/%m/%Y %H:%M") for fecha_hora in fechas_y_horas]
print(fechas_y_horas)