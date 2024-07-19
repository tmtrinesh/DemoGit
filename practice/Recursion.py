#Recursion  function ..A function calling itself is called recursion
# Base case..Aft finite number of steps every recursion should be terminated
# Recursive case..we r keep on calling the function itself
# Best example  for recursion is Factorial
def Factorial(n):
    if (n == 0 or n==1):
        return 1
    else:
        return n*Factorial(n-1)
n=int(input("Enter value of n:"))
result=Factorial(n)
print("Factorial of n is",result)


