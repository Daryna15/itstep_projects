class Student:
     def __init__(self, name, surname, age):
            self.name = name
            self.surname = surname
            self.age = age
     def get_info(self):
         print(self.name, self.surname, self.age)

student1= Student("Nastia", "Stetskiv", 14)
student1.get_info()


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(self.title, self.author, self.year)


book1 = Book("Harry Potter and Philosopher's Stone", "J.K.Rowling", 1997)
book1.get_info()
book2 = Book("The Kaidash Family", "Ivan Nechuy-Levytsky", 1878)
book2.get_info()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_info(self):
        area = 3.14159 * self.radius * self.radius
        print(area)
n = int(input("radius is"))
circle1 = Circle(n)
circle1.get_info()

