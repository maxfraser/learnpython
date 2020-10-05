import datetime

past=datetime.datetime(1997,9,24,11,19,30)
print(past.minute)

today=datetime.datetime.today()
print(today-past)

print(today+datetime.timedelta())
