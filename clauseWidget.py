import PyQt4
from PyQt4 import QtCore, QtGui

class ClauseWidget(QtGui.QWidget):
    
    def __init__(self):
        
        super(ClauseWidget,self).__init__()
        self.initUI()
        #self.setClause()
        self.show()
    
    
    def initUI(self):
        
        #layout 
        horizontalLayout=QtGui.QHBoxLayout()
        horizontalLayout.setMargin(0)
        
        #label: attribute, OP, Value 
        fieldLabel=QtGui.QLabel("Attriute")
        opLabel=QtGui.QLabel("OP")
        valueLabel=QtGui.QLabel("Value")
        
        #input: fieldInput, opInput, valueInput
        self.fieldInput=QtGui.QComboBox()
        self.opInput=QtGui.QComboBox()
        self.valueInput= QtGui.QLineEdit()
        
        #add to layout 
        
        horizontalLayout.addWidget(fieldLabel)
        horizontalLayout.addWidget(self.fieldInput)

        horizontalLayout.addWidget(opLabel)
        horizontalLayout.addWidget(self.opInput)

        horizontalLayout.addWidget(valueLabel)
        horizontalLayout.addWidget(self.valueInput)

        self.setLayout(horizontalLayout)
    
    def setClause(self,cols,ops):
        for key in cols:
            self.fieldInput.addItem(key)
        
        for op in ops:
            self.opInput.addItem(op)
        
        #// 
    def getClause(self):
        
        #check it is available 
        attribute=None
        attribute=str(self.fieldInput.currentText())
        op=str(self.opInput.currentText())
        value=str(self.valueInput.text())
        
        whereFormat="{}{}{}"
        
        if len(attribute)==0 or len(op)==0 or len(value)==0: 
            return ""
        else:
            #valid 
            return whereFormat.format(attribute,op,value)


        
    
    
