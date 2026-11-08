class Animal:
    def __init__(self, color, age, name):
        self.color = color
        self.age = age
        self.name = name

class Dog(Animal):
    def __init__(self, color, age, name):
        super().__init__(self, color, age, name)

    def show_info(self):
        print(f"color - {self.color}, age - {self.age}, name - {self.name}")


class Cat(Animal):
    def __init__(self, color, age, name):
        super().__init__(self, color, age, name)

    def show_info(self):
        print(f"color - {self.color}, age - {self.age}, name - {self.name}")




Lily = Cat("grey", 1, "lily")
Lily.show_info()

Tysik = Dog("blonde", 5, "Tysik")
Tysik.show_info()