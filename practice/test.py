str = "Bangalore"

for i in range(0,len(str)):
    print(i,str[i])
#############################################
#to find the duplicates in string using List
string = input()
dups = []
for ch in string:
    if string.count(ch)>1 and ch not in dups:
        dups.append(ch)
print("The duplicate charcters are {}".format(dups))
