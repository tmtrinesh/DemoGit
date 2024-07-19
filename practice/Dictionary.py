# DICTIONARY:Group of  key and value pairs separated with coma enclosed by curly braces
Dict={"name":"abc","Rno":514,"Dept":"EEE"} # we call key:value as items of dictionary
print(Dict)
#dictionary is not based on index its based on key
#if the key is string you should pass as print(dict["c"]),with comma s as shown
dict={ } #empty dictionary
print(dict)
#dict() -- key and value pairs in tuple
#dict[(key1:value1),(key2:value2),(key3:value3)])

# we can also create dictionay using comprehension
#Expression ,Iteration,Condition
#dict={expn Itern Condn}
dict1={x:x*2 for x in range(5) if x%2==0} #it is for even series
print(dict1)
dict7={x:x*2 for x in range(5) if x%2==1}
print(dict7)  # for odd series
dict2={x:x*2 for x in range(5)}
print(dict2)   #output ll be 0: 0, 1: 2, 2: 4, 3: 6, 4: 8


#Accessing
#with the help of keys we can accesss corresponding values
dict3={"name":"ABC","Dept":"CSE","Rno":123}
print(dict3["name"])  #prints corresponding value
#items() --displays all key value pairs
#values()--displays all values
#keys()--displays all keys
#ADDING , MODIFING,DELETING
D={"name":"Trinesh","no":36,"Branch":"CSE"}
Dict5={"Course":"B.Tech"}
D.update(Dict5)
print(D)
D["Course"]="M.Tech"   #to update the  dictionaries key with  new value pairs
D["no"]=39
D["University"] = "VTU"  #to add the new dictionaries key with value pairs
print(D)
#we can assign complete dictionary to other variable
A=D
print(A)
del D["name"]
print(D)
A.clear()
print(A)  #it ll delets all elements of dictionay

#Deletion n clear keyword
# del - Keyword --one or more element
#Clear() -function-clears all the elements
# del Dict['key'] -- delets the given key pair
#del DICT -- Removes the dict from memory
#DICT.clear()-- clears all key - value pairs from dictionary
data ={"a":12,"b":25,"c":{"d":15}}



print(data["c"])
print(data.get("c"[0])) #same output as above
print(list(data.values()))
print(data["a"])
#asked in Capgemini
L=[1,89,75,24,64]
L.sort(reverse=False)
print(L)


#asked in Capgemini
#################################################################
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Student("John", 36)

print(p1.name)
print(p1.age)
