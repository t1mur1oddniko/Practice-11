try:
    with open('input.txt', 'r') as infile:
        a, b, c = map(int, infile.read().split())
    result = a / b + c
except ValueError:
    result = 'ValueError'
except ZeroDivisionError:
    result = 'ZeroDivisionError'

with open('output.txt', 'w') as outfile:
    outfile.write(str(result))
