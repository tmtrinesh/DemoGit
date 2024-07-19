
#random()  can write as random.random() it ll give float value in between 0.0 to 1.0
#uniform(a,b)  write as random.unifrom(a,b) it ll return float value in b/w a and b
#randint(a,b) can write as random.randint(a,b) returns integer value in b/w a and b
 #getrandbits(k) write as random.getrandbits(k) returns integer value in b/w min decimal val & max decimal val
 #from given bits "k"
 #choice(seq)  write as rand.choice(seq) returns element from given sequence of elements

import random
print(random.random())
print(random.uniform(1.5,5.5))
print(random.randint(1,10))
print(random.getrandbits(3))
list=[1,2,3,4,5,6]
print(list)
print(random.choice(list))
