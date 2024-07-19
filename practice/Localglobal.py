 #Scope of local variable is that we can use with in rhe function where variables habe been declared
#Scope of globa variables is that in the entire program
#every user defined function to start with def keyword

#VVV IMP
#if local variable and global variable both n have same name then local variable ll be printed
#small program for global variables
a=20     #global var
def display():
    b=100  #local var
    print("inside the user defined function",a)
    print("local varible",b)
display()
print("outside the user defined function",a)

############################################################################################
#exMPLE
a=10
def display():
    print("global a",a)
    b=52
    print("local variable",b)
display()
c=40
print("local variable",c)
print("global varuiable",a)
