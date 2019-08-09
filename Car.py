from PyQt5.QtCore import QPointF
import math


class Car:

    CAR_GUI_RADIUS=25
    free_distance_ahead = 0  #used to arrange inner car lanes to produce more gaps
    PSUEDO_CAR = False


    def __init__(self,number,angle,lane_changed, lane_radius, **kwargs):
        self.CarAngle = angle
        self.CarNumber = number
        self.lane_changed = lane_changed
        self.CarLaneRadius = lane_radius
        self.lane_change_started = False


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
            if self.CarAngle <= 361 and self.CarAngle >=359:
                self.CarAngle=1
            else:
                self.CarAngle+=0.75

        elif self.CarLaneRadius == 200 :
            if self.CarAngle <= 361 and self.CarAngle >=359:
                self.CarAngle=1
            else:
                self.CarAngle+=1.5

        elif self.CarLaneRadius < 200 and self.CarLaneRadius >=150:

            if self.CarAngle <= 361 and self.CarAngle >=359:
                self.CarAngle=1
            else:
                self.CarAngle+=1.5

            self.CarLaneRadius-=1
            #print (self.CarNumber, self.CarAngle)



        elif self.CarLaneRadius <= 150 and self.CarLaneRadius >= 100:                        # this will be used for cars in transition
            self.CarLaneRadius -= 0.5
            self.CarAngle += self.radius_to_speed_mapping(self.CarLaneRadius,150,200,0.75,1.5)


            #print (self.CarNumber, self.CarAngle)
            #print ("+++++++++++++++++++++++++++++")


        else:
            print("error identifying the lane of the car --- Car.update_car_angle() failed")




    def __str__(self):
        return  ("--------------------- Car number = " + str(self.CarNumber) + " ---------------------\n"
        " Car current angle = " + str(self.CarAngle) + "\n"
        " Car priority = " + str(self.priority) + "\n"
        " Free distance ahead : " + str(self.free_distance_ahead) + "\n\n")



    def radius_to_speed_mapping(self, radius, radius_min, radius_max, speed_min, speed_max):
        # Figure out how 'wide' each range is
        radiusSpan = radius_max - radius_min
        speedSpan = speed_max - speed_min

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(radius - radius_min) / float(radiusSpan)

        # Convert the 0-1 range into a value in the right range.
        return speed_min + (valueScaled * speedSpan)
