import sys
import PyQt4
#from PyQt4 import Qt
from PyQt4 import QtCore, QtGui

class AnnoDialog(QtGui.QDialog):
    #AnnoDialog: adding annotation 
    def __init__(self):
        super(AnnoDialog,self).__init__()
        self.annoContent=""
        self.initUI()
        
    
    def initUI(self):
        
        self.resize(400,300)
        self.setWindowTitle("Window: Adding Annotation")


        gridLayout=QtGui.QGridLayout()
        gridLayout.setMargin(0)
        
        label=QtGui.QLabel("annotation")
        gridLayout.addWidget(label, 0, 0, 1, 1)
        self.inputText=QtGui.QTextEdit()
        gridLayout.addWidget(self.inputText, 1, 1, 1, 1)
        
        self.buttonBox = QtGui.QDialogButtonBox()
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        
        gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.setLayout(gridLayout)
        self.buttonBox.accepted.connect(self.slotOK)
        self.show()
        
    
    def slotOK(self):
        self.close()
        self.annoContent=self.inputText.toPlainText()
        
    
    def getContent(self):
        
        return self.annoContent
        
        #print annoContent
        
        

    

# def main():
#
#     app=QtGui.QApplication(sys.argv)
#     dig=AnnoDialog()
#     sys.exit(app.exec_())
#
#
# if __name__=="__main__":
#     main()
        
        
