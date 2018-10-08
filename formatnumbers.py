area = 0
height = 10
width = 20

#calculate the area of a triangle
area = width * height /2

#printing formatted float value with 2 decimal places
print("the area of the triangle would be %.2f" % area)

#printing the formatted decimal number with right justified to take up 6 spaces
#with leading zeros
print("My favorite number is %06d !" % 42)

#do the same thing with the .format syntax to include numbers our output
print("the area of the triangle would be {0:f} ".format(area))
print("my favorite number is {0:d} ".format(42))

#this is an example with multiple numbers
#I have used the \ to indicate command continues on next line
print("Here are three numbers! " + \
      "The first is {0:d} The second is {1:4d} and {2:d}".format(7,8,9))

# format numbers
print("I have %d cats" % 6)
print("I have %3d cats" % 6)
print("I have %03d cats" % 6)
print("I have %f cats" % 6)
print("I have %.2f cats" % 6)

# format method
print("I have {0:d} dogs".format(7))
print("I have {0:3d} dogs".format(6))
print("I have {0:03d} dogs".format(6))
print("I have {0:f} dogs".format(1))
print("I have {0:.2f} dogs".format(6))


#int(value) 	converts to an integer
#long(value) 	converts to a long integer
#float(value) 	converts to a floating number
#(i.e. a number that can hold decimal places)
#str(value) 	converts to a string

# convert input to from string to numeric value so it can be added.
salary = input ("Enter your salary")
bonus = input ("Enter your bonus")
paycheck = float(salary) + float(bonus)
print ("You salary is ", paycheck)