with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    word = ''
    for line in infile:
        if line:
            word += line[0]
    outfile.write(word)
