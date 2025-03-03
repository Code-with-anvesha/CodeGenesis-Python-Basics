class Parrot:
    def speak(self):
        return "Squawk! I am  a parrot!"

class Robot:
    def speak(self):
        return "Beep Bop! I am a robot!"

class Dog:
    def speak(self):
        return "Bhow Bhow! I am a dog!"

# Polymorphism in Action!
def make_them_speak(creature):
    print(creature.speak())

# Objects
mitthu = Parrot()
jarvis = Robot()
tommy = Dog()

make_them_speak(mitthu)
make_them_speak(jarvis)
make_them_speak(tommy)