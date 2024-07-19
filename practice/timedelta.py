#Time delta funciton --manipulation of dates
#we can change date time using time delta function with date time library
# syntax --timedelta(Days=value,Hours=value,minutes=value,seconds=value,microseconds=value)
import datetime
current_date=datetime.datetime.now()
print("Current Date",current_date)
new_date=current_date+datetime.timedelta(days=365)
print("new date",new_date)
new_date1=current_date-datetime.timedelta(days=365)
print("new date",new_date1)
new_date2=current_date-datetime.timedelta(weeks=2)
print("new date",new_date2)
new_date3=current_date-datetime.timedelta(hours=2)
print("new date",new_date3)
new_date4=current_date+datetime.timedelta(minutes=40)
print("new date",new_date4)
new_date5=current_date+datetime.timedelta(microseconds=540)
print("new date",new_date5)
