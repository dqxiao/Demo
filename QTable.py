import sys
import PyQt4
 
from PyQt4 import QtCore, QtGui, QtSql
#from PyQt4.QtGui import *  
#from PyQt4.QtCore import *
#from PyQt4.QtSql import *
 
#from Ui_MainWindow import *
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        super(MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")        
        self.resize(640, 480)
        self.WindowTitle="Soft Collection"
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(81, 20))
        self.label.setMaximumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(471, 20))
        self.comboBox.setObjectName("comboBox")        
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentIndex(0)
        self.horizontalLayout.addWidget(self.comboBox)
        self.cmdApply = QtGui.QPushButton(self.centralwidget)
        self.cmdApply.setMinimumSize(QtCore.QSize(31, 23))
        self.cmdApply.setMaximumSize(QtCore.QSize(31, 23))
        self.cmdApply.setObjectName("cmdApply")
        self.horizontalLayout.addWidget(self.cmdApply)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("mytable")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)        
        self.verticalLayout.addWidget(self.tableWidget)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(self)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\Python26\personal projects\SoftCollection\_eric4project\exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtGui.QAction(self)
        self.actionExit_2.setIcon(icon)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFile.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
 
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.actionExit_2, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self)
 
def initialize():
    #MainWindow.comboBox.addItem("*")
    #Qstring="SELECT DISTINCT CAT from SoftCollection ORDER BY CAT"
    #qcat=QtSql.QSqlQuery()
    #qcat=getqcat(Qstring)
 
    #fieldNo = qcat.record().indexOf("CAT");
    # while (qcat.next()):
#         cat = qcat.value(fieldNo).toString()
#         MainWindow.comboBox.addItem(cat)
#     MainWindow.comboBox.setCurrentIndex(0)
    UpdateTable()
    pass
 
def UpdateTable():
    #Qstring="SELECT CAT,SDESC,VER,EXE,COM from SoftCollection ORDER BY SDESC"
    #qlist=QtSql.QSqlQuery(db)
    #qlist.exec_(Qstring)
    MainWindow.tableWidget.clear()
    MainWindow.tableWidget.setColumnCount(5)
    MainWindow.tableWidget.setHorizontalHeaderLabels(["Cat", "Description", "Version", "Path", "CRemarques"])
    MainWindow.tableWidget.setAlternatingRowColors(True)
    row=0
    # MainWindow.tableWidget.setRowCount(0)
#     while (qlist.next()):
#         row += 1
#         MainWindow.tableWidget.setRowCount(row)
#         for fn in range(5):
#             print row, fn, qlist.value(fn).toString()
#             newitem=QtGui.QTableWidgetItem('%s,%s' %(row,fn))
#             #newitem=QtGui.QTableWidgetItem("test")
#             #newitem=QtGui.QTableWidgetItem(unicode(qlist.value(fn).toString()))
#             MainWindow.tableWidget.setItem(row,fn ,newitem)
#     #MainWindow.tableWidget.resizeColumnsToContents()
#     pass
 
def dbConnect():   
    db = QtSql.QSqlDatabase.addDatabase("QODBC3")
    db.setDatabaseName("SoftCollection")
    db.setUserName("")
    db.setPassword("")
    db.open()
    return db
 
def getqcat(Qstring):
    qs=QtSql.QSqlQuery(db)
    qs.exec_(Qstring)
    return qs   
 
if __name__ == "__main__":    
    app = QtGui.QApplication(sys.argv) 
 
    #db=QtSql.QSqlDatabase()
    #db=dbConnect()    
 
    MainWindow = MainWindow()
    initialize()
    MainWindow.show()   
 
    sys.exit(app.exec_())