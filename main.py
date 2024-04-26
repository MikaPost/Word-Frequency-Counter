import re

def get_argument(fname):
    with open(fname) as f:
        punctuation_pattern = r'[^\w\s]'
        return re.sub(punctuation_pattern, "", f.read()).split()


def count_occurrences(cnt):
    ml = {}
    for i in cnt:
        if i.isalpha():
            if i in ml:
                ml[i] += 1
            else:
                ml[i] = 1
    return ml


def printt(mylist):
    for i in mylist:
        print(i[0], i[1])


def main():
    fname = "a.txt"
    cnt = get_argument(fname)
    mylist = count_occurrences(cnt)
    mylist = sorted(mylist.items(), key=lambda x: x[1], reverse=True)
    printt(mylist)


if __name__ == '__main__':
    main()
