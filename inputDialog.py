import sys
import PyQt4
from PyQt4 import QtCore, QtGui

class InputDialog(QtGui.QDialog):
    #create database connection 
    def __init__(self):
        super(InputDialog,self).__init__()
        self.initUI()
    
    def initUI(self):
        
        mainLayout = QtGui.QVBoxLayout()
        
        layout=QtGui.QHBoxLayout()
        
        
        # 
        self.dblabel=QtGui.QLabel()
        self.dblabel.setText("input DatabaseName:")
        layout.addWidget(self.dblabel)
        self.dbtext=QtGui.QLineEdit()
        layout.addWidget(self.dbtext)
        mainLayout.addLayout(layout)
        
        
        layout=QtGui.QHBoxLayout()
        self.userLabel=QtGui.QLabel()
        self.userLabel.setText("input UserName:")
        layout.addWidget(self.userLabel)
        self.usertext=QtGui.QLineEdit()
        layout.addWidget(self.usertext)
        
        mainLayout.addLayout(layout)
        
        
        
        
       
        
        layout = QtGui.QHBoxLayout()
        button = QtGui.QPushButton("okay") #string or icon
        self.connect(button, QtCore.SIGNAL("clicked()"), self.close)
        
        
        
        layout.addWidget(button)
        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)
        
        self.resize(400,60)
        
        self.setWindowTitle("Connect DataBase in this Machine")
        self.show()
    
    
    def getInput(self):
        
        return [str(self.dbtext.text()),str(self.usertext.text())]




# def main():
#
#     app=QtGui.QApplication(sys.argv)
#     dig=InputDialog()
#     sys.exit(app.exec_())
#
#
# if __name__=="__main__":
#     main()
    

       

       
       
       
