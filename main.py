import math_operations
import compare_data

def group(people, n):
    pairs = []
    n = 0
    combination = {}
    while n < len(people.keys()):
        for i in people.keys():
            for g in people.keys():
                if i != g and g + i not in pairs:
                    pairs.append(i + g)
                    combination[i + '-' + g] = compare_data.compare_dict(people[i],people[g])
                    n += 1
    return combination


def schedule(line):
    days = []
    work_hours = {}
    days = line.split(',')
    for hours in days:
        work_hours[hours[0:2]] = hours[2:]
    return work_hours
            


names = []
employee_data = {}
with open("MockData.txt",'rb') as source:
    for line in source:
        line = line.decode().strip('\n\r')
        aux = line.split('=')
        names.append(aux[0])
        employee_data[aux[0]] = schedule(aux[1])
      
x = math_operations.combination_without_repetition(names)

result =group(employee_data,x)
for key, value in result.items():
    print(key + ": \t" + str(value))
