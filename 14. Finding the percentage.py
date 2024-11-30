from functools import reduce

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lis = student_marks.get(query_name)
    print(format(reduce(lambda a,b : a+b , lis)/len(lis),'.2f'))