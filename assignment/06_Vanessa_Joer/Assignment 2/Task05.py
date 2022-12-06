def count_brackets(strg):
    count_open = 0
    count_close = 0
    for i in strg:
        if i == "(":
            count_open +=1
        if i == ")":
            count_close +=1
    
    return count_open == count_close

print(count_brackets('(())'))
print(count_brackets('())'))
