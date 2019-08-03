from CarCreator import CarCreator
from DistanceLeaderBoard import DistanceLeaderBoard



class CarMaintainer:

    Inner_Car_List=None
    Outer_Car_List=None

    def __init__(self):

        CarMaintainer.Inner_Car_List = CarCreator.Inner_Car_List     #tying the lists in this class to the lists in CarCreator class
        CarMaintainer.Outer_Car_List = CarCreator.Outer_Car_List


        print(*CarMaintainer.Inner_Car_List, sep ="\n")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(*CarMaintainer.Outer_Car_List, sep ="\n")

        print("just copied the lists")


    def run_algortihm(self):
        pass



