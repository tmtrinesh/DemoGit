#basic operation
#1.add 2.length 3.update 4. remove 5.dicard 6.pop 7.clear

s={1,2,3,4}
t={4,5,7}
s.add(6)
print(s)  # value 6 is added
print(len(s))
s.update(t)
print(s) # set ll be updated by t elements
s.remove(6)
print(s)  # element 6 ll be removed from set
s.discard(5)
print(s)  #it ll remove 5 from set

# Diff between remove & discord
#In remove function if element not found it ll return  "Key Error"
#In Discard function if the element not found error ll not be "Raised"
s.pop()
print(s) # it ll remove 1st eleemnt from set
s.clear()
print(s) # it ll clear all elements of the set
#INDEXING AND SLICING CANNOT BE PERFORMED IN SET

s1={1,3,2,5,6,8,7}
print(max(s1))
print(min(s1))
print(sum(s1))
