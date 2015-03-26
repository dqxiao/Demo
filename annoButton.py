import PyQt4 
from PyQt4 import QtGui, QtCore
from spResultParser import * 

class AnnoButton(QtGui.QWidget):
    
    def __init__(self,inputStr):
        
        QtGui.QWidget.__init__(self)
        self.content=inputStr
        self.button=QtGui.QPushButton("..", self)
        self.button.clicked.connect(self.handleButton)
        layout=QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
    
    def handleButton(self):
        
        #print "deal with Button"
        #print "whose inputStr:%{}".format(self.content)
        
        annoView=AnnoViewer()
        annoView.initUI(self.content)
        #annoView.show()
        annoView.exec_()



class AnnoViewer(QtGui.QDialog):
    
    def __init__(self):
        
        super(AnnoViewer,self).__init__() 
        #ok    
    
    def initUI(self,content):
        #print "initUI"
        layout=QtGui.QVBoxLayout(self)
        self.setWindowTitle("Info about all annotations")
        proAnnos=ProAnnos(content)
        
        scrollArea=QtGui.QScrollArea();
        listModel=QtGui.QStandardItemModel();


        for anno in proAnnos.annos:
            s=anno.labelPre()
            item=QtGui.QStandardItem(s)
            listModel.appendRow(item)
        #what can i do for styling ListView
        view=QtGui.QListView()
        view.setModel(listModel)

        scrollArea.setWidget(view)
        scrollArea.setWidgetResizable(True)
        #
        layout.addWidget(scrollArea)
        
        self.setLayout(layout)
        
        self.resize(400,400)
            
        
        
    
        
        
        




