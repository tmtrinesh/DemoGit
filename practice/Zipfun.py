a=[10,20,30]
b=[40,50,60,80]
y=zip(a,b)
#print(type(y))  # to know the class
output=list(y)
print(output)

subjects=["English","Maths","Science","Social"]
marks=[90,100,95,98]
m=zip(subjects,marks)
#result=list(m)
result= dict(m)
#result=tuple(m)
print(result)

# in zip fun 2 iterables joined to form a tuple by considering minimum length of both iterables
#if any iterable having more element ll  not be printing extra element only print pairs
#it will create list of tuples ,if u give tuple(m) it ll give tuple of tuples
# #if u give dict(m) ll print dictionary
#if u give single iterable it ll also print zip output followed by,example below

u=[10,20,3,4]
n=zip(u)
print(list(n))


x=zip()
print(list(x))
print(tuple(x))
print(dict(x))
#EXTENDED SEQUENCE ASSIGNMENT
a,b,c="hai"
print(a)
print(b)
print(c)

a,*b="python"
print(a)
print(b)


#multiple target assignment
a=b=c=d= 10
print(c)

#a,b,c,d= 20  TYPE ERROR

#AUGMENTED ASSIGNMENT
a=10
a+=2   #a=a+2
print(a)

x="55"
y="6"
print(x+y)  #output llbe 556 it adds string format
#texts in double quotes considered as normal text
#input statemnt always prinys string ,then we need to use type conversiobn
a=int(input("enter any number"))
print(a)




