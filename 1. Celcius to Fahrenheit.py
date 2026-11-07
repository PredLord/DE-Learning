# Write `celsius_to_fahrenheit(celsius)` that returns a float using F = (C × 9/5) + 32. Round the result to 1
# decimal place.
# SAMPLE INPUT / OUTPUT
# celsius_to_fahrenheit(0) -> 32.0
# celsius_to_fahrenheit(37) -> 98.6



def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return round(fahrenheit, 1)


print(celsius_to_fahrenheit(50))