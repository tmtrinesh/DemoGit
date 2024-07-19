#Write()  **Writlines()
#f1.write(# string)
#example
f1=open("abc.txt","w")
f1.write("Welcome to Python")

#example
f1=open("abc.txt","w")
lines=["hello\n","welcome\n","python Programming"]
f1.writelines(lines)
#lines means data should be written in the form of list

###########################################################################
#Reading options
#1.read()
#f1.read(#bitpositions)
#f1.read(5) # if data conatins "Hello welcome" it reads from left to write i.e "Hello"
#f1.read(5) #now it starts counting from space and reads "_welc"
#f1.read(3) #now it reads from o n read as "ome"

#2.readline
#f1.readline() # everythin in the 1st line will be printed
#if u close file once you open file pointer starts from beginning
#if file not closed means it count from 2nd line

#3. readlines()
#f1.readlines() #it ll read all the lines in the file

#write content
f1=open("abcd.txt","w")
f1.write("Welcome to python")
f1.close()

f1=open("abc.txt","r");
print(f1.read())  #welcome to python ll be printed





