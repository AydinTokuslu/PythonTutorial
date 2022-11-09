class Pet():
    def __init__(self):
        self.name_ = "no name"
        self.type_ = "no type"
        self.age_ = 0
    def set_name(self, name): # java setter methodu
        self.name_ = name
    def set_type(self,type):  # java setter methodu
        self.type_ = type
    def set_age(self,age):  # java setter methodu
        self.age_ = age
    def get_name(self):  # java getter methodu
        return self.name_
    def get_type(self):  # java getter methodu
        return self.type_
    def get_age(self):  # java getter methodu
        return self.age_

    def __str__(self):  # string fonksiyonu, java tostring methodu
        return self.name_ + " is a " + str(self.age_) + " years old "+ self.type_

def main():
    animal = Pet()
    animal.set_name(input("Pet Name: "))
    while len(animal.get_name()) <= 0:
        print("You must write a proper name: ")
        animal.set_name(input("Pet Name: "))
    animal.set_type(input("Pet Type: "))
    while len(animal.get_type()) <= 0:
        print("You must write a proper type: ")
        animal.set_type(input("Pet Type: "))
    animal.set_age(input("Pet Age: "))
    while len(animal.get_age()) <= 0:
        print("You must write a proper age: ")
        animal.set_age(input("Pet Age: "))
    print()
    print("Pet Name: ", animal.get_name())
    print("Pet Type: ", animal.get_type())
    print("Pet Age: ", animal.get_age())
    print()

    print(animal)
    tatlı = Pet()
    print(tatlı)

main()