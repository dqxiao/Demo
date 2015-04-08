import PyQt4 
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from summaryResultParser import * 




# summaryAnnoButton-> summaryView
class SummaryAnnoButton(QtGui.QWidget):
    
    def __init__(self,inputStr):
        
        QtGui.QWidget.__init__(self)
        #self.content=inputStr
        #self.button=QtGui.QPushButton("..", self)

        self.sumAnnos=SummaryAnnos(inputStr)
        annoNum=str(self.sumAnnos.getSize())
        self.button=QtGui.QPushButton(annoNum, self) #this one should be recounstrut
        self.button.clicked.connect(self.handleButton)
        self.annoLabel=QtGui.QPushButton()
        self.annoLabel.setIcon(QtGui.QIcon('./image/anno.png'))
        self.annoLabel.clicked.connect(self.handleButton)

        layout=QtGui.QHBoxLayout(self)
        layout.addWidget(self.annoLabel)
        layout.addWidget(self.button)

    
    def handleButton(self):
        
        #print "deal with Summary Button"
        #print "whose inputStr:%{}".format(self.content)
        
        summaryView=SummaryViewer()
        summaryView.initUI(self.sumAnnos)
        #annoView.show()
        summaryView.exec_()


class ListAnnosViewer(QtGui.QDialog):
    def __init__(self):
        super(ListAnnosViewer,self).__init__()
    
    def initUI(self,annos):
        layout=QtGui.QVBoxLayout(self)
        self.setWindowTitle("Info about all annotation.")

        scrollArea=QtGui.QScrollArea();
        listModel=QtGui.QStandardItemModel();



        for anno in annos:
            s=anno.labelPre()
            item=QtGui.QStandardItem(s)
            listModel.appendRow(item)


        #scrollArea.setModel(listModel)
            #label=QtGui.QLabel(s)
        view=QtGui.QListView()
        view.setModel(listModel)

        scrollArea.setWidget(view)
        scrollArea.setWidgetResizable(True)
        layout.addWidget(scrollArea)
        self.setLayout(layout)
        self.resize(400,600)
    
    


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
    
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)


    def initUI(self,si):

        #input is one si 
        QtGui.QWidget.__init__(self)
        layout=QtGui.QVBoxLayout(self)


        label=QtGui.QLabel(si.configPresentation())
        hLayout=QtGui.QHBoxLayout()
        #I wanto 
        for sr in si.getResults():
            preLabel=ExtendedLabel(self)
            preLabel.setObjectName("ExtendedLabel")
            preLabel.setSummaryResult(sr)
            self.connect(preLabel,QtCore.SIGNAL('clicked()'), preLabel.clicked)
            hLayout.addWidget(preLabel)
        

        layout.setSpacing(0)
        layout.setMargin(0)
        layout.addWidget(label,0)
        layout.addLayout(hLayout,0)
        
        
    
    
    def clicked(self):
        print "click this poor guy"
        
    
        



class SummaryViewer(QtGui.QDialog):
    
    def __init__(self):
        
        super(SummaryViewer,self).__init__() 
        #ok    
    
    def initUI(self,sumAnnos):
        #print "initUI"
        layout=QtGui.QVBoxLayout(self)
        self.setWindowTitle("Summary about annotation")
        siList=sumAnnos.summaryList()
        
        for si in siList:
            siw=SummaryInstanceWidget(self)
            siw.initUI(si)
            layout.addWidget(siw)
        self.setLayout(layout)
        self.styleWidget()
        self.resize(400,300)

    def styleWidget(self):
        with open("./stypleSheet/SummaryInstanceWidget.css",'r') as f:
            tema=f.read()

        #print "loading stypleSheet"
        #print tema
        self.setStyleSheet(tema)












