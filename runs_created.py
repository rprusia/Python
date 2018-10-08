# Author:  Ray
# Date:  Feb 27, 2016

# The following file will show input from user, forumulas and how to format output
# Determine the runs created using Bill James formula
#  RunsCreated = (TotalBases) (singles+walks) / (AB+walks)
#  TotalBases = singles + doubles + triples + homers

#gather inputs and convert to float
AB = float(input("How many ABs did the player have "))
walks = float(input("How many walks did the player have "))
totalHits = float(input("How many hits did the player have "))
doubles = float(input("How many doubles did the player have "))
triples = float(input("How many triples did the player have "))
homers = float(input("How many homers did the player have "))

# singles
singles = totalHits - doubles - triples - homers
#TotalBases
TotalBases = singles + (2 * doubles) + (3 * triples) + (4 * homers)

RunsCreated = float((TotalBases) * (totalHits + walks) / (AB + walks))  # convert to float

# format RunsCreated as a 2 decimal float
print("The players run created is {0:.2f} ".format(RunsCreated))