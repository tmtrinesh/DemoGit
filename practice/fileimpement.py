import os
f1=open("hello.txt","w")
f1.write("Welcome to python programming")
f1.close()
os.getcwd()
f1=open("hello.txt","r")
print(f1.read())
print(f1.read(5))#only 5 characters ll be printed
f1.close()

f1=open("mlines.txt","w")
lines=["welcome\n","Python\n","Programming"]
f1.writelines(lines)
f1.close()


f1=open("mlines.txt","r")
print(f1.readline())  #olny one line  ll be printed #welcome
print(f1.readline())  #2nd line ll be printed #python
print(f1.readline())  #3rd line ll be printed #programming
f1.close()

f1=open("mlines.txt","r")
print(f1.read()) # complete content ll be printed
