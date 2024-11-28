# Define una clase vacía llamada FirstExercise.
class FirstExercise:
    pass


# Modifica la clase anterior. La clase debe recibir obligatoriamente las variables number y chapter.
class FirstExercise:
    def __init__(self, number, chapter):
        self.number = number
        self.chapter = chapter


# Instancia un objeto con los valores 6 y “Clases y objetos”.
obj = FirstExercise(6, "Clases y objetos")


# Añade un método que imprima por pantalla el número.
class FirstExercise:
    def __init__(self, number, chapter):
        self.number = number
        self.chapter = chapter

    def print_number(self):
        print(self.number)


obj = FirstExercise(6, "Clases y objetos")

obj.print_number()

# Crea una clase Circle que dado un radio permita consultar el área, el perímetro y permita modificar el radio.
class Circle:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio**2)

    def perimeter(self):
        return 2 * 3.14 * self.radio

    def set_radio(self, new_radio):
        self.radio = new_radio


# Cree una clase Vehicle que reciba el nombre, velocidad máxima y el kilometraje.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(
            f"Name: {self.name}, Max Speed: {self.max_speed}, Mileage: {self.mileage}"
        )


car = Vehicle("Mustang", 200, 5000)

car.print_vehicle()


# Cree una clase Bus que herede todos los métodos y variables de Vehicle.
class Bus(Vehicle):
    pass


# Cree un método a Vehicle que recibiendo la capacidad, imprima por pantalla “La capacidad de (nombre) es de (capacidad).
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(
            f"Name: {self.name}, Max Speed: {self.max_speed}, Mileage: {self.mileage}"
        )

    def print_capacity(self, capacity):
        print(f"La capacidad de {self.name} es de {capacity}")


car = Vehicle("Mustang", 200, 5000)

car.print_capacity(10)


# Cree el mismo método para Bus en el que por defecto la capacidad sea de 50.
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=50):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def print_capacity(self):
        print(f"La capacidad de {self.name} es de {self.capacity}")


bus = Bus("Mustard", 200, 5000)

bus.print_capacity()


# Defina la variable owner que tenga el valor “Nter” para todos los objetos de la clase.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.owner = "Nter"

    def print_vehicle(self):
        print(
            f"Name: {self.name}, Max Speed: {self.max_speed}, Mileage: {self.mileage}, Owner: {self.owner}"
        )


car = Vehicle("Mustang", 200, 5000)

car.print_vehicle()
