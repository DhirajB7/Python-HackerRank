def print_formatted(number):
    a = len(str(bin(number))[2:])
    for i in range(1,number+1) :
        print(f'{str(i).rjust(a)} {str(oct(i)[2:]).rjust(a)} {str(hex(i).upper()[2:]).rjust(a)} {str(bin(i)[2:]).rjust(a)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)