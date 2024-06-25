def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("Select conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    
    ch = input("Enter choice 1, 2, or 3: ")

    if ch == '1':
        temp = float(input("Enter the temperature in Celsius: "))
        print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    elif ch == '2':
        temp = float(input("Enter the temperature in Fahrenheit: "))
        print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    elif ch == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid input, please try again.")
