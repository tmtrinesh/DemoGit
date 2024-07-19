#1.System error or syntax error
#Ex: to print string in multiple we should use triple quotation but
# if we use double quotation it ll throw syntx or system error
a="""Welcome to
Python programming"""
print(a)
#2.Indentation error
for i in range(10):
    print(i)   #if we do not give space in the new line
    # after using for ll get this error(index block missin)

#3.Index error
#if list or tuple or string if we r accessing elements out of range
# then it ll show this error index out of range error
#4.Key error
d={"name":"Trinesh","rno":54,"perc":90}
#print(d["branch"]) #if we try to access the key which doent exist then it ll throw kwy error

#5.Name error
#if non existent identifier is used then name error ll be thrown
a,b,c=10,20,30
#print(e) #if u trying to print element which is not thr

#6.Type error
#type error raised when wrong type of parameter sent to a function
#Ex
a="welcome"
b=10
#print(a+b)#throw type error
#7.Value error
#Raised when parameter has invalid value
x="welcome"
#y=int(a) #throwrs value error
#8.Zero Division Error
#Raised when division is done by zero
#anything divide by zero..i.e denominator should not be zero
#9.Module not found error
#it ll throw error when try to import library which is not avaialable
#10Unbound local error
#raised when a reference is made to a local variable in a function or method,
# but no value has been bound to that variable
#def display():
#    m=m+1
#    print(m)

#m=100
#display()  #throw unbound local error

#11.Attribute Error
# raised if object accessing a member which is not available
class Demo:
    a,b=10,20
    def show(self):
        print("demo class")
obj=Demo()
print(obj.a,obj.b) # if we try to access one more variable which is not member of the class
obj.show() # then it ll throw attribute error
#12.File not found error
#Raised if the fine not available
#fo=open("python.txt","r")
#fo.read()
#fo.close()
#shows error no such file or directory 
