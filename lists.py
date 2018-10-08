friends = ['kevin', 'jim', 'bob','james']
friends.append('mike')

print(friends)  # print all elements
print(friends[1])
print(friends[-3])  #print reading from end of list
print(friends[1:3])  #print range of list

friends.remove('mike')
print(friends)
friends.pop(2)  # removes item from list
print(friends)
print('number of jims ' + str(friends.count('jim')))

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends2)

friends.insert(1,'kelly')
print(friends)