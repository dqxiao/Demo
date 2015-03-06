import PyQt4 
import sys
#import PyQt4
from PyQt4 import QtCore,QtGui 
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMenu
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QCursor

class WhereEditingWidget(QtGui.QWidget):
    
    def __init__(self):
        super(WhereEditingWidget,self).__init__()
        self.initUI()
        self.mode=None
        self.show()
    
    
    def initToolBar(self):
        self.toolBar = QtGui.QToolBar() 
        self.editAction=QtGui.QAction('Edit', self)
        self.editAction.triggered.connect(self.edit)
        
        self.addAction=QtGui.QAction('ADD', self)
        self.addAction.triggered.connect(self.add)
        
        self.filterActon=QtGui.QAction('Filter', self)
        self.filterActon.triggered.connect(self.filter)
        
        
        self.toolBar.addAction(self.editAction)
        self.toolBar.addAction(self.filterActon)
        self.toolBar.addAction(self.addAction)
        
        #
        #editAction.setShortcut('')
    def filter(self):
        print "filter"
        
    def edit(self):
        #print "editing clause"
        
        cItem=self.clauseTree.currentItem()
        
        #print cItem.text()
        cItem.setFlags(cItem.flags()|Qt.ItemIsEditable)
        
    
    def add(self):
        #self.mode="add"
        print "adding "
    
    
    def initTreeWidget(self):
        
        self.clauseTree=QtGui.QTreeWidget(self)
        
        
        header=QtGui.QTreeWidgetItem(["RelationOp","RelationOp","Clause"])
        
        self.clauseTree.setHeaderItem(header)
        
        root = QtGui.QTreeWidgetItem(self.clauseTree, ["root"]) # get current item 
        A = QtGui.QTreeWidgetItem(root, ["A"])
        barA = QtGui.QTreeWidgetItem(A, ["bar", "i", "ii"])
        bazA = QtGui.QTreeWidgetItem(A, ["baz", "a", "b"])
        
        
        self.clauseTree.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.clauseTree.addAction(self.addAction)
        self.clauseTree.addAction(self.editAction)
        
        #
    
    def context_menu(self):
        print "context_menu"
        menu=Qmenu(self)
        menu.addAction("edit")
        menu.addAction("add")
        menu.exec_(QCursor.pos())
        #menu.addAction(self.filterActon)
        
        
        
    
    def initUI(self):
        
        #first one build Ver
        self.resize(400,800)
        vLay=QtGui.QVBoxLayout(self)
        self.initToolBar()
        vLay.addWidget(self.toolBar)
        self.initTreeWidget()
        vLay.addWidget(self.clauseTree)
        
        #self.initToolBar()
        

def main():
    app=QtGui.QApplication(sys.argv)
    ex=WhereEditingWidget()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    
    main()
        
        
        
        
        
        
        
        
        