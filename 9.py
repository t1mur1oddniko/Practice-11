import os


os.makedirs('simple', exist_ok=True)

with open('input.txt', 'r') as infile, \
     open('simple/input.txt', 'w') as outfile:
    for idx, line in enumerate(infile, start=1):
        if idx % 2 == 0:
            outfile.write(line)
