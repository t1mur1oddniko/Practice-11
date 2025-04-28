try:
    with open('input.txt', 'r') as infile:
        lines = infile.readlines()
    n = int(lines[0].strip())
except ValueError:
    with open('output.txt', 'w') as outfile:
        outfile.write('ERROR')
else:
    result = 'YES' if len(lines) - 1 == n else 'NO'
    with open('output.txt', 'w') as outfile:
        outfile.write(result)
