

from Car import Car
from random import randint


class CarCreator:


    permission_to_create_car=1
    car_number=1
    car_creation_tries=0
    Inner_Car_List=[]


    def __init__(self, outer_cars, inner_cars):


        self.Inner_Car_List.append(Car(self.car_number,0,1))        #create the first car manually


        for i in range(0,inner_cars-1):                             #create all other cars in a loop

            self.car_number+=1

            while(1):                                         #This infinite loop tries to find an open position for the new car in the inner lane

                if self.car_creation_tries==10:
                    print("Too many inner lane cars")
                    break                                           #if can't find a spot in mentioned tries , the inner lane is probably full
                else:
                    self.car_creation_tries+=1

                random_angle= randint(0,360)                        #create a random angle

                for a_car in self.Inner_Car_List:
                    if abs(random_angle-a_car.CarAngle)<30:         #check if any existing cars are close to this position
                        permission_to_create_car=0

                if self.permission_to_create_car==1:                     #if no existing car is close , it is safe to create a new car at this postion
                    self.Inner_Car_List.append(Car(self.car_number,random_angle,1))
                    break

                else:
                    self.permission_to_create_car=1                 #set the permission back to true for the next trial to find a new random position


        print ("all inner cars created successfully")



        # for i in range(0,outer_cars):
        #     self.car_number+=1
        #
        #     while(1):
        #
        #         if self.car_creation_tries==10:
        #             print("Too many inner lane cars")
        #             break
        #
        #
        #         random_angle= randint(0,360)        # create a random angle
        #
        #         for a_car in Master_Car_List:
        #             if abs(random_angle-a_car.CarAngle)<30:
        #                 permission_to_create_car=0
        #
        #         if permission_to_create_car==1:
        #             Master_Car_List.append(Car(self.car_number,random_angle,1))
        #             permission_to_create_car=0
