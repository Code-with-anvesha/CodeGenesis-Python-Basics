distance = float(input("Enter the distance in km:"))

if distance < 3:
    transport = "Walk"
elif distance <= 15:
     transport = "Bike"
else:
     transport = "Car"

     print(f" Based on the distance of {distance} km, aashi recommends: {transport}")