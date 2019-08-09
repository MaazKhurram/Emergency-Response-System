
from CarMaintainer import CarMaintainer




class DistanceLeaderBoard:

    Distance_list_inner=[]
    Distance_list_outer=[]

    def __init__(self):

        angle_sorted_inner_cars = sorted(CarMaintainer.Inner_Car_List, key=lambda x: x.CarAngle, reverse=True)

        angle_sorted_inner_cars.insert(0, angle_sorted_inner_cars[len(angle_sorted_inner_cars)-1])        #copy and insert the last Car object in the list on the first place



        for i in range(len(angle_sorted_inner_cars)-1, 0, -1):

            other = angle_sorted_inner_cars[i-1].CarAngle
            you = angle_sorted_inner_cars[i].CarAngle

            if other>you:
                angular_distance=other-you
                DistanceLeaderBoard.Distance_list_inner.append([angle_sorted_inner_cars[i - 1].CarNumber , angle_sorted_inner_cars[i].CarNumber , angular_distance])        # [other , you , distance between other and you when other is ahead ]

                angle_sorted_inner_cars[i].free_distance_ahead = angular_distance




            elif other<you:
                angular_distance=other+360-you
                DistanceLeaderBoard.Distance_list_inner.append([angle_sorted_inner_cars[i - 1].CarNumber , angle_sorted_inner_cars[i].CarNumber , angular_distance])        # [other , you , distance between other and you when you are ahead ]

                angle_sorted_inner_cars[i].free_distance_ahead = angular_distance




        DistanceLeaderBoard.Distance_list_inner.sort(key=lambda x: x[2], reverse=True)
        print(*DistanceLeaderBoard.Distance_list_inner, sep ="\n")


        #---------------------------------------
        #inner cars done . now calculating angular distances for outer cars

        angle_sorted_outer_cars = sorted(CarMaintainer.Outer_Car_List, key=lambda x: x.CarAngle, reverse=True)

        angle_sorted_outer_cars.insert(0, angle_sorted_outer_cars[len(angle_sorted_outer_cars)-1])        #copy and insert the last Car object in the list on the first place



        for i in range(len(angle_sorted_outer_cars)-1, 0, -1):

            other = angle_sorted_outer_cars[i-1].CarAngle
            you = angle_sorted_outer_cars[i].CarAngle


            if other>you:
                angular_distance=other-you
                DistanceLeaderBoard.Distance_list_outer.append([angle_sorted_outer_cars[i - 1].CarNumber , angle_sorted_outer_cars[i].CarNumber , angular_distance])        # [other , you , distance between other and you when other is ahead ]

                angle_sorted_outer_cars[i].free_distance_ahead = angular_distance



            elif other<you:
                angular_distance=other+360-you
                DistanceLeaderBoard.Distance_list_outer.append([angle_sorted_outer_cars[i - 1].CarNumber , angle_sorted_outer_cars[i].CarNumber , angular_distance])        # [you , other , distance between other and you when you are ahead ]

                angle_sorted_outer_cars[i].free_distance_ahead = angular_distance


        DistanceLeaderBoard.Distance_list_outer.sort(key=lambda x: x[2], reverse=True)
        print(*DistanceLeaderBoard.Distance_list_outer, sep ="\n")





    def update_leaderboard():           # only used when lane is switched or speed of any car is changed. Not tested yet

        angle_sorted_inner_cars = sorted(CarMaintainer.Inner_Car_List, key=lambda x: x.CarAngle, reverse=True)

        angle_sorted_inner_cars.insert(0, angle_sorted_inner_cars[len(angle_sorted_inner_cars)-1])        #copy and insert the last Car object in the list on the first place

        DistanceLeaderBoard.Distance_list_inner.clear()
        DistanceLeaderBoard.Distance_list_outer.clear()


        for i in range(len(angle_sorted_inner_cars)-1, 0, -1):

            other = angle_sorted_inner_cars[i-1].CarAngle           #other is always ahead of you
            you = angle_sorted_inner_cars[i].CarAngle

            if other>you:
                angular_distance=other-you
                DistanceLeaderBoard.Distance_list_inner.append([angle_sorted_inner_cars[i - 1].CarNumber , angle_sorted_inner_cars[i].CarNumber , angular_distance])        # [ahead , behind , distance between other and you when other is ahead ]

                angle_sorted_inner_cars[i].free_distance_ahead = angular_distance



            elif other<you:
                angular_distance=other+360-you
                DistanceLeaderBoard.Distance_list_inner.append([angle_sorted_inner_cars[i - 1].CarNumber , angle_sorted_inner_cars[i].CarNumber , angular_distance])        # [ahead , behind , distance between other and you when you are ahead ]

                angle_sorted_inner_cars[i].free_distance_ahead = angular_distance

        DistanceLeaderBoard.Distance_list_inner.sort(key=lambda x: x[2], reverse=True)



        #---------------------------------------
        #inner cars done . now calculating angular distances for outer cars

        angle_sorted_outer_cars = sorted(CarMaintainer.Outer_Car_List, key=lambda x: x.CarAngle, reverse=True)

        angle_sorted_outer_cars.insert(0, angle_sorted_outer_cars[len(angle_sorted_outer_cars)-1])        #copy and insert the last Car object in the list on the first place



        for i in range(len(angle_sorted_outer_cars)-1, 0, -1):

            other = angle_sorted_outer_cars[i-1].CarAngle
            you = angle_sorted_outer_cars[i].CarAngle

            if other>you:
                angular_distance=other-you
                DistanceLeaderBoard.Distance_list_outer.append([angle_sorted_outer_cars[i - 1].CarNumber , angle_sorted_outer_cars[i].CarNumber , angular_distance])        # [other , you , distance between other and you when other is ahead ]

                angle_sorted_outer_cars[i].free_distance_ahead = angular_distance





            elif other<you:
                angular_distance=other+360-you
                DistanceLeaderBoard.Distance_list_outer.append([angle_sorted_outer_cars[i - 1].CarNumber , angle_sorted_outer_cars[i].CarNumber , angular_distance])        # [you , other , distance between other and you when you are ahead ]

                angle_sorted_outer_cars[i].free_distance_ahead = angular_distance

        DistanceLeaderBoard.Distance_list_outer.sort(key=lambda x: x[2], reverse=True)

