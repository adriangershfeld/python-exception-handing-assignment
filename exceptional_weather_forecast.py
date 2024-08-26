# Task 1: Start
# Begin by asking the user to enter the temperature in Fahrenheit.
# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius. 
# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format. 
# Task 4: Finally
# Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

def fahrenheit_to_celsius(fahrenheit):
    return (float(fahrenheit) - 32) * 5 / 9

try:
    user_fahrenheit = input("Enter the Fahrenheit temperature you want convered to Celsius: ")
    fahrenheit_temperature = float(user_fahrenheit)
    celsius_temperature = fahrenheit_to_celsius(user_fahrenheit)
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print(f"{fahrenheit_temperature}° Fahrenheit is {celsius_temperature:.2f}° Celsius.")
finally:
    print("Thank you for using the weather forecast application!")