str = "India"
print(str[-1])#prints last element
print(str[:-1]) #prints Indi except last element a
print(str[::-1]) #print str in reverse format

list1=["a","b","c"]
list2=[1,2,3]
dict1=dict(zip(list1,list2)) # to print 2 lists in dictionary format
print(dict1)

dict2={list1[i]:list2[i] for i in range(len(list1))}
print(dict2)   # to print 2 lists in dictionary format

dict3={}
for key in list1:
    for value in list2:
        dict3[key]= value
        list2.remove(value)
        break
print(dict3)

#how to count number of class instance in python
class A:
    count=0
    def __init__(self):
        A.count+=1
        print("class A is called")

a1=A()
a2=A()
a3=A() #number of times we call ll be printed
print(A.count)

count=0
class B:
    def __init__(self):
        global count
        count +=1
        print("class B is called")
b1=B()
b2=B()
print(count)

#write a program to find duplicate characters in list exp output i n y
list=["India","is","my","country"]
str=" ".join(list)
print(str)
duplicates=[]
for char in str:
    if str.count(char)>1 and char not in duplicates:
        duplicates.append(char)
print(duplicates)
print(*duplicates) #prints chars in str form


#print uniq char in str
str1="test"  #exp e s
unique=[]
for char in str1:
    if str1.count(char)==1 and char not in unique:
        unique.append(char)
print(unique)