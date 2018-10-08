words = ['cat', 'window', 'defenestrate']
# get length of strings
for w in words:
    print (w, len(w))

# loop over a slice copy of entire list
for w in words[:]:
    if (len(w) > 6):
        words.insert(0,w)

print(words)

#range, iterate over a group of numbers
for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


print(range(10))
print(list(range(5))  )


# The break statement, like in C, breaks out of the innermost enclosing for or while loop.
# Loop statements may have an else clause; it is executed when the loop terminates
# through exhaustion of the list (with for) or when the condition becomes
# false (with while), but not when the loop is terminated by a break statement.
# This is exemplified by the following loop, which searches for prime numbers:
#  for x in range(2, n):
for n in range(2, 10):  
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

# pass statement, does nothing, commonly used for creating minimal class
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl-C)

class MyEmptyClass:
    pass

# Another place pass can be used is as a place-holder for a function or conditional body
# when you are working on new code, allowing you to keep thinking at a more abstract level.
# The pass is silently ignored:
def initlog(*args):
    pass
