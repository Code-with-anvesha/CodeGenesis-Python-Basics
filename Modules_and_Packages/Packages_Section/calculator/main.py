from packages.calculator import add, subtract, multiply, divide

def main():
    print(" Simple Calculator (Student-Friendly)")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = int(input("Konsa operation karna hai? (1/2/3/4): "))
    
    num1 = float(input("Pehla number: "))
    num2 = float(input("Dusra number: "))

    if choice == 1:
        print(f"Result: {add(num1, num2)}")
    elif choice == 2:
        print(f"Result: {subtract(num1, num2)}")
    elif choice == 3:
        print(f"Result: {multiply(num1, num2)}")
    elif choice == 4:
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")

if _name_ == "_main_":
    main()
