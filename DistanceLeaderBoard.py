
from CarCreator import CarCreator



class DistanceLeaderBoard:

    Distance_list=[]

    def __init__(self, outer_cars, inner_cars):

        angle_sorted_inner_cars = sorted(CarCreator.Inner_Car_List, key=lambda x: x.CarAngle, reverse=True)

        angle_sorted_inner_cars.insert(0, angle_sorted_inner_cars[len(angle_sorted_inner_cars)-1])        #copy and insert the last Car object in the list on the first place



        for i in range(len(angle_sorted_inner_cars)-1, 0, -1):

            other = angle_sorted_inner_cars[i-1].CarAngle
            you = angle_sorted_inner_cars[i].CarAngle

            if other>you:
                angular_distance=other-you
                self.Distance_list.append([angle_sorted_inner_cars[i-1].CarNumber , angle_sorted_inner_cars[i].CarNumber , angular_distance])        # [other , you , distance between other and you when other is ahead ]


            elif other<you:
                angular_distance=other+360-you
                self.Distance_list.append([angle_sorted_inner_cars[i-1].CarNumber , angle_sorted_inner_cars[i].CarNumber , angular_distance])        # [you , other , distance between other and you when you are ahead ]


        print(*self.Distance_list, sep = "\n")