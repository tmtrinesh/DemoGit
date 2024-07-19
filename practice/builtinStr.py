a="hello welcome to python programming"
print(a.capitalize()) #convert 1st char of str to capital
print(a.center(40,'c'))  #actual string ll be centered remaining char ll be left n right
print(a.count("o",0,len(a)))#counts str "o"
print(a.endswith("g",0,len(a))) #it ll return boolean output
print(a.find('o',0,len(a)))  #it ll give index value of character 'o'
print(a.index('p',0,len(a))) #it ll give index value of character 'p'
print(a.islower())   # it ll print boolean output  if all char are lower case it ll give True
print(a.title()) #returns every char of str to title case

b="Hello Welcome To Python Programming"
print(b.isupper())  #it ll print boolean output true if all characters are in Upper case
print(b.istitle())  #boolean output if every word 1st char is in upper
print(len(b))  # priints length of character
print(b.upper()) # Print every char to upper
print(b.lower()) # Print every char to lower
print(b.startswith("Hello",0,len(b)))  #returns boolean output

c="Hello"
print(max(c))  # returns maximum char of str
print(min(c))  # returns minimum char of str
print(c.find("l",0,len(c))) #returns the 1st occurence of index of char "l"
print(c.rfind("l",0,len(c))) # returns the lst occurence of index of char "l"
print(c.rindex("l",0,len(c))) # returns the lst occurence of index of char "l"
print(c.swapcase())#upper to lower and vice versa

#techmahindra question
####################################################################################
xyz="pytpythopython"
print(xyz[8::])
#print 2nd largest number in list
#how to assign job in jenkins which should repeat every 5 days
#have u used keywords in robotframework
#structure of the project
#api testing how to get validattions
#2.27 pm  to 2.50pm
#
List1=[10,29,33,28,50,29,60]
List2=list(set(List1))
List2.sort()
print("second largest element is:",List2[-2])




