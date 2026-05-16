#Write a recursive function to calculate the sum of first n natural numbers.

def natural(n):
    if n==0:
        return 0
    return n + natural(n-1)

n = int(input("Enter the value of n: "))
print(f"sum of first {n} natural numbers is {natural(n)}")