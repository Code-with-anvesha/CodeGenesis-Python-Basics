# Dictionary creation
person = {"name": "Anvesha", "age": 20}

# Add key-value pair

person["city"] = "Jaunpur"

# Access value using key
print(person["name"])
# output Anvesha

# Loop through dictionary
  for key, value in
        person.items(): # type: ignore
       print(f"{key}: {value}")
