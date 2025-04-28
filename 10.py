def date_to_day_of_year(date_str):
    day, month = map(int, date_str.split('.'))
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(month_days[:month-1]) + day

with open('input.txt', 'r') as infile:
    current_date = infile.readline().strip()
    n = int(infile.readline().strip())
    entries = [infile.readline().strip().split() for _ in range(n)]

current_day = date_to_day_of_year(current_date)

with open('output.txt', 'w') as outfile:
    for cell_number, deposit_date in entries:
        deposit_day = date_to_day_of_year(deposit_date)
        if current_day - deposit_day > 3:
            outfile.write(cell_number + '\n')
