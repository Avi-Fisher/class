from Agent2 import Agent2

class Agent_field(Agent2):

    def __init__(self,code_name,clearance_level,region):

        super().__init__(code_name,clearance_level)
        self.region = region


    def report(self):
        super().report()
        print(self.region)



