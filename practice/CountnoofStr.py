str = input("Enter a string \n")
lst = []
for data in str:
    if data not in lst:
        lst.append(data)
print(lst)
for char in lst:
    print(char,"",str.count(char),"times")

