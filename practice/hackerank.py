#program to print if num is 3 print weird and if if num (2,5) print not wewird
#if num is (6,20) print weird
#if num<20 n even print not weird


n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n > 2 and n <= 5:
    print("Not Weird")
elif n % 2 == 0 and n > 6 and n <= 20:
    print("Weird")
else:
    print("Not Weird")








