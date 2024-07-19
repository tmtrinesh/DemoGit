#Sets are similar to list and tuples but it avoids duplication
s={1,'a',2.5,"abc"}
print(s)
s1={2,1,2}
print(s1) # output ll be printed as {1,2} eliminates duplicates

#Creating SET from scrach means from Empty set
#s2={ }
#s2.add(1) #output of set s2 ll be {1}
#print(s2)

#Updating  a set
s3={1,2,3,4,5}
t={7,8,9,6}
s3.update(t)  # while updating also it ll avoid the duplication
print(s3)   #Duplicates ll not be printed







