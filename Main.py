from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class clock (QMainWindow):
    def __init__(self):
        super().__init__()
        timer=QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle('Analog clok')
        self.setGeometry(200,200,300,300)
        self.setStyleSheet('background:black;')
        self.hpointer=QtGui.QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-50)])
        self.mpointer=QtGui.QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-70)])
        self.spointer=QtGui.QPolygon([QPoint(1,1),QPoint(-1,1),QPoint(0,-90)])
        self.bcolor=Qt.green
        self.scolor=Qt.red
    def paintEvent (self,event):
        rec = min(self.width(),self.height())
        Tik=QTime.currentTime()
        painter = QPainter(self)
        def Drawpointer (color,rotation,pointer):
            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2,self.height()/2)
        painter.scale(rec/200,rec/200)
        painter.setPen(QtCore.Qt.NoPen)
        Drawpointer(self.bcolor,(30*(Tik.hour()+Tik.minute()/60)),self.hpointer)
        Drawpointer(self.bcolor,(6*(Tik.minute()+Tik.second()/60)),self.mpointer)
        Drawpointer(self.scolor,(6*Tik.second()),self.spointer)
        painter.setPen(QPen(self.bcolor))
        for i in range(0,60):
            if(i%5)==0:
                painter.drawLine(87,0,97,0)
            painter.rotate(6)
        painter.end()


if __name__=='__main__':
    app=QApplication(sys.argv)
    win=clock()
win.show()
exit(app.exec_())

