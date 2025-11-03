class Agent2():

    total_agents = 0

    def __init__(self,code_name,clearance_level):

        self.code_name = code_name
        self.__clearance_level = clearance_level
        Agent2.total_agents += 1

    def getter(self):
        print(self.__clearance_level)


    def setter(self,new_level):

        if new_level >= 1 and new_level <= 10:
            self.__clearance_level = new_level
        else:
            print("Enter a valid level number")


    def report(self):
        print(f"Agent {self.code_name} reporting. clearance level: {self.__clearance_level}")


    @classmethod
    def get_total_agent(cls):
        print(f"Totul agents: {cls.total_agents}")

























