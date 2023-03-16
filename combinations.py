import compare_data

def generate_pairs(people):
    pairs = set()
    for i in people.keys():
        for g in people.keys():
            if i != g and (g, i) not in pairs:
                pairs.add((i, g))
    return pairs

def get_pair_combinations(pairs, people, n):
    combinations = {}
    for pair in pairs:
        if n == 0:
            break
        i, g = pair
        combinations[f"{i}-{g}"] = compare_data.compare_dict(people[i], people[g])
        n -= 1
    return combinations

def group_up_pairs_with_combinations(people, n):
    pairs = generate_pairs(people)
    return get_pair_combinations(pairs, people, n)

def schedule(line):
    days = []
    work_hours = {}
    days = line.split(',')
    for hours in days:
        work_hours[hours[0:2]] = hours[2:]
    return work_hours
            