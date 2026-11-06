class Fuel:
    def __init__(self, hp):
        self.hp = hp

    def start(self):
        print(f"Fuel car with {self.hp} is riding")

class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        print("Electric car with", self.battery_capacity, "is charged")

class HybridCar(Fuel, ElectricCar):
    def __init__(self, hp, battery_capacity, brand):
        Fuel.__init__(self, hp)
        ElectricCar.__init__(self, battery_capacity)
        self.brand = brand

    def drive(self):
        print(f"Hybrid car {self.brand} with {self.battery_capacity} is driving ")

car = HybridCar(230, 100, "Honda")
car.drive()
car.charge()
car.start()


class Audioplayer:
    def __init__(self, volume):
        self.volume = volume

    def play_audio(self):
        print(f"audio playing volume = {self.volume}")

class Videoplayer:
    def __init__(self, lenght):
        self.lenght = lenght

    def play_video(self):
        print(f"video playing lenght = {self.lenght}")

class Multimediaplayer(Audioplayer, Videoplayer):
    def __init__(self, volume, lenght):
        Audioplayer.__init__(self, volume)
        Videoplayer.__init__(self, lenght)

    def play_Multimediaplayer(self):
        print(f"multimedia playing volume = {self.volume} lenght = {self.lenght}")


youtube_video = Multimediaplayer(36, 360)
youtube_video.play_audio()
youtube_video.play_video()







print(hasattr(youtube_video, "go"))
print(hasattr(youtube_video, "play"))

def show_info():
    print("Hello wourld")

print(callable(show_info))
print(callable(youtube_video))
print(callable(ElectricCar))


print(issubclass(Videoplayer, Multimediaplayer))
print(issubclass(Multimediaplayer, Videoplayer))

print(issubclass(Multimediaplayer, Fuel))