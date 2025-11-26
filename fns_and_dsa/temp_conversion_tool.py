FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        value = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if scale == 'c':
        result = convert_to_fahrenheit(value)
        print(f"{value}°C is {result}°F")
    elif scale == 'f':
        result = convert_to_celsius(value)
        print(f"{value}°F is {result}°C")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
