#Write a python function to print multiplication table of a given number.

def table(n):
    x=1
    for i in range(1,11):
        print(n*x)
        x+=1
        
    
n = int(input("enter the value of n: "))
table(n)