
#define the car class
class Car:
    #define the init methods
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
#define the minivan class
class Minivan(Car):
    #define the init methods
    def __init__(self,brand,model,year, hasASD):
        super().__init__(brand,model,year)
        self.hasASD = hasASD

#create an object of the Car class
car = Car("Chevrolet","Malibu",2017)
#print all the attributes
print("Car Class")
print("Brand: ",car.brand)
print("Model: ",car.model)
print("Year: ",car.year)

#create an object of the Minivan class
minivan = Minivan("Honda","Odyssey",2024,True)
#print the attributes
print("Minivan Class")
print("Brand: ", minivan.brand)
print("Model: ", minivan.model)
print("Year: ", minivan.year)
print("hasASD: ", minivan.hasASD)
