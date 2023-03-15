def convert_time(schedule):
    
    hour_start_str,hour_end_str = schedule.split('-')
    
    try:
        hour_start, min_start = map(int, hour_start_str.split(":"))
        hour_end, min_end = map(int, hour_end_str.split(":"))
        total_time = {"hour_start":int(hour_start),"min_start":int(min_start),"hour_end":int(hour_end),"min_end":int(min_end)}
    except:
        print("Indicated format for time: 'MO10:00-10:20' not met")
        return 0  
    
    return total_time

def compare_times(first_employee_time, second_employee_time):
    if first_employee_time["hour_start"] > second_employee_time["hour_end"]:
        return 0
    if first_employee_time["hour_start"] < second_employee_time["hour_start"]:
        return 0
    if first_employee_time["hour_end"] == second_employee_time["hour_start"]:
        if first_employee_time["min_end"] >= second_employee_time["min_start"]:
            return 1
        return 0
    return 1
            

def compare_dict(first_employee, second_employee):
    total = 0
    for key in first_employee:
        if key in second_employee.keys():
            first_employee_time = convert_time(first_employee[key])
            second_employee_time = convert_time(second_employee[key])
            total += compare_times(first_employee_time, second_employee_time)
    return total    

def group(people, n):
    pairs = []
    n = 0
    combination = {}
    while n < len(people.keys()):
        for i in people.keys():
            for g in people.keys():
                if i != g and g + i not in pairs:
                    pairs.append(i + g)
                    combination[i + '-' + g] = compare_dict(people[i],people[g])
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

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
        
x = factorial(len(names))/(factorial(2)*(factorial(len(names)-2)))

result =group(employee_data,x)
for key, value in result.items():
    print(key + ": \t" + str(value))
