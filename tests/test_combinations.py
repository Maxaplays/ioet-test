import combinations

def test_group_up_pairs_with_combinations_default() -> None:
    people = {'RENE': {'MO': '10:00-10:20', 'TU': '10:00-12:00', 'TH': '01:00-03:00', 'SA': '14:00-18:00', 'SU': '20:00- 21:00'}, 'ASTRID': {'MO': '10:30-12:00', 'TH': '12:00-12:30', 'SU': '20:00-21:00'}, 'ANDRES': {'MO': '10:00-12:00', 'TH': '12:31-14:00', 'SU': '20:00-21:00'}, 'JUAN': {'MO': '10:15-12:00', 'TU': '10:00-12:00', 'TH': '13:00-13:15', 'SA': '14:00-18:00', 'SU': '20:00-21:00'}, 'MATEO': {'MO': '10:00-12:00', 'TH': '12:00-14:00', 'SU': '20:00-21:00'}}
    n = 10
    result = combinations.group_up_pairs_with_combinations(people, n)
    assert type(result) is dict