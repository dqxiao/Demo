import PyQt4
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import Qt
import sys

#import serveral components 
from inputDialog import * 
from sqlTranslater import * 
from annoDiag import * 
from clauseWidget import * 
from sqlParser import * 
from annoButton import *
from summaryAnnoButton import *
from linkSummaryMethod import * 

#for connectio with database 
import psycopg2



class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.desc={}
        self.initDesc()
        self.initUI()
        self.connection=[]
        self.clauseWidgets=[]
        self.queryMode="standard"
        
        
    
    def initDesc(self):
        self.desc["ID"]=["Int"]
        self.desc["Content"]=["Text"]
        self.desc["ops"]=[">",">=","=","!=","<","<="]
        
        
    def conToString(self):
        return "dbname='{}' user='{}'".format(self.connection[1],self.connection[0])
        
        
    
    def initCentralWidget(self):
        
        #self.centralWidget = QtGui.QWidget()
        #tableArea:
        self.TableArea = QtGui.QScrollArea()
        self.TableArea.setWidgetResizable(True)
       

        #tableScroll
        #self.TableScorll = QtGui.QWidget()
        #self.TableScorll.setGeometry(QtCore.QRect(0, 0, 509, 299))

        #tableWidget
        self.tableWidget = QtGui.QTableWidget()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        #self.tableWidget.setWidgetResizable(True)
 #
 #        #tablescroll->tableArea
        self.TableArea.setWidget(self.tableWidget)
        
        
        
        
        self.widget = QtGui.QWidget()
 # #        self.widget.setGeometry(QtCore.QRect(30, 10, 511, 131))
 #
 #
 #        #SQL section
        self.SQLSection = QtGui.QVBoxLayout(self.widget)
        self.SQLSection.setMargin(0)
 #
 #        #ClauseSection
        self.ClauseSection = QtGui.QHBoxLayout()
        self.ClauseArea = QtGui.QScrollArea(self.widget)
        self.ClauseArea.setWidgetResizable(True)
 #
        # ClauseScroll
        self.ClauseScroll = QtGui.QWidget()
        #self.ClauseScroll.setGeometry(QtCore.QRect(0, 0, 424, 72))

         #AddClauseButton

        self.ClauseLayout=QtGui.QVBoxLayout(self.widget)
        self.AddClauseButton = QtGui.QPushButton("Add",self.widget)
        self.FilterButton=QtGui.QPushButton("Filter",self.widget)

        self.ClauseLayout.addWidget(self.AddClauseButton)
        self.ClauseLayout.addWidget(self.FilterButton)

        #add clause Buttoon trigger
        self.AddClauseButton.clicked.connect(self.addClause)
        self.FilterButton.clicked.connect(self.filterClause)



        #ClauseScroll-> ClauseArea
        self.ClauseArea.setWidget(self.ClauseScroll)

        #ClauseArea,addClause-> ClauseSection
        self.ClauseSection.addWidget(self.ClauseArea)
        self.ClauseSection.addLayout(self.ClauseLayout)
        self.ClauseGrid = QtGui.QGridLayout(self.ClauseArea)

        #
        self.RawSqlSection = QtGui.QHBoxLayout()
        self.sqlInput = QtGui.QLineEdit(self.widget)
        self.RawSqlSection.addWidget(self.sqlInput)
        self.execButton = QtGui.QPushButton("exe",self.widget)
        self.execButton.clicked.connect(self.executeSql)

        self.RawSqlSection.addWidget(self.execButton)


        #ClauseSection,RawSqlSection--> SQLSection
        self.SQLSection.addLayout(self.ClauseSection)
        self.SQLSection.addLayout(self.RawSqlSection)


        #self.setCentralWidget(self.centralWidget)
        
       
        
        splitter = QtGui.QSplitter()
        splitter.addWidget(self.widget)
        splitter.addWidget(self.TableArea)
        splitter.setOrientation(Qt.Vertical)
        #self.centralWidget.setCentralWidget(splitter)
        
 #
 #

 #
        
        
        self.setCentralWidget(splitter)
        
    
    
    def initMenuBar(self):
        
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 596, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuMainWindow = QtGui.QMenu(self.menuBar)
        self.menuMainWindow.setObjectName(_fromUtf8("menuMainWindow"))
        MainWindow.setMenuBar(self.menuBar)
        
        

    def initToolBar(self):
        
        self.toolBar = QtGui.QToolBar()
        #self.toolBar.setObjectName(_fromUtf8("toolBar"))
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        
        exitAction = QtGui.QAction(QtGui.QIcon('./image/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)


        conDBAction=QtGui.QAction(QtGui.QIcon('./image/connect_database-icon.gif'), 'Connect', self)
        conDBAction.setShortcut('Command+D')
        conDBAction.setStatusTip('Connect to DataBase')
        conDBAction.triggered.connect(self.connectDBlog)
        
        
        queryAction=QtGui.QAction(QtGui.QIcon('./image/standardQuery.jpg'), 'Query', self)
        queryAction.setStatusTip('Setting query mode as Standard')
        queryAction.triggered.connect(self.queryMode)
        
        
        
        #add annotation Icon 
        self.addAnnoAction=QtGui.QAction(QtGui.QIcon('./image/addAnnotation.tiff'), 'Add Annotation', self)
        self.addAnnoAction.setStatusTip('Add annotation to Select Row')
        self.addAnnoAction.triggered.connect(self.addAnnotation)
        
        
        #standard Propagation
        anQueryAction=QtGui.QAction(QtGui.QIcon('./image/annotationPropagation.jpg'), 'AnnoQuery', self)
        anQueryAction.setStatusTip('Query with annotation')
        anQueryAction.triggered.connect(self.queryAnnoMode)
        
        #summary_aware Propagation
        sanQueryAction=QtGui.QAction(QtGui.QIcon('./image/summary.png'), 'SummaryQuery', self)
        sanQueryAction.setStatusTip('Query with annotation summary')
        sanQueryAction.triggered.connect(self.querySummaryMode)
        
        #Link_in summary instance with current table 
        linkAction=QtGui.QAction(QtGui.QIcon('./image/link.jpg'), 'SummaryQuery', self)
        linkAction.setStatusTip('link summary methods to current table')
        linkAction.triggered.connect(self.linkSummaryMethod)
        
        
        
        
        
        self.toolBar.addAction(exitAction)
        self.toolBar.addAction(conDBAction)
        self.toolBar.addAction(self.addAnnoAction)
        self.toolBar.addAction(queryAction)
        self.toolBar.addAction(anQueryAction)
        self.toolBar.addAction(sanQueryAction)
        self.toolBar.addAction(linkAction)
        
        #return toolbar

    def initUI(self):   
        #self size 
        self.resize(800,1024)
        
        self.initToolBar()
        self.initCentralWidget()
        
        #self.initClauseWidget()
        self.show()
    
    
    def executeAddQuery(self,addAnnoQuery):
        #
        self.cur.execute(str(addAnnoQuery))
        self.conn.commit()
    
    
    def queryMode(self):
        self.queryMode="standard"
        self.addAnnoAction.setDisabled(False)
        
        
    def queryAnnoMode(self):
        
        self.queryMode="standard-propagation"
        
        self.addAnnoAction.setDisabled(True)
    
    
    def querySummaryMode(self):
        self.queryMode="summary-aware"
        self.addAnnoAction.setDisabled(True)
        
    
    def setQueryMode(self):
        
        setPModeQuery="select setPMode("
        setPModeQuery+="\'"
        setPModeQuery+=self.queryMode
        setPModeQuery+="\'"
        setPModeQuery+=");"
        
        self.cur.execute(str(setPModeQuery))
        print "exe:",setPModeQuery
        
        self.conn.commit()
        
        


    
    def addAnnotation(self):
        if(len(self.tableWidget.selectedRanges())==0):
            return
        for item in self.tableWidget.selectedRanges():
            rowIndex=[item.topRow(),item.bottomRow()]
            colIndex=[item.leftColumn(),item.rightColumn()]
        
        
        #local selectQuery 
        
        selectQuery=self.sqlTrans.tranSelectQuery(rowIndex,colIndex)
        
        #trigger one annoDiag and get something 
        annoDiag=AnnoDialog()
        annoDiag.exec_()
        content=annoDiag.getContent()
        #print content 
        
        if(len(content)==0):
            #not adding annotation
            return 
        
        
        addAnnoQuery="add annotation on {"
        addAnnoQuery+=selectQuery
        addAnnoQuery+=" }"
        addAnnoQuery+="\""
        addAnnoQuery+=content
        addAnnoQuery+="\""
        addAnnoQuery+=" ;"
        
        self.executeAddQuery(addAnnoQuery)
        #print "add annotation
    def connectDBlog(self):
        
        cbDiag=InputDialog()
        cbDiag.exec_()
        result=cbDiag.getInput()
        if(result!=None):
            self.connection=result
            self.buildConnect()
        #
    
    def buildConnect(self):
        
        constr=self.conToString()
        self.conn=psycopg2.connect(constr)
        self.cur=self.conn.cursor()
        
    
    def showTable(self,rows):
        
        rowNum=len(rows)
        colnames=[desc[0] for desc in self.cur.description]
        colNum=len(colnames)
        #self.tableWidget.
        self.tableWidget.setRowCount(rowNum)
        self.tableWidget.setColumnCount(colNum)
        
        #
        #newItem=QtGui.QTableWidgetItem(colnames)
        n=0 
        m=0
        for c in colnames:
            newitem=QtGui.QTableWidgetItem(c)
            newitem.setFlags( QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setHorizontalHeaderItem(m,newitem)
            m+=1
        #n+=1
        
        for row in rows:
            m=0
            for c in row:
                newitem=QtGui.QTableWidgetItem(str(c))
                #print newitem
                newitem.setFlags( QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(n,m,newitem)
                m+=1
            n+=1
                
        #
    
    def showAnnoTable(self,rows):
        #here waiting for 
        self.tableWidget.clear()
        rowNum=len(rows)
        colnames=self.sqlTrans.colNames
        colNum=len(colnames)-1
    
        self.tableWidget.setRowCount(rowNum)
        self.tableWidget.setColumnCount(colNum)
       
        print colnames
        
        m=0
        #set colnames
        for c in colnames[:-2]:
            newitem=QtGui.QTableWidgetItem(c)
            self.tableWidget.setHorizontalHeaderItem(m,newitem)
            m+=1
        #
        annoCol=QtGui.QTableWidgetItem("Annotation")
        self.tableWidget.setHorizontalHeaderItem(m,annoCol)
        
        #show row's content into table 
        n=0
        for row in rows:
            for i in xrange(colNum-1):
                newitem=QtGui.QTableWidgetItem(str(row[i]))
                newitem.setFlags( QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(n,i,newitem)
            
            #here show annotation annoButton
            newItem=AnnoButton(str(row[-1]))
            self.tableWidget.setCellWidget(n,i+1,newItem)
            n+=1
            
                
    
    def showSummaryAnnoTable(self,rows):
        
        
        self.tableWidget.clear()
        rowNum=len(rows)
        colnames=self.sqlTrans.colNames
        colNum=len(colnames)-1
    
        self.tableWidget.setRowCount(rowNum)
        self.tableWidget.setColumnCount(colNum)
       
        print colnames
        
        m=0
        #set colnames
        for c in colnames[:-2]:
            newitem=QtGui.QTableWidgetItem(c)
            self.tableWidget.setHorizontalHeaderItem(m,newitem)
            m+=1
        #
        anSummaryCol=QtGui.QTableWidgetItem("AnnoSummary")
        self.tableWidget.setHorizontalHeaderItem(m,anSummaryCol)
        
        
        n=0
        for row in rows:
            for i in xrange(colNum-1):
                newitem=QtGui.QTableWidgetItem(str(row[i]))
                newitem.setFlags( QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(n,i,newitem)
            
            
            
            newItem=SummaryAnnoButton(str(row[-1]))
            self.tableWidget.setCellWidget(n,i+1,newItem)
            n+=1
            
            
        
        
        
        
    
                
        
            
        
        
        
        
    def executeQuery(self):
        self.setQueryMode()
        print self.queryMode
        try:
            self.cur.execute(self.sqlQuery)
        except psycopg2.ProgrammingError:
            self.conn.rollback()
            return
    
        rows=self.cur.fetchall()
        
        # set sqlTrans
        self.sqlTrans=SQLTranslater()
        self.sqlTrans.setTableName("test")
        self.sqlTrans.setRows(rows)
        self.sqlTrans.setDescription(self.cur.description)
        
        if(self.queryMode=="standard"):
            self.showTable(rows)
        if(self.queryMode=="standard-propagation"):
            self.showAnnoTable(rows)
        
        if(self.queryMode=="summary-aware"):
            self.showSummaryAnnoTable(rows)
        
        
    def executeSql(self):
        
        self.sqlQuery=str(self.sqlInput.text())
        self.executeQuery()
        
    def addClause(self):
        
        clauseWidget=ClauseWidget()
        clauseWidget.setClause(self.desc)
        count=len(self.clauseWidgets)
        self.ClauseGrid.addWidget(clauseWidget,count,0)
        self.clauseWidgets.append(clauseWidget)
        
    
    def filterClause(self):
        #default sql query  
        sqlQuery="select * from test;"
        #editing the number 
        if(self.sqlQuery!=sqlQuery):
            sqlQuery=self.sqlQuery
        
        #it is time to parse this sql query 
        
        whereClauses=[]
        for item in self.clauseWidgets:
            sClause=item.getClause()
            #whereClauses.append(item.getClause())
            if(len(sClause)==0):
                continue
            whereClauses.append(sClause)
            
        #parse orignal sql query 
        sParser=SQLParser(sqlQuery)
        sParser.extract_where_part()
        sParser.insertWhereClause(whereClauses)
        
        query=sParser.formatSQL()
        self.sqlQuery=query
        self.executeQuery()
        
        
    
    
    def linkSummaryMethod(self):
        #link summary method to given table 
        #GuI and real execution into different part 
        
        lsDialog=linkSummaryDialog()
        lsDialog.exec_()
        siList=lsDialog.getSummaryList()
        
        #debugging 
        for item in siList:
            print str(item)
        
            
        
        
        
        
               
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
