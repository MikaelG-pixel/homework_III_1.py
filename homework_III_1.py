calls = 0

def count_calls(a):
    global calls
    calls += a
    return a

def string_info(string):
    b = []
    b.append(len(string))
    b.append(string.upper())
    b.append(string.lower())
    count_calls(1)
    return b

def is_contains(string, list_to_search):
    c = []
    string.lower()
    count_calls(1)
    for i in list_to_search:
        c.append(i.lower())
    return (string.lower() in c)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)