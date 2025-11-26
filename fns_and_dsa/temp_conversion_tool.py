def FAHRENHEIT_TO_CELSIUS_FACTOR(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9.0
def CELSIUS_TO_FAHRENHEIT_FACTOR(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9.0 / 5.0) + 32

def convert_temperature(value, scale):
    """Convert temperature between Celsius and Fahrenheit."""
    scale = scale.strip().lower()
    if scale in ("celsius", "c"):
        return FAHRENHEIT_TO_CELSIUS_FACTOR(value)
    elif scale in ("fahrenheit", "f"):
        return CELSIUS_TO_FAHRENHEIT_FACTOR(value)
    else:
        return "Error: Invalid temperature scale."
    
def main():
    print("Temperature Conversion Tool")
    value = float(input("Enter the temperature value to convert: "))
    scale = input("Enter the scale to convert to (Celsius or Fahrenheit): ")
    
    result = convert_temperature(value, scale)
    print(f"Converted temperature: {result}")
if __name__ == "__main__":
    main()