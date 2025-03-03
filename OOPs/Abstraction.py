from abc import ABC, abstractmethod

# Abstract Class
class Magician(ABC):
    @abstractmethod
    def perform_trick(self):
        pass  # This method will be implemented in subclasses

class CardMagician(Magician):
    def perform_trick(self):
        return "Abracadabra! I'm pulling a card from behind your ear!"

class DisappearingMagician(Magician):
    def perform_trick(self):
        return "Boom! I just disappeared! "

# Objects
harry = CardMagician()
houdini = DisappearingMagician()

print(harry.perform_trick())
print(houdini.perform_trick())