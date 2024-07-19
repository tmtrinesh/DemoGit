#string can be single word or group of characters represented by "" '' ,''' '''
#we cannot change element of string so they r immutable

#index should be normal value or any mathematical expression whcih return value st(i*2) when i =1 str(2) ll prnt
#by default input function ll read only string
str1="Hello"
str2="world"
print(str1+ " "+str2)
print(str1*3)
#####################################################################################
Str="Welcome to python programming"
print(Str.split())
print(Str[5])
#str3=input()


#print(str3)
char="Welcome"
for i in range(len(char)): #to print charcter with index number
    print(i,char[i])
