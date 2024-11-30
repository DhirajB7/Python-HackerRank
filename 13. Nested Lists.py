if __name__ == '__main__':
    marks={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in marks.keys() :
            marks[score].append(name)
        else :
            marks[score] = [name]
    sorted_list = list(marks.keys())
    sorted_list.sort()
    name_list = marks.get(sorted_list[1])
    name_list.sort()
    for x in name_list:
        print(x)