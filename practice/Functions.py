#main use of "function" is that in order to acieve reusability
#Easy debugging & reusability
#FUNCTION DEFINATION
# Every function should start wth DEF Keyword
#Every function should have a name (not equal to any keyword
#Parameters or arguements(optional) these should be included in between paranthesis
#Evry function name with or with out arguemnts should end with (:)
#Every function should have empty or value return
#Multi value return value can be done using tuples

#function name and arguements/parameters equal to function defination

#Function to add two numbers

def add(a,b):
    sum=a+b
    return sum
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
res=add(a,b)
print("Result = ",res)
