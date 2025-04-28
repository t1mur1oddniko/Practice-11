with open('input.txt', 'r') as infile:
    steps = [int(line) for line in infile]

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('output.txt', 'w') as outfile:
    idx = 0
    for days in month_days:
        month_sum = sum(steps[idx:idx + days])
        avg = month_sum / days
        outfile.write(str(avg) + '\n')
        idx += days
