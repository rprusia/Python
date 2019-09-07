# get greatest common divisor without importing anything

def mygcd(x, y):
    while (y):
        x,y = y, x % y

    return x

def main():
    print(mygcd(20, 311))

if __name__ == '__main__':
    main()