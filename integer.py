x = 5
y = 10
y = 0xA # hexadecimal
y = 0o12 # octal (Python 2 use 012)
y = 0b1010 # binary

print ('x = ', x, ',','y = ', y)

#comparisons can be made
print ('comparisons can be made')
print (' x == y ', x == y)
print (' x != y ', x != y)
print (' x >= y ', x >= y)
print (' x > y ', x > y)
print (' x <= y ', x <= y)
print (' x < y ', x < y)

# math operators
print ('math operators')
print (' x + y ', x + y)
print (' x - y ', x - y)
print (' x * y ', x * y)
print (' x / y ', x / y)

# phython 2 uses x / y floor division
print ('phyton 2 floor division')
print('x // y = ', x // y)
print('x % y = ', x % y)
print('x ** y =', x ** y)

# several builtin functions
print ('Several builtin functions')
print('divmod (x, y)',divmod(x,y))
print('pow (x,y)', pow(x,y))
print('abs(-x)', abs(-x))
print('int(5.2) ', int(5.2))
print('int("0xff", 16) = ' , int("0xff", 16))
print('float(x) ', float(x))

# inline functions
print ('# inline functions')
print('x = x + y = ', end = ' ' )
x += y
print(x)

print('x = x - y = ', end = ' ' )
x -= y
print(x)

print('x = x * y = ', end = ' ' )
x *= y
print(x)

print('x = x / y = ', end = ' ' )
x /= y
print(x)

#multiple assignments can be done
print('#multiple assignments can be done')
x, y = 4, 2
print('x = ', x, ',', 'y = ', y)

# bitwise operators
print('bitwise operators')
print('Or: x | y = ', x | y)
print('Xor: x ^ y = ', x ^ y)
print('And:  x & y = ', x & y)
print('Left Shift: x << y', x << y)
print('Right Shift: x >> y', x >> y)
print('Inversion:  -x = ', -x)

