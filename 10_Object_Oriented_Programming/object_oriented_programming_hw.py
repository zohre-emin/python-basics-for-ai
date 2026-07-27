###############################################################

class DataAnlyzingTool:
    def __init__(self, data):
        self.data = data

    def give_info(self):
        print(f"Data: {self.data}")

    def cal_sum(self):
        add = sum(self.data)
        print(f"Summation: {add}")

    def cal_avg(self):
        avarage = sum(self.data)/len(self.data)
        print(f"Avarage: {avarage}")

    def find_max(self):
        maximum = max(self.data)
        print(f"Maximum Value: {maximum}")

    def find_min(self):
            minimum = max(self.data)
            print(f"Maximum Value: {minimum}")

analiz1 = DataAnlyzingTool([10, 20, 30, 40, 50])
analiz1.give_info()
analiz1.cal_sum()
analiz1.cal_avg()
analiz1.find_max()
analiz1.find_min()