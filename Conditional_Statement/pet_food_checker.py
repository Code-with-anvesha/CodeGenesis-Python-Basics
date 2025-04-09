pet_type = input("Enter your pet name : ").strip().lower()
age = int(input("Enter your pet's age (in years): "))

# Pet food recommendation logic
if pet_type == "dog 🐶":
    if age < 2:
        food = "Puppy Food"
    else:
        food = "Adult Dog Food"
elif pet_type == "cat":
    if age <= 2:
        food = "Kitten Food"
    elif age <= 5:
        food = "Adult Cat Food"
    else:
        food = "Senior Cat Food"
else:
    food = "Unknown pet type! Please enter Dog or Cat."

# Final output
print("Recommended Food:", food)