class Reader:
    def __init__(self,input_name, order):
        self.input_name = input_name
        self.order = order
        
    def read_txt(self):
        return open(self.input_name,self.order)
    