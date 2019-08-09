from CarMaintainer import CarMaintainer
from DistanceLeaderBoard import DistanceLeaderBoard
import math

class Algorithm:

    list_of_arcs=[]
    list_of_arrows=[]

    def __init__(self):
        DistanceLeaderBoard()





                #
                # min_lane_switch_distance = 361  # initial value is the maximum impossible
                #
                # for outer_car in CarMaintainer.Outer_Car_List:          # take each outer car and find how close it is to the available spot
                #     if outer_car.CarAngle > potential_spot_angle_front:    # other > you
                #         lane_switch_distance_front = potential_spot_angle_front+360-outer_car.CarAngle  # = you + 360 - other
                #
                #     elif outer_car.CarAngle < potential_spot_angle_front:    # other < you
                #         lane_switch_distance_front = potential_spot_angle_front - outer_car.CarAngle  # = you - other
                #
                #     else:
                #         lane_switch_distance_front = 362
                #
                #
                #     if lane_switch_distance_front < min_lane_switch_distance:     #find the car closest to the found gap
                #         min_lane_switch_distance = lane_switch_distance_front
                #
                #     else:
                #         pass
                #
                #
                #     if min_lane_switch_distance > 111: # gap is big enough for car to switch lane
                #         CarMaintainer.Inner_Car_List.append()
                #





    def run_algorithm(system_state):

        if system_state==0:
            list(map(lambda x:x.update_car_angle(),CarMaintainer.Inner_Car_List))      # lambda functions to update angle of every car object in this list
            list(map(lambda x:x.update_car_angle(),CarMaintainer.Outer_Car_List))
            #pass

        elif system_state==1:

            list(map(lambda x:x.update_car_angle(),CarMaintainer.Inner_Car_List))      # lambda functions to update angle of every car object in this list
            list(map(lambda x:x.update_car_angle(),CarMaintainer.Outer_Car_List))


            points_to_draw=list()
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


                    if ( car_ahead_angle - 30 ) < 0:        # deciding the angular location to fill up in inner lane
                        potential_spot_angle_front = ( car_ahead_angle -30 ) + 360
                    else:
                        potential_spot_angle_front = ( car_ahead_angle -30 )


                    if  ( car_behind_angle +35 ) > 360 :
                        potential_spot_angle_behind = ( car_behind_angle + 35 ) - 360
                    else:
                        potential_spot_angle_behind =  ( car_behind_angle + 35  )

                    #print("Car ahead angle= ", car_ahead_angle , "potential spot angle front= ", potential_spot_angle_front)
                    #print("Car behind angle= ", car_behind_angle , "potential spot angle behind= ", potential_spot_angle_behind)

                    points_to_draw.append([200*math.cos(math.radians(potential_spot_angle_front)), 200*math.sin(math.radians(potential_spot_angle_front))])
                    points_to_draw.append([200*math.cos(math.radians(potential_spot_angle_behind)), 200*math.sin(math.radians(potential_spot_angle_behind))])


                    for outer_car in CarMaintainer.Outer_Car_List:

                        if potential_spot_angle_front > potential_spot_angle_behind:
                            if outer_car.CarAngle > potential_spot_angle_behind and outer_car.CarAngle < potential_spot_angle_front:

                                if outer_car.PSUEDO_CAR == False :
                                    outer_car.CarLaneRadius-=1
                                    outer_car.PSUEDO_CAR = True
                                    print("status changed Car angle == ",outer_car.CarAngle )


                        elif potential_spot_angle_front < potential_spot_angle_behind:
                            if (outer_car.CarAngle < potential_spot_angle_front and outer_car.CarAngle > 0) or (outer_car.CarAngle > potential_spot_angle_behind and outer_car.CarAngle < 0):

                                if outer_car.PSUEDO_CAR == False :
                                    outer_car.CarLaneRadius-=1
                                    outer_car.PSUEDO_CAR = True
                                    print("status changed Car angle **** ANGLE AT 0 **** == ",outer_car.CarAngle )



                                else:
                                    pass





        else:
            print("Invalid system state")


        return points_to_draw