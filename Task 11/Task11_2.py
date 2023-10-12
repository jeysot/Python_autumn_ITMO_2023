with open('data.txt', 'r') as file:
    lines = file.readlines()

data = []
for line in lines:
    number, last_name, first_name, company, salary = line.strip().split(',')
    data.append((int(number), last_name, first_name, company, float(salary)))

sorted_data = sorted(data, key=lambda x: (x[3], x[1], x[2]))

with open('output.xlsx', 'w') as file:
    for item in sorted_data:
        file.write(','.join(map(str, item)) + '\n')

total_salary = sum(item[4] for item in sorted_data)

with open('output.xlsx', 'a') as file:
    file.write(f'ИТОГО, , , , {total_salary}\n')

