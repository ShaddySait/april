"""
    Program to convert Celsius to Fahrenheit
"""
def celsius_to_fahrenheit(celsius):
    """convert value given to fahrenheit"""
    fah= celsius *9/5+32
    return fah
def fahrenheit_to_clesius(fahrenheit):
    celsius= fahrenheit -32
    return celsius


celsius =25
fah= (celsius_to_fahrenheit(celsius))
print(f"{celsius} degress is {fah} Fahrenheit")

celsius= fahrenheit_to_clesius(fah)
print(f"{fah} degress Fahrenheit is {celsius} celsius")

