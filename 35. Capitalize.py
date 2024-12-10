
def solve(s):
    flag = False
    answer = s[0].upper()
    for x in s[1:] :
        if x==' ' :
            flag = True
            answer+=x
        else :
            if flag:
                flag = False
                answer+=x.upper()
            else :
                answer+=x
    return answer





if __name__ == '__main__':
    s = input()
    print(solve(s))

