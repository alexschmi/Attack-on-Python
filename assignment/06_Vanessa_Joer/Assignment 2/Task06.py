def test_function(strg):
    errors_found = []
    open_counts = {'(': 0, '[': 0, '{': 0}

    open_brackets = ['(', '[', '{']
    close_brackets = ['(', '[', '{']

    open = []
    for i in strg:
        if i not in '()[]{}':
            continue
        if i in open_brackets:
            open.append(i)
            open_counts[i] += 1
        if i in close_brackets:
            if open[-1] != open_brackets[close_brackets.index(i)]:
                errors_found.append("Andere Art von Klammern noch offen")
            open.pop(-1)
            open_counts[open_brackets[close_brackets.index(i)]] -= 1
    for i in open_counts.values():
        if i != 0:
            errors_found.append('Nicht alle Klammern geschlossen')
        if len(errors_found) == 0:
            print('Keine Fehler gefunden')
        else:
            print(errors_found)
        return

print(test_function('{[()()]([[]])}{}'))
print(test_function('([)]'))
