lis = sorted(input(),key=str.lower)
lower=""
upper=""
odd=""
even=""

for x in lis :
    if x.isalpha() and x.islower() :
        lower+=x
    elif x.isalpha() and x.isupper() :
        upper+=x
    elif x.isnumeric() and int(x)%2 == 1 :
        odd+=x
    elif x.isnumeric() and int(x) % 2 == 0:
        even+=x
    else:
        pass

print(lower+upper+odd+even)