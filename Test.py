g = 9.81
global g

class Mass:
    def __init__(self, m):
        self.m = m

    def get_weight(self):
        print(self.m * g)

mass1 = Mass(1)
mass1.get_weight()