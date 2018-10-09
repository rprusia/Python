import random

faces = ('heads', 'tails')  # tuple

def subproc():
    print('I do something')
    print(' But return nothing')

subproc()
print(subproc())  # returns none.

def funcproc():
    return random.choice(faces)

print(funcproc())

# for loop with range
for flipcoin in range(5):
    print(funcproc(), end = ' ' )

print() # blank line

def isadd(arg1, arg2):
    ''' my doc string '''
    return arg1 + arg2

print(isadd(5, 3))

def issum(*args):
    ''' any number of arguments '''
    print( ' args:  ', args)
    total = 0
    for arg in args:
        total += arg
    return total

print('issum(1,2,3,4,5):  ', issum(1,2,3,4,5))
params = ( 5, 4, 3, 2, 1)
print ('issum(*params) ->', issum(*params))

def ilist(alpha, beta= 'default', gamma = 'assumed'):
    return alpha, beta, gamma

print('ilist (required)', ilist('required'))
print("ilist ('pos1', 'pos2', 'pos3')", ilist('pos1', 'pos2', 'pos3'))
print("ilist (gamma = pos1, 'pos2', 'pos3')", ilist('pos1', 'pos2', 'pos3'))