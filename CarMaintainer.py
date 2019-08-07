from CarCreator import CarCreator




class CarMaintainer:

    Inner_Car_List = []
    Outer_Car_List = []
    In_Transition_List = []

    def __init__(self):

        CarMaintainer.Inner_Car_List = CarCreator.Inner_Car_List     #tying the lists in this class to the lists in CarCreator class
        CarMaintainer.Outer_Car_List = CarCreator.Outer_Car_List





