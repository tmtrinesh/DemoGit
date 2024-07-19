a = "Trinesh Python Automation"
print(len(a))
print(a[8])
print(a[-1])
print(a[:: -1])
print(a[:])




b = "Tilak \"Civil"
print(b)
c = "Trinesh \'auto"
print(c)


first = "Trinesh"
last = "T M"
#full = f"{first} {last}"    full = f"{len(first)} { 2 + 2}"#like this alkso we can concatanate
full = first + " " +last
print(full)

course = "  Trinesh is a efficient software Engineer"
print(course.upper())
print(course.title())
print(course.strip())
print(course.split())
print(course.find("Eng"))
print(course.find("eng"))   #as python in case sensitive it ll show -1 as output if not found
print(course.replace("s","p"))
print("Eng" in course)
print(course[: 20: -1])


s = "welcome"
for i in s:
    print(i)  # if i use s in place of i we ll get 6 times welcome as oupput as no of chars are
    # 6

t = "Greatest"
for i in range(len(t)):
    print(i,t[i])  #nthis will print the string with index number


x = "Hello"
print(x.center(11,"Y"))
