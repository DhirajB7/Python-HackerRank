def count_substring(string, sub_string):
    len_word = len(string)
    len_sub_string = len(sub_string)
    cnt = 0
    for i in range(0,len_word):
        if i+len_sub_string <= len_word and string[i:i+len_sub_string]==sub_string:
            cnt += 1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)