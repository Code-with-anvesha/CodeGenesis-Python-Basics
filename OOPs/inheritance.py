class Ghost:
    def __init__(self, name):
        self.name = name
    
    def scare(self):
        return f"{self.name} says: BOOOO!"

class FriendlyGhost(Ghost):
    def scare(self):
        return f"{self.name} says: Wanna be my friend? "

class EvilGhost(Ghost):
    def scare(self):
        return f"{self.name} whispers: I'm right behind you... "

#  Ghost Objects
casper = FriendlyGhost("Casper")
bloody_mary = EvilGhost("Bloody Mary")

print(casper.scare())
print(bloody_mary.scare())