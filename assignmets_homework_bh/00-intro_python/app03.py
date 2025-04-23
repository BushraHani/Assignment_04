#03_fahrenheit_to_celsius

def main():
    print("Temperature in Fahrenheit! :)")
    fahrenheit = float (input("Enter the temperature in fahrenheit:"))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature: {fahrenheit}F = {celsius}C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
    
    