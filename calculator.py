# Simple Calculator

print("🧮 Welcome to Calculator\n")

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ").strip()

if choice == "1":
    print(f"Result: {a + b}")

elif choice == "2":
    print(f"Result: {a - b}")

elif choice == "3":
    print(f"Result: {a * b}")

elif choice == "4":
    if b == 0:
        print("❌ Cannot divide by zero")
    else:
        print(f"Result: {a / b}")

else:
    print("❌ Invalid choice")

print("\n✅ Done")



