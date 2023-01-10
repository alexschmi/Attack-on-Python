def remove_long_words(s, n):
    s = ([i for i in s.split()])
    lst = []
    for x in s:
        if len(x) <= n:
            lst.append(x)
    return print(lst)


remove_long_words(s=input("Input sentence "), n=int(input(" Input number ")))
