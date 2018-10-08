
# Author: Ray
# Date:  Feb 27, 2016
# Following shows how to format dates in python

#import the datetime class
import datetime

#declare and initialize variables
strMyDeadline = ""
intTotalDays = 0
intTotalWeeks = 0
intDays = 0

#Get Today's date
currentDate = datetime.date.today()

#Ask the user for the date of their deadline
strMyDeadline = input("Please enter the date of your deadline (mm/dd/yyyy): ")

deadline = datetime.datetime.strptime(strMyDeadline,"%m/%d/%Y").date()

#Calculate number of days between the two dates
totalNbrDays = deadline - currentDate

#For extra credit calculate results in weeks & days
nbrWeeks = totalNbrDays.days / 7

#The modulo will return the remainder of the division
#which will tell us how many days are left
nbrDays = totalNbrDays.days%7

#display the result to the user
print("You have %d weeks" %nbrWeeks + " and %d days " %nbrDays + "until your deadline.")

#import datetime

## print current date
#currentDate = datetime.date.today()
#print (currentDate)

## print time
#currentTime = datetime.time(hour)
#print (currentTime)

## date formatting
#currentDate = datetime.date.today()
#print(currentDate.strftime("%d %b, %y"))

## date formatting
#currentDate = datetime.date.today()
#print(currentDate.strftime("%d %b, %Y"))