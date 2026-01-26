# oop inheritance


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am '{self.name}' and I am '{self.age}' years old")

    def speak(self):
        print("I dont't speak")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(
            f"I am '{self.name}' and I am '{self.age}' years old and I am '{self.color}'"
        )


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Tim", 12)
p.speak()  # I dont't speak

c = Cat("Nelly", 14, "red")
c.show()  # Meow

d = Dog("Lucifer", 18)
d.speak()  # Bark

f = Fish("bubble", 10)
f.speak()  # I dont't speak
