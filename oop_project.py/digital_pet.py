
import time

class DigitalPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        self.happiness += 5
        print(f" {self.name} is eating... Hunger: {self.hunger}, Happiness: {self.happiness}")

    def play(self):
        self.happiness += 10
        self.hunger += 5
        print(f" {self.name} is playing... Hunger: {self.hunger}, Happiness: {self.happiness}")


pet = DigitalPet("Tommy")

pet.feed()
time.sleep(1)
pet.play()