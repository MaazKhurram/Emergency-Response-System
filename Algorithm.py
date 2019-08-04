from CarMaintainer import CarMaintainer
from DistanceLeaderBoard import DistanceLeaderBoard

class Algorithm:

    list_of_arcs=[]
    list_of_arrows=[]

    def __init__(self):
        DistanceLeaderBoard()
        pass


    def run_algorithm(system_state):

        if system_state==0:
            list(map(lambda x:x.update_car_angle("inner"),CarMaintainer.Inner_Car_List))      # lambda functions to update angle of every car object in this list
            list(map(lambda x:x.update_car_angle("outer"),CarMaintainer.Outer_Car_List))

        elif system_state==1:
            pass





        else:
            print("Invalid system state")