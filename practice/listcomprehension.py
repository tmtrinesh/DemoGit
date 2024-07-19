#program to find the square of first 5 integers
square=[i**2 for i in range(1,6)] # ** means exponential
print(square)
################################################################################
#using range function printin one by one
for i in range(1,11):
    print(i)
################################################################################
#LOOPING in lists
List=[1,3,5,7,9]
for i in List:
    print(i) # This will print list in newline 1 by 1

################################################################################
#to print each letter of string /set elemnt one by one
set=("Triveni")
for i in set:
    print(i)

string=("Trinesh")
for i in string:
    print(i)
#################################################################################
List1=[1,3,5,7]
List2=[2,4,6,8]
Pair=[(x,y) for x in List1 for y in List2 if x!=y]
print(Pair)


#################################################################################