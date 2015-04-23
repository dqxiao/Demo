import sys
import PyQt4
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from basicConfig import * 


class summaryInstance(object):
    '''
    a custom data structure, for storing summary instance
    '''
    def __init__(self,name,method,desc):
        
        self.name=name
        self.method=method
        self.desc=desc
    
    def __repr__(self):
        return "%s\n%s\n%s" %(self.name,self.method,self.desc)

class linkSummaryDialog(QtGui.QDialog):

    def __init__(self, parent=None,existSumInstance=None):
        """
        parent: parent widget
        existSumInstance: dict 
                          key: tableName
                          value: summaryInstance attached to this given table 
        """

        super(linkSummaryDialog, self).__init__(parent)

        self.reference=existSumInstance
        self.setWindowTitle("Select Summary Methods Attached to Chosed Table")
        self.resize(400,250)
        self.siList=[]
        layout = QtGui.QGridLayout(self)

      

      	self.tableCombo=QtGui.QComboBox(self)
      	
      	for item in tableList:
      		self.tableCombo.addItem(item)



        self.tableCombo.activated[str].connect(self.onActivated)

        self.model=QtGui.QStandardItemModel()
        self.view=QtGui.QListView()
        self.view.setModel(self.model)






        self.buttons=QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.closeAndRecord)
        self.buttons.rejected.connect(self.rejectSelection)
        
        

        layout.addWidget(self.tableCombo,0,0)
        layout.addWidget(self.view,1,0)
        layout.addWidget(self.buttons)

        self.styleWidget()

        self.show()

    def styleWidget(self):
        #self.setStyleSheet("background-color:white;");
        with open("./stypleSheet/combCheckBox.css",'r') as f:
            tema=f.read()

        #print "loading stypleSheet"
        #print tema
        self.setStyleSheet(tema)

    def onActivated(self,inputText):

      tableName=str(inputText)
      self.tableName=tableName
      self.model=QtGui.QStandardItemModel()
      existSumInstance=self.reference
      for (name,method,desc) in siList:
        si=summaryInstance(name,method,desc)
        item=QtGui.QStandardItem(str(si))
        item.setCheckable(True)
        if(existSumInstance!=None and si.name in existSumInstance[tableName]):
          item.setCheckState(Qt.Checked)
      
        self.model.appendRow(item)
      self.view.setModel(self.model)
    
    def closeAndRecord(self):
      #need to calculation
      self.siList=[]
      for i in range(self.model.rowCount()):
        item=self.model.item(i)
        if(item.checkState()==Qt.Checked):
          #print item.text()
          self.siList.append(str(item.text()))

      self.close()

    def getConfigTableName(self):
      return self.tableName


    def getSummaryList(self):
        return self.siList   
    
    def rejectSelection(self):
        self.close()

# if __name__ == "__main__":
#     '''
#     the try catch here is to ensure that the app exits cleanly no matter what
#     makes life better for SPE
#     '''
#     try:
#         app = QtGui.QApplication([])
#         dl =linkSummaryDialog()
#         dl.exec_()
#     except Exception, e:  #could use as e for python 2.6...
#         print e
#     sys.exit(app.closeAllWindows())

