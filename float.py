x = 5.0
y = float.fromhex('A')
print('x = ', x, ',', 'y = ' , y)
print('x as integer_ratio() =', x.as_integer_ratio())
print('y.hex() = ', y.hex())

#comparisons can be made
print ('comparisons can be made')
print (' x == y ', x == y)
print (' x != y ', x != y)
print (' x >= y ', x >= y)
print (' x > y ', x > y)
print (' x <= y ', x <= y)
print (' x < y ', x < y)

# math operators
print ('# math operators')
print ('math operators')
print (' x + y ', x + y)
print (' x - y ', x - y)
print (' x * y ', x * y)
print (' x / y ', x / y)
print (' x // y ' , x // y)
print (' x % y ' , x % y)
print (' x ** y ', x ** y)

# there are several useful builtin functions:
print ('there are several useful builtin functions:')
print('divmod (x, y)', divmod(x,y))
print('pow(x,y) ', pow(x,y))
print('abs(-x) ', abs(-x))
print('int(x) ', int(x))
print('float(10) ', float(10))

#inline notation can also be used
print (' x = x + y = ', end = ' ')
x += y
print (x)

print (' x = x - y = ', end = ' ')
x -= y
print (x)

print (' x = x * y = ', end = ' ')
x *= y
print (x)

print (' x = x / y = ', end = ' ')
x /= y
print (x)
