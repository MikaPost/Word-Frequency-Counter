"""
This file is for our new theme: word Frequency cointer
Create by: Miqayel Postoyan
Date: 30 April
"""
import re

def get_file(fname):
    """
    Function: get_file
    Brief: read txt file
    Params: file name
    Return:	data file
    """
    with open(fname) as f:
        punctuation_pattern = r'[^\w\s]'
        return re.sub(punctuation_pattern, "", f.read()).split()


def count_occurrences(cnt):
    """
    Function: count_occurrences
    Brief: count_occurrences
    Params: data
    Return:	ml list
    """
    ml = {}
    for i in cnt:
        if i.isalpha():
            if i in ml:
                ml[i] += 1
            else:
                ml[i] = 1
    return ml


def printt(mylist):
    """
    Function: printt
    Brief: print list
    Params: mylist
    Return:	None
    """
    for i in mylist:
        print(i[0], i[1])


def main():
    """
    Function: main
    Brief: Entry point
    """
    fname = "a.txt"
    cnt = get_file(fname)
    mylist = count_occurrences(cnt)
    mylist = sorted(mylist.items(), key=lambda x: x[1], reverse=True)
    printt(mylist)


if __name__ == '__main__':
    main()
