
from random import randint
from Car import Car


class CarCreator:

    permission_to_create_car=1
    car_number=1
    car_creation_tries=0
    Inner_Car_List=[]
    Outer_Car_List=[]

    priority_counter=1 # only for outer lane cars. Lower number means higher priority


    def __init__(self, outer_cars, inner_cars):


        CarCreator.Inner_Car_List.append(Car(CarCreator.car_number, 0, 1))    #create the first car manually


        for i in range(0,inner_cars-1):                         #create all other cars in a loop

            CarCreator.car_creation_tries=0
            CarCreator.car_number+=1

            while(1):                                           #This infinite loop tries to find an open position for the new car in the inner lane

                if CarCreator.car_creation_tries==20:
                    print("Too many inner lane cars")
                    break                                               #if can't find a spot in mentioned tries , the inner lane is probably full
                else:
                    CarCreator.car_creation_tries+=1

                random_angle= randint(0,360)                        #create a random angle



                for a_car in CarCreator.Inner_Car_List:

                    if abs(random_angle-a_car.CarAngle)<30 or abs(random_angle-360-a_car.CarAngle)<30:      #check if any existing cars are close to this position

                        CarCreator.permission_to_create_car=0
                        break

                if CarCreator.permission_to_create_car==1:                                                   #if no existing car is close , it is safe to create a new car at this postion

                    CarCreator.Inner_Car_List.append(Car(CarCreator.car_number, random_angle, 1))
                    break

                else:
                    CarCreator.permission_to_create_car=1                 #set the permission back to true for the next trial to find a new random position




        #---------------------------------------------------------------------------------------------------------------
        #now creating cars in the outer lane

        CarCreator.car_number+=1

        CarCreator.Outer_Car_List.append(Car(CarCreator.car_number, 0, 0))    #create the first car manually


        for i in range(0,outer_cars-1):                         #create all other cars in a loop

            CarCreator.car_creation_tries=0
            CarCreator.car_number+=1

            while(1):                                           #This infinite loop tries to find an open position for the new car in the inner lane

                if CarCreator.car_creation_tries==20:
                    print("Too many outer lane cars")
                    break                                               #if can't find a spot in mentioned tries , the inner lane is probably full
                else:
                    CarCreator.car_creation_tries+=1

                random_angle= randint(0,360)                        #create a random angle



                for a_car in CarCreator.Outer_Car_List:

                    if abs(random_angle-a_car.CarAngle)<20 or abs(random_angle-360-a_car.CarAngle)<20:      #check if any existing cars are close to this position

                        CarCreator.permission_to_create_car=0
                        break

                if CarCreator.permission_to_create_car==1:                                                   #if no existing car is close , it is safe to create a new car at this postion

                    CarCreator.Outer_Car_List.append(Car(CarCreator.car_number, random_angle, 0, priority=CarCreator.priority_counter))
                    CarCreator.priority_counter+=1
                    break

                else:
                    CarCreator.permission_to_create_car=1                 #set the permission back to true for the next trial to find a new random position




