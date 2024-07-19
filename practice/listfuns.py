#Builtin functions
#1.returns value but doesnt change the list are
# 1.count 2.index(value) 3..index(value,start)

list=[1,2,1,3,4,2,1,5]
list1=[3,5,8,75,8,7,1,3,2]

print(max(list1)) #maximum of list
print(min(list1))  # minimum of list
print(len(list1))  # to find the length of list

list[4]=15  # updating the list
print(list)
del list[3]
print(list) #deleted the value 3 with index number 3
print(list.count(1)) # counts the number of occurences of 1
print(list.index(5)) #it ll print the index of element 5 which is in the list
print(list.index(2))#it ll print the 1st index of occurence of 2

#syntax list.index(value,start)
#Example
print(list.index(1,3))  #find the index value of 1 from position 3

#2.Doesnt return vbalue but change the list
#1.append(vlaue) 2.extend(list) 3.insert(index,value) 4.reverse 5.SORT 6.POP

list.append(7)
print(list)  # append ll only add single element @ the end

#extend is used to append more values to list at  a time @ the end
list.extend([56,8,9])
print(list)

#we can insert the value at mentioned index
list.insert(5,100)  # at thre index of 5 value 100 is added
print(list)

#Remove function
# syntax list.remove(value) here 1st appearence of the value will be removed
list.remove(56)
print(list)
list.remove(1)  # 1st occurence of value 1 will be removed
print(list)

#REVERSE function
list.reverse()
print(list)

#SORT function
list1.sort() # in sort it llprint duplicate numbers also with ascending order
print(list1)

#POP fiunction
#always removes the last elemnt from the list
list.pop()#last elemt 100 removed
print(list)
list.pop(2) # in this 2n index value of 7 has been removed
print(list)

a=[1,2,3]
b=[8,9,7]
print(a+b)  #list concatanation
print(a*2)  #list repeatattion

c=['a','s','r','t','n','u']
print(len(c))
print(c[1:4])  #slicing this ll print the elemts from index position 1 to index position (4-1)=3
print(c[-2])  #it ll print the elemnt from 2nd from right to left


m=input()
print(m)
m=input().split()  #to convert to string to list
print(m)  # wher ever we have given space aft every strng that ll treated as 1 eelemnt
print(m[0:2]) # it ll print 1st 2 elemnts in list





