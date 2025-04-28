with open('input.txt', 'r') as infile:
    lines = infile.readlines()

with open('input.txt', 'w') as outfile:
    for line in lines:
        if line.strip() != '100':
            outfile.write(line)
