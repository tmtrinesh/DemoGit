# Anonymous functions ara also called as Lambda functions
#These functions do not defined by "def" Keyword
# These functions returns expression not value
# these functions are One line functions and can take any number of arguements
# these functions cannot act as global Variables
# These functions can be defined by using "Lambda" Keyword
# these functions doesnt have  any name
#Syntax : lambda arguements:expression


sum = (lambda x,y:x+y)
print(sum(2,3))

a=int(input("Enter the value of a:"))  #print("sum=",sum(4,5) one liner program
b=int(input("Enter the value of b:"))
print("sum=",sum(a,b))