# Encapsulation (Public, Private, Protected Attributes)

class ToyBox:
    def __init__(self):
        self.__toys = []  

    def add_toy(self, toy):
        self.__toys.append(toy)
        print(f'{toy} added to the toy box!')

    def show_toys(self):
        if self.__toys:
            print('Current toys in the box:', ', '.join(self.__toys))
        else:
            print("ToyBox is empty!")

    def __secret_function(self):
        print("Shh! This is a secret function!")

my_toy_box = ToyBox()

my_toy_box.add_toy('Teddy Bear')
my_toy_box.add_toy('Race Car')

my_toy_box.show_toys()

try:
    my_toy_box.__secret_function()
except AttributeError:
    print("Cannot access private method directly!")

my_toy_box._ToyBox__secret_function()