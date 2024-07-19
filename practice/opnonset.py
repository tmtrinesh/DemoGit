s={1,2,3}
t={1,2,5,6,3,4}
s1={1,2,3,10}

#issubset  can also represented as  s<=t
print(s.issubset(t)) #returns boolean output
print(s1.issubset(t))

#issuperset also represented as  s>=t
print(s.issuperset(t)) #return boolean o/p if every element of t present in s

#union  every element of both the sets ll be created into another set with out any duplications
print(s.union(t))
#union can also represented as s!t

#Intersection elements which are present in both s and t
print(s.intersection(t))

#intersection can be implented as s&t


#Difference common elements ll be removed remaining elements ll be printed n represented as s-t
print(t.difference(s)) #t-s
print(s.difference(t))  #display empty set #s-t

#Symmetric Difference returns all the elements of s and t except common elements
print(s.symmetric_difference(t))  #can reprents as  s^t

#Sort
print(sorted(t))





