class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    #add a method
    def printinfo(self):
        print(self.make, self.model, self.year)

car = Vehicle('Nissan', 'Leaf', '2016')

#print(car.make, car.model, car.year)

car.printinfo()