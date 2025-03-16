order_size = input("Enter coffee size (small/medium/large):")
extra_shot = input("Do you want an extra shot? (yes/no):").strip().lower()

if extra_shot == "Yes":
     coffee = f"{order_size} coffee with an extra shot"
else:
        coffee = f"{order_size} coffee"
print("Your order:", coffee)