import PyQt4 
from PyQt4 import QtGui, QtCore
from summaryResultParser import * 
#from annoButton import * 
#

class SummaryAnnoButton(QtGui.QWidget):
    
    def __init__(self,inputStr):
        
        QtGui.QWidget.__init__(self)
        self.content=inputStr
        self.button=QtGui.QPushButton("..", self)
        self.button.clicked.connect(self.handleButton)
        layout=QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
    
    def handleButton(self):
        
        print "deal with Summary Button"
        print "whose inputStr:%{}".format(self.content)
        
        summaryView=SummaryViewer()
        summaryView.initUI(self.content)
        #annoView.show()
        summaryView.exec_()


class ListAnnosViewer(QtGui.QDialog):
    def __init__(self):
        super(ListAnnosViewer,self).__init__()
    
    def initUI(self,annos):
        layout=QtGui.QVBoxLayout(self)
        self.setWindowTitle("Info about all annotation.")
        for anno in annos:
            s=anno.labelPre()
            label=QtGui.QLabel(s)
            layout.addWidget(label)
        
        self.setLayout(layout)
        
        self.resize(200,300)
    
    


class ExtendedLabel(QtGui.QLabel):
    def __init__(self,parent):
        QtGui.QLabel.__init__(self,parent)
    
    def setSummaryResult(self,sr):
        [result,annos]=sr
        self.result=result
        self.annos=annos # a list of annotation 
        self.setText(self.presentation())
    
    def presentation(self):
        return "{}:{}".format(self.result,len(self.annos))
    
    def mouseReleaseEvent(self,ev):
        self.emit(QtCore.SIGNAL('clicked()'))
    
    def clicked(self):
        #print "click this poor guy"
        annoView=ListAnnosViewer()
        annoView.initUI(self.annos)
        annoView.exec_()
        
        
        


class SummaryInstanceWidget(QtGui.QWidget):
    
    def __init__(self,si):
        #input is one si 
        QtGui.QWidget.__init__(self)
        layout=QtGui.QVBoxLayout(self)
        label=QtGui.QLabel(si.configPresentation())
        hLayout=QtGui.QHBoxLayout()
        #preLabel=ExtendedLabel("clicked this one")
        #preLabel.clicked.connect(clicked)
        #self.connect(preLabel,QtCore.SIGNAL('clicked()'), self.clicked())
        
        
        for sr in si.getResults():
            preLabel=ExtendedLabel(self)
            preLabel.setSummaryResult(sr)
            self.connect(preLabel,QtCore.SIGNAL('clicked()'), preLabel.clicked)
            hLayout.addWidget(preLabel)
        
        layout.addWidget(label)
        layout.addLayout(hLayout)
        #layout.addWidget(preLabel)
    
    def clicked(self):
        print "click this poor guy"
        
    
        



class SummaryViewer(QtGui.QDialog):
    
    def __init__(self):
        
        super(SummaryViewer,self).__init__() 
        #ok    
    
    def initUI(self,content):
        print "initUI"
        layout=QtGui.QVBoxLayout(self)
        self.setWindowTitle("Summary about annotation")
        sumAnnos=SummaryAnnos(content)
        siList=sumAnnos.summaryList()
        
        for si in siList:
            siw=SummaryInstanceWidget(si)
            layout.addWidget(siw)
        self.setLayout(layout)
        
        self.resize(400,600)