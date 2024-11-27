#Define tres variables llamadas a, b y c con los valores 50, 5.0, 100.  
a = 50
b = 5.0
c = 100

#Define la variable d siendo la suma de a y b.
d = a + b

#Define la variable e siendo la resta de c y d.
e = c - d

#Define la variable f con el resultado de la multiplicación d y e.
f = d * e

#Define la variable g con el resultado de la división f y a.
g = f / a

#Define la variable h con el módulo de f y a.
h = f % a

#Define las variables a y b con los valores 50 y 10
a = 50
b = 10

#Comprueba si a y b son iguales.
if a == b:
    print("a y b son iguales")
else: 
    print("a y b no son iguales")

#ahora lo mismo pero sin if else.

#Comprueba si a y b son distintos.
if a != b:
    print("a y b son distintos")
else: 
    print("a y b no son distintos") 

#Comprueba si a es mayor que b.
if a > b:
    print("a es mayor que b")    
else:
    print("a no es mayor que b")    

#Comprueba si a es menor o igual que b.
if a <= b:
    print("a es menor o igual que b")    
else:
    print("a no es menor o igual que b")    


#Define una variable y asígnale el valor 999.
y = 999

#Suma 1 a la variable anterior.
y = y + 1

#Resta 10 a la variable anterior.
y = y - 10

#Multiplica por 10.
y = y * 10

#Divide entre 5.
y = y / 5

#Asigna a la variable inicial el resultado del módulo de 60.
y = y % 60

#Imprime el valor de la variable y.
print(y)

#Crea las variables a, b, c y d con los valores 10, 100, 200 y 300 respectivamente.
a = 10
b = 100
c = 200
d = 300

#Comprueba si a es mayor que b y c es menor que d.
if a > b and c < d:
    print("a es mayor que b y c es menor que d")
else:
    print("a no es mayor que b o c no es menor que d")  

#Comprueba si la suma de a y b es mayor o igual que c o la suma de b y c es mayor o igual que d.
if (a + b) >= c or (b + c) >= d:
    print("la suma de a y b es mayor o igual que c o la suma de b y c es mayor o igual que d")
else: 
    print("la suma de a y b no es mayor o igual que c y la suma de b y c no es mayor o igual que d")


#Para realizar los siguientes ejercicios, debemos de crear las siguientes variables:

list1 = [1,2,3,4,5]

list2 = ['Hello','Word','Python']

list3 = ['Operator','Membership', 100,200]

#Comprueba si 5 está en list1.
if 5 in list1:
    print("5 esta en list1")
else:
    print("5 no esta en list1")

#Comprueba si “Hello” y “Python” están en list2.
if "Hello" in list2 and "Python" in list2:
    print("Hello y Python estan en list2")
else:
    print("Hello y Python no estan en list2")

#Comprueba si list2 es igual que list3.
if list2 == list3:
    print("list2 es igual que list3")    
else:        
    print("list2 no es igual que list3")

#Recuerda que estos tipos de operadores utiliza números binarios internamente. Los siguientes ejercicios consisten en utilizar los operadores indicados con las variables siguientes:
#Operador AND
#Operador XOR
#Operador left shit

a = 1  # En binario: 0001
b = 2  # En binario: 0010

# 1. Operador AND (&)
# Realiza un AND bit a bit, devuelve 1 solo si ambos bits son 1
resultado_and = a & b
print("Resultado AND:", resultado_and)
# 0 (porque no hay bits 1 en la misma posición)

# 2. Operador XOR (^)
# Devuelve 1 si los bits son diferentes
resultado_xor = a ^ b
print("Resultado XOR:", resultado_xor)
# 3 (porque los bits son diferentes)

# 3. Operador Left Shift (<<)
# Desplaza los bits hacia la izquierda
resultado_left_shift_a = a << 1
resultado_left_shift_b = b << 1
print("Left Shift de a:", resultado_left_shift_a)
# 2 (0001 se desplaza a 0010)
print("Left Shift de b:", resultado_left_shift_b)
# 4 (0010 se desplaza a 0100)

a = 3
b = 3.0
#Comprueba si a es un int
if isinstance(a, int):
    print("a es un int")        
else:
    print("a no es un int") 
#Comprueba si b es un boolean.
if isinstance(b, bool):
    print("b es un boolean")
else:
    print("b no es un boolean")
#Comprueba si b es un float.
if isinstance(b, float):
    print("b es un float")
else:
    print("b no es un float")
