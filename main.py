class Human:
    def __init__(self, name = "Daryna"):
        self.name = name

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def get_info(self):
        if self.passengers != []:
            print(f"car brand - {self.brand}")
            for human in self.passengers:
                print(human.name)
        else:
            print("No passengers")

class Shape:
    def __init__(self, color, area):
        self.color = color
        self.area = area

class Circle(Shape):
    def __init__(self, color, area, radius):
        super().__init__(color, area)
        self.radius = radius

        def show_info(self):
            print(f"Name - {self.name}, area - {self.area}, radius - {self.radius}")

class Rectangle(Shape):
    def __init__(self, color, area, width, height):
        super().__init__(color, area)
        self.width = width
        self.height = height

        def show_info(self):
            print(f"Name - {self.name}, area - {self.area}, width - {self.width}, height - {self.height}")

circle = Circle("circle", 20, 10)


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_info(self):
        print(f"Name - {self.name}, Health - {self.health}")

class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name,health)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} attacks enemy with weapon {self.weapon}")

    def show_info(self):
        print(f"Name - {self.name}, Health - {self.health}, Weapon - {self.weapon}")

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    def attack(self):
        print(f"{self.name} hits with {self.damage}")

        def show_info(self):
            print(f"Name - {self.name}, Health - {self.health}, Weapon - {self.weapon}")

spider = Hero("spider", 100, 20)
spider.show_info()
spider.attack()

venom = Enemy("venom", 80, 30)
venom.show_info()
venom.attack()

hero1 = Hero(name = "Hero1", health = 100, weapon = 2)
hero1.show_info()


Olexandr = Human(name = "Olexandr")
Anna = Human(name = "Anna")
Vladyslav = Human(name = "Vladyslav")

toyota = Car(brand = "Toyota")
toyota.add_passenger(Olexandr)
toyota.add_passenger(Anna)
toyota.add_passenger(Vladyslav)
toyota.get_info()