from PyQt5.QtCore import QPointF
import math



class Car:

    def __init__(self,number,angle,lane_changed):
        self.CarAngle = angle
        self.CarNumber = number
        self.lane_changed = lane_changed



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



