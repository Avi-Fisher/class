from Agent2 import Agent2


class Cyber_agent(Agent2):

    def __init__(self,cose_name,clearance_level,specialty):

        super().__init__(cose_name,clearance_level)
        self.specialty = specialty


    def report(self):
        super().report()
        print(f"specialty: {self.specialty}")