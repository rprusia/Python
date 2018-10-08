# Author:  Ray Pruisa
# Example of importing a csv file in python

import csv

READONLY = 'r'
FILENAME = "BaseballBatters2015.csv"

# Programs should always open a file, and close it when they are done
# If they don’t sometimes the code crashes when you try to re-open
# a file that wasn’t closed last time you ran your code

#The ‘with’ ‘:’ syntax is used for certain methods to make sure clean up code
# such as close file runs even if there is an error.
with open (FILENAME, READONLY) as myCSVFile :
    #reader function to return all the rows from the file into a list
    dataFromFile = csv.reader(myCSVFile)

    for currentRow in dataFromFile :
        print(','.join(currentRow))