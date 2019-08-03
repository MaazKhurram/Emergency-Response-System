from PyQt5.QtCore import QPointF
import math


class Car:

    CAR_GUI_RADIUS=25
    free_distance_ahead=0

    def __init__(self,number,angle,lane_changed,**kwargs):
        self.CarAngle = angle
        self.CarNumber = number
        self.lane_changed = lane_changed

        if "priority" in kwargs:            #if priority is mentioned , use it , otherwise default to 0
            self.priority=kwargs['priority']
        else:
            self.priority=0



    def calculate_position(self, lane_identifier):

        if lane_identifier=="inner":
            self.carX=100*math.cos(math.radians(self.CarAngle))
            self.carY=100*math.sin(math.radians(self.CarAngle))

            return QPointF(self.carX,self.carY)

        elif lane_identifier=="outer":
            self.carX=200*math.cos(math.radians(self.CarAngle))
            self.carY=200*math.sin(math.radians(self.CarAngle))

            return QPointF(self.carX,self.carY)

        else:
            print ("error identifying the lane of the car --- Car.calculate_positon() failed")


    def update_car_angle(self,lane_identifier):

        if lane_identifier=="inner":
            if self.CarAngle==360:
                self.CarAngle=1
            else:
                self.CarAngle+=0.75

        elif lane_identifier=="outer":
            if self.CarAngle==360:
                self.CarAngle=1
            else:
                self.CarAngle+=1

        else:
            print("error identifying the lane of the car --- Car.update_car_angle() failed")




    def __str__(self):
        return  ("--------------------- Car number = " + str(self.CarNumber) + " ---------------------\n"
        " Car current angle = " + str(self.CarAngle) + "\n"
        " Car priority = " + str(self.priority) + "\n"
        " Free distance ahead : " + str(self.free_distance_ahead) + "\n\n")



    # def check_gap_inner_lane(self):     # only called on outer lane cars
    #
    #     next_closest_car = None                      #stores the Car object of next closest car
    #
    #     for a_car in CarCreator.Inner_Car_List:
    #         if self.CarAngle == a_car.CarAngle:     #if angle of an outer lane car matches with any inner lane car
    #
    #             anglular_distance= self.
    #             for a_car in CarCreator.Inner_Car_List[1:]:
    #                 anglular_distance= self.ca
    #




