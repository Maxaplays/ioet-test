import math_operations
import combinations
import reader
import formatter_txt

names, employee_data = formatter_txt.Formatter_txt(reader.Reader("MockData.txt", "rb").read_txt()).format_file()
total_number_of_combinations = math_operations.combination_without_repetition(names)

result = combinations.group_up_pairs_with_combinations(employee_data,total_number_of_combinations)
for key, value in sorted(result.items()):
    print(f"{key}: \t{value}")
