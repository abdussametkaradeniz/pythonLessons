#https://www.hackerrank.com/challenges/python-string-split-and-join/problem

if __name__ == '__main__':
    """
    a = input().split()
    words = ""
    for i in range(len(a)):
        if i != len(a)-1:
            words += a[i]+"-"
        else:
            words += a[i]

    print(words)
    """
    #replace

    words = input().replace(" ","-")
    print(words)


    