class Agent():

    def __init__(self,code_name:str,clearance_level:int ):

        self.code_name = code_name
        self.__clearance_level = clearance_level


    def get_clearance_leval(self):
        return self.__clearance_level


    def set_clearance_leval(self,level):

        if level >= 1 and level <= 5:
            self.__clearance_level = level
        else:
            print("The level is not proper")

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.__clearance_level}")
























