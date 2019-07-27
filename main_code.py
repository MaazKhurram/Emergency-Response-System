
from PyQt5.QtWidgets import QApplication,QMainWindow
import GUI_code
import sys


if __name__=='__main__':

    NUMBER_OF_CARS_INNER_LANE = 2
    NUMBER_OF_CARS_OUTER_LANE = 2




    App = QApplication(sys.argv)
    window = GUI_code.Window()



    sys.exit(App.exec())
