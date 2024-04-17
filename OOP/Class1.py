class Dog:
     def __init__ (self):
          self.name= "lassie"
     def bark(self,name):
          print(f"woof, my name is {name}")
          
          
dog = Dog()
print(dog.name)
dog.bark("perro")