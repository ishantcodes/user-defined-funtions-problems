#Write a program using functions to find greatest of three numbers.

def great(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3
print("NUMBER SHOULDN'T BE SAME")    
n1 = int(input("enter the number: "))
n2 = int(input("enter the number: "))
n3 = int(input("enter the number: "))

print(f"the greatest number is {great(n1,n2,n3)}")
