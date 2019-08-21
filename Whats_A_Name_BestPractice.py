def name_in_str(str, name):
    it = iter (str.lower())
    return all(c in it for c in name.lower())

def main():
    str = 'Just enough nice friends'
    name = 'Jennifer'
    print (name_in_str(str, name))


if __name__ == '__main__':
    main()