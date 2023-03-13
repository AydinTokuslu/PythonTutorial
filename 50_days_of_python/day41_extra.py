# Create three classes of three car brands – Ford, BMW, and
# Tesla. The attributes of the car's objects will be, model,
# color, year, transmission, and whether the car is
# electric or not (Boolean value.) Consider using inheritance
# in your answer.
# You will create one object for each car brand:
# bmw1 : model: x6, Color: silver, Year: 2018, Transmission: Auto, Electric: False
# tesla1: model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True
# ford1 : model: focus, Color: white, Year: 2020, Transmission: Auto, Electric: False
# You will create a class method, called print_cars that will be
# able to print out objects of the class. For example, if you call the
# method on the ford1 object of the Ford class, your function
# should be able to print out car info in this exact format:
# car_model = focus
# Color = White
# Year = 2020
# Transmission = Auto
# Electric = False

class Cars:
    def __init__(self, model, color, year,
    transmission, electric=False):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
    # Creating the class method
    def print_car(self):
        return f'car_model = {self.model}\nColor = ' \
                f'{self.color} \nYear = {self.year}' \
                f' \nTransmission = {self.transmission} ' \
                f'\nElectric = {self.electric}'
class BMW(Cars):
    def __init__(self, model, color, year,
    transmission, electric=False):
        Cars.__init__(self, model, color, year,
        transmission, electric=electric)
class Tesla(Cars):
    def __init__(self, model, color, year,
    transmission, electric=False):
        Cars.__init__(self, model, color, year,
        transmission, electric=electric)
class Ford(Cars):
    def __init__(self, model, color, year,
    transmission, electric=False):
        Cars.__init__(self, model, color, year,
        transmission, electric=electric)
# instantiating class objects
ford1 = Ford("Focus", "White", 2017, "Auto", False)
print(ford1.print_car())
tesla1 = Tesla("S", "Grey", 2016, "Manual", True)
print(tesla1.print_car())
bmw1 = BMW('X6', 'silver', 2018, 'Auto', False)
print(bmw1.print_car())