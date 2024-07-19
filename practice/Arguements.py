#Types of Arguements
# 1. Required arguements 2. Keyword arguements 3.Default Arguements 4.Variable Length arguements


#1.Required arguements == No.of aruements should be same in both function cal & function defn.
#order or the position should be same


#Example for required argue
def display(a,b):
    print(a,b)
display(a=10,b=20) #or display(10,20)

#2.Keyword arguements== initiatialization can be done based name of keywords
#order or position not required

#Example
def display(a,b):
    print(a,b)
display(b=50,a=90)

#3.Default arguements== no of arguements need not be same
#some of the arguements will be consider as default arguements

#Examole

def display(name,course="B.Tech"):
    print(name,course)
    #print(course)  u can also use this
display(name="Trinesh",course="M.Tech")
display(name="Ashiq")  #course ll be taken as default arguements


#4.Variable length arguement ==accepts arbitrary number of arguements
#this can be done by placing "*" as prefix  to the arguement of function defination

def display(*courses): #* means it ll accept variablev length arguements
    for i in courses:
        print(i)
display("B.Tech","M.Tech","Ph.D","MBA")


