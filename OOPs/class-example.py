class Vehicle:  
    def __init__(self, name, max_speed):  
        self.name = name  
        self.max_speed = max_speed  

    def drive(self):  
        print(f"Driving the {self.name} at {self.max_speed} km/h.")  

# Object
my_vehicle = Vehicle("Bike", 120)  
my_vehicle.drive()