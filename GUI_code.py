


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QPainter,QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QTransform
from PyQt5.QtCore import QPointF




from CarMaintainer import CarMaintainer
from Algorithm import Algorithm




class Window(QMainWindow):

    STATE_OF_EMERGENCY=1




    def __init__(self):
        super().__init__()





        timer = QTimer(self)
        timer.setInterval(20) # interval in ms
        timer.timeout.connect(self.update)
        timer.start(0)

        self.title= "Emergency Response System"
        self.top=100
        self.left=100
        self.width=500
        self.height=500


        #button = QPushButton('button', self)
        #button.move(0,0)
        #button.clicked.connect(self.on_click)




        CarMaintainer()
        Algorithm()
        self.InitWindow()



    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)



        self.show()


    def on_click(self):
        Window.STATE_OF_EMERGENCY=1




    def paintEvent(self, e):







        painter= QPainter(self)


        reflecting_axis= QTransform(1,0,0,0,-1,0,250,250,1) #translating the coordinate system to the middle of the screen and reflecting it about x axis to make positive y cooredinates above x axis
        painter.setTransform(reflecting_axis)

        painter.setPen(QPen(Qt.black,1,Qt.SolidLine))
        painter.setBrush(QBrush(Qt.gray,Qt.SolidPattern))

        painter.drawEllipse(QPointF(0,0),250,250)                       #draw outer lane


        painter.setPen(QPen(Qt.yellow,5,Qt.DashLine))
        painter.setBrush(QBrush(Qt.gray,Qt.SolidPattern))

        painter.drawEllipse(QPointF(0,0),150,150)                       #draw inner lane

        painter.setPen(QPen(Qt.black,2,Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black,Qt.SolidPattern))

        painter.drawEllipse(QPointF(0,0),50,50)                         #black centre

        # -------------------------------------------------------------------------------------------------------------
        # Drawing lanes is complete. Now drawing cars

        painter.setBrush(QBrush(Qt.green,Qt.SolidPattern))



        counter=1
        for point in Algorithm.run_algorithm(Window.STATE_OF_EMERGENCY):

            if counter==1:
                painter.drawEllipse(QPointF(point[0], point[1]),10,10)
                counter=-1
            else:
                painter.drawEllipse(QPointF(point[0], point[1]),5,5)
                counter=1




        for a_car in CarMaintainer.Inner_Car_List:
            if a_car.PSUEDO_CAR==False:
                painter.drawEllipse(a_car.calculate_position(),a_car.CAR_GUI_RADIUS,a_car.CAR_GUI_RADIUS)
                painter.drawText(a_car.calculate_position(),str(a_car.CarNumber))

            else:
                painter.setPen(QPen(Qt.red,1,Qt.DashLine))      #new paint settings for Psuedo car
                painter.setBrush(QBrush(Qt.gray,Qt.NoBrush))

                painter.drawEllipse(a_car.calculate_position(),a_car.CAR_GUI_RADIUS,a_car.CAR_GUI_RADIUS)
                painter.drawText(a_car.calculate_position(),str(a_car.CarNumber))

                painter.setPen(QPen(Qt.black,2,Qt.SolidLine))       # restore paint settings after drawing a psuedo car
                painter.setBrush(QBrush(Qt.green,Qt.SolidPattern))




        for a_car in CarMaintainer.Outer_Car_List:
            painter.drawEllipse(a_car.calculate_position(),a_car.CAR_GUI_RADIUS,a_car.CAR_GUI_RADIUS)
            painter.drawText(a_car.calculate_position(),str(a_car.CarNumber))

        for a_car in CarMaintainer.In_Transition_List:


                painter.setBrush(QBrush(Qt.yellow,Qt.SolidPattern))

                painter.drawEllipse(a_car.calculate_position(),a_car.CAR_GUI_RADIUS,a_car.CAR_GUI_RADIUS)
                painter.drawText(a_car.calculate_position(),str(a_car.CarNumber))

                painter.setBrush(QBrush(Qt.green,Qt.SolidPattern))





        painter.setPen(QPen(Qt.red,1,Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green,Qt.NoBrush))

        painter.drawEllipse(QPointF(0,0),100,100)   #draw constuction line on inner lane
        painter.drawEllipse(QPointF(0,0),200,200)   #draw constuction line on outer lane

        painter.setPen(QPen(Qt.red,1,Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red,Qt.SolidPattern))

        # painter.drawEllipse(QPointF(100,0),5,5)
        # painter.drawEllipse(QPointF(-100,0),5,5)
        # painter.drawEllipse(QPointF(0,-100),5,5)



        painter.drawEllipse(QPointF(0,0),10,10)






