
file = open('anvesha_data.txt', 'w')

try:
    
    file.write('Anvesha Sharma ka custom data')
finally:

    file.close()


with open('anvesha_data.txt', 'w') as file:
    
    file.write('Anvesha Sharma ka custom data')

with open('anvesha_data.txt', 'a') as file:
    file.write('\nIn a world full of voices, she wonders if anyone truly listens.!')

print("Step 2: Data appended.")

# Read the file and display content
with open('anvesha_data.txt', 'r') as file:
    content = file.read()

print("Step 3: File read completed.")
print("\nFile Content:\n" + content)  
