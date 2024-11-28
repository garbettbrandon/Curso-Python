def divide(a, b):
    try:
        z = a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    except TypeError:
        return "No se puede dividir por un string"
    else:
        return z
    finally:
        print("Siempre se ejecuta")


print(divide(10, "a"))


def division(x, y):
    assert y != 0, "y cannot be zero"

    print(x / y)


division(10, 2)
division(10, 0)

def division(x,y):
  assert y!=0, "y cannot be zero"
  
  print(x/y)
  
#call division() function in try block
try:
  division(10,0)
except AssertionError as msg:
  print(msg)