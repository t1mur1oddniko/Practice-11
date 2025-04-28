with open('input1.txt', 'r') as infile:
    data = infile.read()

with open('output1.txt', 'w') as outfile:
    outfile.write(data.upper())
