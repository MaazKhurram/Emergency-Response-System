from PyQt5.QtCore import QPointF
import math


class Car:

    def __init__(self,number,angle,lane_changed):
        self.CarAngle = angle
        self.CarNumber = number
        self.lane_changed = lane_changed



    def calculate_position(self):
        self.carX=100*math.cos(math.radians(self.CarAngle))
        self.carY=100*math.sin(math.radians(self.CarAngle))

        return QPointF(self.carX,self.carY)



