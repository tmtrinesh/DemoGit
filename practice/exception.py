a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
try:
    c=a/b
    print(c)
except:
    print("exception raised")
else:
    print("No exception")
finally:
    print("Program Ends.....")
