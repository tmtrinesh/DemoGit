#how to create a single element with tuple
#if we create a = (1) it ll treat a as integer and 1 as integer
#so we should write like this a=(1,) element followed by comma
#UPDATING TUPLE
a=(1,2,3,2,4) #we cant add items to both tuple
b=(5,6,7,1,8)
c=a+b  #concatanation
print(c) #updated tuple

#DELETION OF TUPLE
#deletion of single element in tuple we can delete entire tuple
del b

print(c[0:4])
print(c[3:])

#BASIC OPERATIONS
#1.Length 2.Concatantion 3.Repetation 4.membership 5.Iterartive statements
#6.Maximum 7.minimum 8.index 9.count 10.conversion to tuple

print(len(c))
print(a*3)  #repetation
print(1 in a)  #returns true menbership operator

for ele in a:  #Iterative statements
    print(ele)  #prints elements 1 by 1

print(max(c))
print(min(c))
print(c.index(7)) #we have to pass ele as arguement to get the index
print(c.count(2)) # count no of times ele repeated
print(c.index(1))
print(tuple("Hello")) #conerts string to elements
list=[10,20,30,40,50]
print(tuple(list)) #Converts list to tuple
