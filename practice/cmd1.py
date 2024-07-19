# to find the sum of all the elements from command line
import sys
sum=0
for i in range(1,len(sys.argv)):
    sum+=int(sys.argv[i])
print("result=",sum)

