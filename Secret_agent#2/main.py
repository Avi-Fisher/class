from Agent2 import Agent2
from Mission2 import Mission2
from Agent_field import Agent_field
from Agent_cyber import Cyber_agent





def report_agents(agents):

    for i in agents:
        agents.report








if __name__ == "__main__":

    agent1 = Agent2("avi",2)
    mission = Mission2("kill","gaze",agent1)

    agent_field = Agent_field("Avi",5,"Hi")
    agent_field.report()

    agent_cyber = Cyber_agent("or",1,"abc")
    agent_cyber.report()

    agent2 = Agent2("df",5)
    agent3 = Agent2("gfds",9)

    agent3.get_total_agent()


