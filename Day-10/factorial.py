# Function to calculate factorial
def factorial(n):
    result=1
    for i in range(1,n+1):
        result *= i
    return result

num=int(input("Enter a number to find the factorial: "))

print(f"Factorial of {num} is :",factorial(num))
