
from animal import Animal


class Cat(Animal):
    def add_trick(self, trick):
        return super().tricks.append(trick)
    
    def print_trick(self):
        print("calling it from Cat")

cat=Cat()


dog=Animal()
cat.add_trick("meow")
cat.add_trick("climb")

dog.add_trick("jump")
dog.add_trick("growl")

print(*(dog.tricks),sep="\n")

print(cat.__class__)
print(dog.__class__)

dog.print_trick()
print(cat._pri_var)