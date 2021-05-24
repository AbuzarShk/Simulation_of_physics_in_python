from UIpy import Ui_PYSCHIS
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import startandplanet
import Multipleplanet
import basic_pendulum
import projectilemotiongravity
import rocket
import spring
import reflection
import vectadd
import vectsub
import airfall
import rotation
import webbrowser



class Start_page(QtWidgets.QWidget,Ui_PYSCHIS):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton_Start.clicked.connect(self.Startbutton)
        self.pushButton_About.clicked.connect(self.Aboutbutton)
        self.pushButton_solar_system.clicked.connect(self.Solarsysbutton)
        self.pushButton_start_and_planet.clicked.connect(self.starandplanet)
        self.pushButton_SAPstartSimu.clicked.connect(self.SAPstartsimu)
        self.pushButton.clicked.connect(self.MSAPstartsimu)
        self.pushButton_pendulum.clicked.connect(self.Pendulum)
        self.pushButton_projection.clicked.connect(self.Project)
        self.pushButton_rocket.clicked.connect(self.Rocket)#No to delet
        self.pushButton_MPstart.clicked.connect(self.MSAPstartsuim)
        self.pushButton_Penstart.clicked.connect(self.Pendulumstart)
        self.pushButton_2.clicked.connect(self.Prostart)
        #self.pushButton_RSTART.clicked.connect(self.Rstart)
        self.startroataion.clicked.connect(self.Rotationanimation)
        self.pushButton_spring.clicked.connect(self.Springpage)
        self.pushButton_SpringStart.clicked.connect(self.Springstart)
        self.pushButton_reflection.clicked.connect(self.Reflectionstart)
        self.pushButton_vector.clicked.connect(self.vectorpage)
        self.pushButton_3.clicked.connect(self.vectadd)
        self.pushButton_4.clicked.connect(self.vectsub)
        self.pushButton_rolling.clicked.connect(self.rollpage)
        self.pushButton_rollstart.clicked.connect(self.rollingstart)
        self.spl.clicked.connect(self.splbutton)
        self.mspl.clicked.connect(self.msplbutton)
        



    def Startbutton(self):
        self.stackedWidget.setCurrentWidget(self.page_3) 

    def Aboutbutton(self):
        self.stackedWidget.setCurrentWidget(self.page_2) 

    def Solarsysbutton(self):
        self.stackedWidget.setCurrentWidget(self.page_4) 

    def starandplanet(self):
        self.stackedWidget.setCurrentWidget(self.page_5)

    def SAPstartsimu(self):
        MS = None
        MP = None
        MS = int(self.lineEdit_page5_MS.text())
        MP = int(self.lineEdit_page5_MP.text())
        startandplanet.Startandplanet(MS, MP)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def MSAPstartsimu(self):
        self.stackedWidget.setCurrentWidget(self.page_6)


    def Pendulum(self):
        self.stackedWidget.setCurrentWidget(self.page_7)

    def Project(self):
        self.stackedWidget.setCurrentWidget(self.page_8)

    def Rocket(self):
        self.stackedWidget.setCurrentWidget(self.page_9)

    def MSAPstartsuim(self):
        P1 = None
        P2 = None
        P3 = None
        P1 = int(self.lineEdit_Massp1.text())
        P2 = int(self.lineEdit_Massp2.text())
        P3 = int(self.lineEdit_Massp3.text())
        Multipleplanet.Multileplanet(P1,P2,P3)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def splbutton(self):
        chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome).open_new("https://www.youtube.com/watch?v=dTKEwdLIqQM")

    def msplbutton(self):
        chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome).open_new("https://www.youtube.com/watch?v=dTKEwdLIqQM")



        

    def Pendulumstart(self):
        Mass = None
        Len = None
        Dummping = None
        Mass = float(self.lineEdit_page7_Mass.text())
        Len = float(self.lineEdit_page7_lenght.text())
        Dummping = float(self.lineEdit_page7_dummping.text())
        basic_pendulum.Pendulum(Mass, Len, Dummping)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def Prostart(self):
        Mass = None
        Angle = None
        Speed = None
        Mass = float(self.lineEdit.text())
        Speed = float(self.lineEdit_2.text())
        Angle = int(self.lineEdit_3.text())
        projectilemotiongravity.Projectile(Speed, Angle,Mass)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def Rotationanimation(self):
        R = int(self.page9_radi.text())
        X = int(self.page9_x.text())
        Y = int(self.page9_y.text())
        Z = int(self.page9_z.text())
        V = int(self.page9_velocity.text())
        rotation.Rotation(R, X, Y, Z, V)
        self.stackedWidget.setCurrentWidget(self.page_3)
    # def Rstart(self):
    #     RM = None
    #     FM = None
    #     V = None
    #     RM = float(self.lineEdit_MOR.text())
    #     FM = float(self.lineEdit_MOF.text())
    #     V = int(self.lineEdit_VR.text())
    #     rocket.Rocket(RM, FM, V)
    #     self.stackedWidget.setCurrentWidget(self.page_3)

    def Springpage(self):
        self.stackedWidget.setCurrentWidget(self.page_10)

    def Springstart(self):
        KS = None
        LO = None
        M = None
        G = None
        KS = float(self.lineEdit_KS.text())
        LO = float(self.lineEdit_LO.text())
        M = float(self.lineEdit_MA.text())
        G = float(self.lineEdit_G.text())
        spring.Spring(KS, LO, M, G)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def Reflectionstart(self):
        reflection.Reflection()


    def vectorpage(self):
        self.stackedWidget.setCurrentWidget(self.page_11)

    def vectadd(self):
        VAX = int(self.lineEdit_VAX.text())
        VAY = int(self.lineEdit_VAY.text())
        VBX = int(self.lineEdit_VBX.text())
        VBY = int(self.lineEdit_VBY.text())
        vectadd.VECTADD(VAX,VAY,VBX,VBY)
        self.stackedWidget.setCurrentWidget(self.page_3)


    def vectsub(self):
        VAX = int(self.lineEdit_VAX.text())
        VAY = int(self.lineEdit_VAY.text())
        VBX = int(self.lineEdit_VBX.text())
        VBY = int(self.lineEdit_VBY.text())
        vectsub.VECTSUB(VAX,VAY,VBX,VBY)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def rollpage(self):
        self.stackedWidget.setCurrentWidget(self.page_12)

    def rollingstart(self):
        R = float(self.lineEdit_RD.text())
        O = int(self.lineEdit_OD.text())
        L = int(self.lineEdit_LT.text())
        airfall.ROLL(R,O,L)
        self.stackedWidget.setCurrentWidget(self.page_3)


if __name__=='__main__': 
    app = QtWidgets.QApplication([])
    widget = Start_page()
    widget.show()
    app.exec_()
    # sys.exit()