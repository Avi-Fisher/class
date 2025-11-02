from multiprocessing.util import log_to_stderr

from Agent import Agent
from Mission import Misson
import Intel_tools
from Secret_agent.Mission_control import MissionControl
from Secret_agent.Report import Report

if __name__ == "__main__":

    a1 = Agent("8200",None)
    a1.set_clearance_leval(4)

    m1 = Misson("###","gaze",a1.code_name)

    r1 = Report(m1.mission_name,a1.get_clearance_leval(),m1.assigned_agent)

    mc1 = MissionControl.analyze_report(r1)

    i = Intel_tools.Intel_tools()

    i.log_transmission(a1.code_name,mc1)