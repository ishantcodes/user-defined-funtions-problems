#Write a python program using function to convert Celsius to Fahrenheit.

#°F = °C * 9/5 + 32
#C = (F − 32) * 5/9

def convert(f):
    c = (f-32)*5/9
    return c

f = float(input("Enter the temp in fahrenheit: "))

print(convert(f),"°C")
 