import sys
import PyQt4
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


tableList=["bird"]


siList=[
    ('classifier_1','NB'),
    ('classifier_2','SVM'),
    ('cluster_1','KMEANS'),
    ('cluster_2','Gaussian mixtures'),
    ('snippet_1','LDA'),
    ('snippet_2','Text Rank')
]

class summaryInstance(object):
    '''
    a custom data structure, for storing summary instance
    '''
    def __init__(self,name,method):
        
        self.name=name
        self.method=method
    
    def __repr__(self):
        return "%s\n%s" %(self.name,self.method)




class linkSummaryDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(linkSummaryDialog, self).__init__(parent)
        self.setWindowTitle("Select summary methods attached to one table")
        layout = QtGui.QGridLayout(self)

      	#ok think about the stucture 

      	tableCombo=QtGui.QComboBox(self)
      	
      	for item in tableList:
      		tableCombo.addItem(item)

      	#sumMethodList=QtGui.QListWidget(self)


      	# for (name,method) in siList:
      	# 	si=summaryInstance(name,method)
      	# 	siCheck=QtGui.QCheckBox(str(si))
      	# 	sumMethodList.

        self.model=QtGui.QStandardItemModel()


        for (name,method) in siList:
          si=summaryInstance(name,method)
          item=QtGui.QStandardItem(str(si))
          item.setCheckable(True)
          #item.setCheckState(Qt.Checked)
          #item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
          #item.setData(QVariant(Qt.Checked), Qt.CheckStateRole)
          self.model.appendRow(item)



        #
        view=QtGui.QListView()
        view.setModel(self.model)





        self.buttons=QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.closeAndRecord)
        self.buttons.rejected.connect(self.rejectSelection)
        
        

        layout.addWidget(tableCombo,0,0)
        layout.addWidget(view,1,0)

        # layout.addWidget(label,0,0)
        # layout.addWidget(tnLabel,0,1)
        # layout.addWidget(self.listView,1,0)
        # layout.addWidget(self.dz,1,1,2,2)
        
       
        
        layout.addWidget(self.buttons)
        self.show()
        
    
    def closeAndRecord(self):

      # for item in self.model:
      #   if item.checkState()==Qt.Checked:
      #     print item.Text()

      for i in range(self.model.rowCount()):
        item=self.model.item(i)
        if(item.checkState()==Qt.Checked):
          print item.text()

      self.close()




        
    
    def rejectSelection(self):
      print "rejectSelection"
        # self.dz.clearDrops() 
        # self.close()


if __name__ == "__main__":
    '''
    the try catch here is to ensure that the app exits cleanly no matter what
    makes life better for SPE
    '''
    try:
        app = QtGui.QApplication([])
        dl =linkSummaryDialog()
        dl.exec_()
    except Exception, e:  #could use as e for python 2.6...
        print e
    sys.exit(app.closeAllWindows())

