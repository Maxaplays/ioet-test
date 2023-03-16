import math_operations
import combinations

class Reader:
    def __init__(self,input_name, order):
        self.input_name = input_name
        self.order = order
        
    def read_txt(self):
        return open(self.input_name,self.order)
    
class Formater:
    def __init__(self, input_text) -> None:
        self.input_text = input_text
        
    def format_file(self):
        for line in self.input_text:
            line = line.decode().strip('\n\r')
            aux = line.split('=')
            names.append(aux[0])
            employee_data[aux[0]] = combinations.schedule(aux[1])


names = []
employee_data = {}

Formater(Reader("MockData.txt", "rb").read_txt()).format_file()
total_number_of_combinations = math_operations.combination_without_repetition(names)

result = combinations.group_up_pairs_with_combinations(employee_data,total_number_of_combinations)
for key, value in sorted(result.items()):
    print(f"{key}: \t{value}")
