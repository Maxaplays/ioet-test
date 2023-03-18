import combinations

names = []
employee_data = {}

class Formatter_txt:
    def __init__(self, input_text) -> None:
        self.input_text = input_text
        
    def format_file(self):
        for line in self.input_text:
            line = line.decode().strip('\n\r')
            aux = line.split('=')
            names.append(aux[0])
            employee_data[aux[0]] = combinations.schedule(aux[1])
        return names, employee_data

