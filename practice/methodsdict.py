#Copy() =copy the key - value pairs into another variable d.copy()
#clear() removes all key value pairs  d.clear()
#items() display all the key value pairs availabale in dict d.items()
#Keys()  display all the keys in dictionary d.keys()
#values() display all the values of the dictionary d.values()
#update() used to add one or more items into existing dictionary d.update()
d={"name":"Trinesh","Rno":52,"Course":"B.Tech"}
b=d.copy()
print(b)
b.clear()
print(b)
d.update({"Branch":"CSE","Place":"Bangalore"})
print(d)

print(d.items())

print(d.keys())

print(d.values())
#pop() --used to delete or remove from dict,return the value of a key which is removed
d.pop("Branch")  #giving values is optional to remove
print(d)

#popitem() it ll remove recently inserted items
# value of removed key value pair ll be returned
d.popitem()
print(d)

#get() one arguement --key display the value of given key  --d.get("key")
print(d.get("name"))

#from keys() --2 arguements 1.tuple(keys) and value for all keys
#set default() this ll also take 2 arguements 1 is key and 2nd is value
#d.set default()
print(d.fromkeys("name","Trinesh"))#if u give in dict with curly braces it ll take as 2 keys
#if u give with out curly braces as above it ll treat each char in 1st as a key and common value
e =('k','g','f')
print(d.fromkeys(e,"trinesh"))
print(d.setdefault("Rno",7)) #value doent chamge
d.pop("Rno")
print(d)
print(d.setdefault("Rno",7)) #if r no is deleted then it ll treat rno as default



