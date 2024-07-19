it=4
while it>1:
    if it !=3: # to skip the number 3
        print(it)
    it = it-1

print("while loop execution  ends")


print("***********Skipping**********")

ix=10
while ix>1:
    if ix ==6: # to skip at 6 n stop
        break
    print(ix)
    ix = ix-1

print("while loop execution  ends with break")

print("***********Continue statement starts**********")

iy=10
while iy>1:
    if iy ==6:
        iy = iy-1  # to skip only 6
        continue
    if iy==3:
        break #to print till 3
    print(iy)
    iy = iy-1

print("while loop execution  ends with continue n break")

print("****************************************")
str = "tutorialspoint"
# initializing a list to add all the duplicate characters
duplicate_char = []
for character in str:
   # check whether there are duplicate characters or not
   # returning the frequency of a character in the string
      if str.count(character) > 1:
   # append to the list if it is already not present
         if character not in duplicate_char:
            duplicate_char.append(character)
print(*duplicate_char)