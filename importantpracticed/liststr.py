list = ["run ipmitool cmd from csv","in band","get cmd only","run ib cmd via ssh and validate output"]
#list.insert(1,"in abc")
list.__delitem__(1)
print(list)
list.insert(1,"in abc")
print(list)

###############################################################
#Mphasis question