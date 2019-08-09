
import sys
from CarCreator import CarCreator
import GUI_code

if __name__=='__main__':

    NUMBER_OF_CARS_INNER_LANE = 2  #MAX LIMIT =8
    NUMBER_OF_CARS_OUTER_LANE = 2  #MAX_LIMIT=10

    car_creator_obj= CarCreator(NUMBER_OF_CARS_OUTER_LANE , NUMBER_OF_CARS_INNER_LANE)


    App = GUI_code.QApplication(sys.argv)
    window = GUI_code.Window()
    sys.exit(App.exec())


