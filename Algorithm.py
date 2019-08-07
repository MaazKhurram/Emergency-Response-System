from CarMaintainer import CarMaintainer
from DistanceLeaderBoard import DistanceLeaderBoard

class Algorithm:

    list_of_arcs=[]
    list_of_arrows=[]

    def __init__(self):
        DistanceLeaderBoard()

        for a_gap in DistanceLeaderBoard.Distance_list_inner:       #grab the biggest gap in the inner lane

            if a_gap[2] > 60 : #if the gap is big enough , fill the gap

                car_ahead_number = a_gap[0]
                car_behind_number = a_gap[1]

                for inner_car in CarMaintainer.Inner_Car_List:      #find the car objects using their car number

                    if inner_car.CarNumber == car_ahead_number:
                        car_ahead_angle =  inner_car.CarAngle

                    elif inner_car.CarNumber == car_behind_number:
                        car_behind_angle = inner_car.CarAngle

                    else:
                        pass


                open_spot_angle= car_ahead_angle-30     # fill the gap starting from the front

                #now finding the closest car in the outer lane that can fit in this spot





    def run_algorithm(system_state):

        if system_state==0:
            list(map(lambda x:x.update_car_angle(),CarMaintainer.Inner_Car_List))      # lambda functions to update angle of every car object in this list
            list(map(lambda x:x.update_car_angle(),CarMaintainer.Outer_Car_List))

        elif system_state==1:
            pass











        else:
            print("Invalid system state")