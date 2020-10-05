#1. create a variable that stores the following text "the current year is 2020"
year='the current year is 2020'
#2.  split the string in 1. by spaces
print(year.split())

#3.  replace current with last and 2020 with 2019
# print(year.replace("current","last"))
# print(year.replace("2020","2019"))

year = year.replace("current", "last")
year = year.replace("2020", "2019")

year = year.replace("current", "last").replace("2020", "2019")
print(year)
#4.  print the last 4 items in the text in 1.
print(year[-4:])
#5. print the current date
import datetime
now = datetime.datetime.now()
print("current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))