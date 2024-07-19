a=list(map(int,input().split()))
print(a)   # numbers ll b printed as integer
print(type(a[0]))


 #map function is used to convert iterables into required functions..str to int ,float etc
#we can use tuple in place of list

# int to float example
a=list(map(float,input().split()))
print(a)   # numbers ll b printed as floating point nos
print(type(a[0]))

b=input().split()
print(b)     #numbers ll be printed as strings
print(type(b[0]))


# tuple example
a=tuple(map(int,input().split()))
print(a)
print(type(a[0]))

# to read multiple elements in set
a=set(map(float,input().split()))
print(a)


