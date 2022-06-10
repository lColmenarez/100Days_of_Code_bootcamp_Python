from numpy import multiply


def add(*args):
    #print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

    
#print(add(3, 4, 5, 4, 6, 7, 9))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=5)

class Car():
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        
my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)