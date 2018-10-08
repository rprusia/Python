# shows how to get input form console.
name = input("What is your name?")
print(name)

print (name.lower());  # put value to lower case and print.
print (name.upper());  # put value to uppper case and print.

name = name.upper();   # change value in var to upper

# count the number occurances of a value in a string
numOfChars = name.count("A")
print (numOfChars);

#find, index starts at 0
locationOfValue = name.find("B")
print("First position of 'B'" + str(locationOfValue) )
