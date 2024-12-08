if __name__ == '__main__':
    s = input()
    a = b = c = d = e =  False
    for x in s :
        if x.isdigit() :
            a = a or True
            c = c or True
        if x.islower() :
            a = a or True
            b = b or True
            d = d or True
        if x.isupper() :
            a = a or True
            b = b or True
            e = e or True
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
