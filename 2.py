with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        if line.startswith(('A', 'a')):
            outfile.write(line)
