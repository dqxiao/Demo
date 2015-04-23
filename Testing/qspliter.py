import PyQt4
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
import sys


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.textedit = QtGui.QTextEdit()
        self.textedit.setText("This is a TextEdit!")

        self.listwidget = QtGui.QListWidget()
        self.listwidget.addItem("This\nis\na\nListWidget!")

        self.treewidget = QtGui.QTreeWidget()
        self.treewidget.setHeaderLabels(['This','is','a','TreeWidgets!'])

        splitter = QtGui.QSplitter(self)
        splitter.addWidget(self.textedit)
        splitter.addWidget(self.listwidget)
        splitter.addWidget(self.treewidget)
        splitter.setOrientation(Qt.Vertical)
        self.setCentralWidget(splitter)
        self.show()
        
        
       
        


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    