# 14 Method Overriding

# Method overriding means replacing/extending a method defined in the base class.
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1
    
    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        super().__init__() # If we don't add the super function the constructor in the Animal class will not be executed because it will be replace by the contructor 
        # With the super() we can acess any method on the animal class
        print('Mammal Constructor') #If you want to call this constructor first you have put super().__init__() on the last line of this function.

    def walk(self):
        print("walk")

m = Mammal()
print(m.age)
print(m.weight)
