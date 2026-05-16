#Write a python function which converts inches to cms.

#inches = cms/2.54

def convert(n):
    if n==0:
        return 0
    return n*2.54

n = float(input("enter the value of n in inches: "))
print(f"value of {n} inches in centimeters is {convert(n)}cms")