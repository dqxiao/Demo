import PyQt4 
from PyQt4 import QtGui, QtCore
from summaryAnnoButton import *
from spResultParser import * 


class AnnoButton(QtGui.QWidget):
    
    def __init__(self,content):
        
        QtGui.QWidget.__init__(self)
        self.annos=ProAnnos(content).annos
        annoNum=str(len(self.annos))
        self.button=QtGui.QPushButton(annoNum, self) #this one should be recounstrut
        self.button.clicked.connect(self.handleButton)
        self.annoLabel=QtGui.QPushButton()
        self.annoLabel.setIcon(QtGui.QIcon('./image/anno.png'))
        self.annoLabel.clicked.connect(self.handleButton)
        layout=QtGui.QHBoxLayout(self)
        layout.addWidget(self.annoLabel)
        layout.addWidget(self.button)
        self.styleWidget()
    

    def styleWidget(self):
        #self.setStyleSheet("background-color:white;");
        with open("./stypleSheet/annoButton.css",'r') as f:
            tema=f.read()

        #print "loading stypleSheet"
        #print tema
        self.setStyleSheet(tema)

    def handleButton(self):
        annoView=ListAnnosViewer()
        annoView.initUI(self.annos)
        annoView.exec_()



            
        
        
    
        
        
        




