from PyQt5.QtCore import QPointF
import math


class Car:

    CAR_GUI_RADIUS=25
    free_distance_ahead=0


    def __init__(self,number,angle,lane_changed, lane_radius, **kwargs):
        self.CarAngle = angle
        self.CarNumber = number
        self.lane_changed = lane_changed
        self.CarLaneRadius = lane_radius


        if "priority" in kwargs:            #if priority is mentioned , use it , otherwise default to 0
            self.priority=kwargs['priority']
        else:
            self.priority=0





    def calculate_position(self):
        self.carX=self.CarLaneRadius*math.cos(math.radians(self.CarAngle))     #outer lane radius is 200
        self.carY=self.CarLaneRadius*math.sin(math.radians(self.CarAngle))
        return QPointF(self.carX,self.carY)



    def update_car_angle(self):

        if self.CarLaneRadius==100:
            if self.CarAngle==360:
                self.CarAngle=1
            else:
                self.CarAngle+=0.75

        elif self.CarLaneRadius <= 200 and self.CarLaneRadius >=150:
            if self.CarAngle==360:
                self.CarAngle=1
            else:
                self.CarAngle+=1

            self.CarLaneRadius-=1



        elif self.CarLaneRadius <= 150 and self.CarLaneRadius >= 100:                        # this will be used for cars in transition
            self.CarLaneRadius -= 0.5
            self.CarAngle += self.radius_to_speed_mapping(self.CarLaneRadius,150,200,0.75,1)    


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



    def radius_to_speed_mapping(self, radius, radius_min, radius_max, speed_min, speed_max):
        # Figure out how 'wide' each range is
        radiusSpan = radius_max - radius_min
        speedSpan = speed_max - speed_min

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(radius - radius_min) / float(radiusSpan)

        # Convert the 0-1 range into a value in the right range.
        return speed_min + (valueScaled * speedSpan)
