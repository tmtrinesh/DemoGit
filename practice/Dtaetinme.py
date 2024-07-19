
#Date and Time Module
 #Year,Month ,Day,Hours,Minutes,Seconds, Microseconds
import datetime
import dataclasses
print(datetime.datetime.now())
#creating date
#we eed to use constructor
x=datetime.datetime(2020,6,7,10)
print(x)
#strftime(parameter) formatting date time feilds
# we can retrieve month date time hour
#parameter--formatting parameter
#function used to retrieve the date and time feilds
# %y==prints year in 2 digit format
# %Y == prints year in 4 digits

#month
# %w== short version of month
# %W== full version of month

#Day
# %a == short version of day
# %A == Full version of day
#Hour
# %H --24 hour format
# %I -- 12 hour  format
#%p ---AM /PM

#Minutes
#%M --0-59 minutes
#%S==0-59 seconds
#%f ==0-999999

res=datetime.datetime(2023,7,20,10,20,59,125)
print(res)
cd=datetime.datetime.now()
res1=cd.strftime("%y")
print("Short version of year:",res1)
res2=cd.strftime("%Y")
print("full version of year:",res2)
res3=cd.strftime("%b")
print("Short version of month:",res3)
res4=cd.strftime("%B")
print("full version of month:",res4)
res5=cd.strftime("%a")
print("Short version of Day:",res5)
res6=cd.strftime("%A")
print("full version of DAy:",res6)
res7=cd.strftime("%w")
print("number of week day",res7)
res8=cd.strftime("%H")
print("24 hr fromat",res8)
res9=cd.strftime("%I")
print("12 hr fromat",res9)
res10=cd.strftime("%p")
print("AM / PM  fromat",res10)