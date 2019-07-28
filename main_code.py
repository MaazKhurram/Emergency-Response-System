
from PyQt5.QtWidgets import QApplication,QMainWindow
import GUI_code
import sys

from CarCreator import CarCreator


if __name__=='__main__':

    NUMBER_OF_CARS_INNER_LANE = 5  #MAX LIMIT =8
    NUMBER_OF_CARS_OUTER_LANE = 7 #MAX_LIMIT=8

    CarCreator(NUMBER_OF_CARS_OUTER_LANE , NUMBER_OF_CARS_INNER_LANE)





    App = QApplication(sys.argv)
    window = GUI_code.Window()



    sys.exit(App.exec())
