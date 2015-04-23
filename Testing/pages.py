import sys
import PyQt4


from PyQt4 import QtGui

def createIntroPage():
    page = QtGui.QWizardPage()
    page.setTitle("Introduction")

    label = QtGui.QLabel("This wizard will help you register your copy of "
            "Super Product Two.")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page


def createRegistrationPage():
    page = QtGui.QWizardPage()
    page.setTitle("Registration")
    page.setSubTitle("Please fill both fields.")

    nameLabel = QtGui.QLabel("Name:")
    nameLineEdit = QtGui.QLineEdit()

    emailLabel = QtGui.QLabel("Email address:")
    emailLineEdit = QtGui.QLineEdit()

    layout = QtGui.QGridLayout()
    layout.addWidget(nameLabel, 0, 0)
    layout.addWidget(nameLineEdit, 0, 1)
    layout.addWidget(emailLabel, 1, 0)
    layout.addWidget(emailLineEdit, 1, 1)
    page.setLayout(layout)

    return page


def createConclusionPage():
    page = QtGui.QWizardPage()
    page.setTitle("Conclusion")

    label = QtGui.QLabel("You are now successfully registered. Have a nice day!")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page

class ConnectDBpage(QtGui.QWizard):
    
     def __init__(self):
         super(ConnectDBpage,self).__init__()
         
         self.initUI()
     def initUI(self):
         
         
         self.addPage(createIntroPage())
         
         reg=createRegistrationPage()
         self.addPage(reg)
         self.addPage(createConclusionPage())
         self.show()
         
    
        #self.exec_()
        
     def getValues(self):
         return "yes"

# for testing 
def main():
    
    app=QtGui.QApplication(sys.argv)
    ex=ConnectDBpage()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()
    

        
        