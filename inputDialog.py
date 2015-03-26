import sys
import PyQt4
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt


class InputDialog(QtGui.QDialog):
    """
    InputDialog for building connection with local database management system 

    """
    def __init__(self):
        super(InputDialog,self).__init__()
        self.initUI()
    
    def initUI(self):
        
        #tilte, size 
        self.resize(400,60)
        self.setWindowTitle("Connect with Local DataBase Managemen System")

       

        database = QtGui.QLabel('DataBase')
        user=QtGui.QLabel('UserName')

        self.databaseEdit = QtGui.QLineEdit()
        self.userEdit = QtGui.QLineEdit()

        gridLayout = QtGui.QGridLayout()
        gridLayout.setSpacing(10)

        gridLayout.addWidget(database,1,0)
        gridLayout.addWidget(self.databaseEdit,1,1)
        gridLayout.addWidget(user,2,0)
        gridLayout.addWidget(self.userEdit,2,1)
        

        #ok,cancel button 

        self.buttons=QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.close)
        self.buttons.rejected.connect(self.close)

        gridLayout.addWidget(self.buttons,3,1)
        self.setLayout(gridLayout)

        #initiate styleSheet
        self.styleWidget()

        self.show()
    

    def styleWidget(self):
        #self.setStyleSheet("background-color:white;");
        with open("./stypleSheet/inputDialog.css",'r') as f:
            tema=f.read()

        #print "loading stypleSheet"
        #print tema
        self.setStyleSheet(tema)

    
    def getInput(self):
        if(self.databaseEdit.text()!="" and self.userEdit.text()!=""):
            return [str(self.databaseEdit.text()),str(self.userEdit.text())]
        else:
            return None




# def main():

#     app=QtGui.QApplication(sys.argv)
#     dig=InputDialog()
#     sys.exit(app.exec_())


# if __name__=="__main__":
#     main()
    

       

       
       
       
