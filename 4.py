with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        if len(line) > 20:
            outfile.write(line)
