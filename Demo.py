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
#from linkSummaryMethod import *  // switch to differnt version 
from combCheckBox import * 
from basicConfig import * 
from summaryLinkManager import * 

#for connectio with database 
import psycopg2



class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.table_name="bird"
        self.initUI()
        self.connection=[]
        self.clauseWidgets=[]
        self.queryMode="standard"
        
        
    
    # def initDesc(self):
    #     self.desc["ID"]=["Int"]
    #     self.desc["Content"]=["Text"]
    #     self.desc["ops"]=[">",">=","=","!=","<","<="]
        
        
    def conToString(self):
        return "dbname='{}' user='{}'".format(self.connection[1],self.connection[0])
        
        
    
    def initCentralWidget(self):
        
        #self.filterSection=QtGui.QWidget();
        self.fsMainSplitter = QtGui.QSplitter(Qt.Horizontal)
        
        #button selection 
        self.AddClauseButton = QtGui.QPushButton()
        self.AddClauseButton.setIcon(QtGui.QIcon('./image/add.png'))
        self.FilterButton=QtGui.QPushButton()
        self.FilterButton.setIcon(QtGui.QIcon('./image/filter.png'))
        #signal connecting
        self.AddClauseButton.clicked.connect(self.addClause)
        self.FilterButton.clicked.connect(self.filterClause)
    
        btsplitter=QtGui.QSplitter(Qt.Vertical)
        btsplitter.addWidget(self.AddClauseButton)
        btsplitter.addWidget(self.FilterButton)

        #
        self.ClauseArea = QtGui.QScrollArea()
        self.ClauseScroll = QtGui.QWidget()
        self.ClauseArea.setWidget(self.ClauseScroll)
        self.ClauseGrid = QtGui.QGridLayout(self.ClauseArea)

        self.fsMainSplitter.addWidget(btsplitter)
        self.fsMainSplitter.addWidget(self.ClauseArea)
        self.fsMainSplitter.setStretchFactor(1,1)




        self.sqlSplitter=QtGui.QSplitter(Qt.Horizontal)
        self.sqlInput = QtGui.QLineEdit()
        self.execButton = QtGui.QPushButton()
        self.execButton.setIcon(QtGui.QIcon('./image/exec.png'))

        self.execButton.clicked.connect(self.executeSql)
        self.sqlSplitter.addWidget(self.sqlInput)
        self.sqlSplitter.addWidget(self.execButton)







 

        #tablArea: tableWidget
        self.TableArea = QtGui.QScrollArea()
        self.TableArea.setWidgetResizable(True)
        self.tableWidget = QtGui.QTableWidget()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.TableArea.setWidget(self.tableWidget)

        
    
        #genearal setting middle object 
        splitter = QtGui.QSplitter()
        splitter.addWidget(self.fsMainSplitter)
        splitter.addWidget(self.sqlSplitter)
        splitter.addWidget(self.TableArea)
        splitter.setOrientation(Qt.Vertical)
        self.setCentralWidget(splitter)
        
    
    
    def initMenuBar(self):
        
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 596, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuMainWindow = QtGui.QMenu(self.menuBar)
        self.menuMainWindow.setObjectName(_fromUtf8("menuMainWindow"))
        MainWindow.setMenuBar(self.menuBar)
        
        

    def initToolBar(self):
        #image processing 
        self.toolBar = QtGui.QToolBar()
        self.toolBar.setFixedSize(50, 800)
      
        self.toolBar.setOrientation(Qt.Vertical)
        #
        self.addToolBar(Qt.LeftToolBarArea,self.toolBar)
        
        
        exitAction = QtGui.QAction(QtGui.QIcon('./image/exit.png'), ' Exit ', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)


        conDBAction=QtGui.QAction(QtGui.QIcon('./image/connectDB.png'), 'Connect with DataBase', self)
        conDBAction.setShortcut('Command+D')
        conDBAction.setStatusTip('Connect to DataBase')
        conDBAction.triggered.connect(self.connectDBlog)
        
        
        queryAction=QtGui.QAction(QtGui.QIcon('./image/standardQuery.png'), 'SQL Query about Data', self)
        queryAction.setStatusTip('standardQuery')
        queryAction.triggered.connect(self.queryMode)
        
        
        
        #add annotation Icon 
        self.addAnnoAction=QtGui.QAction(QtGui.QIcon('./image/addAnnotation.png'), 'Attach Annotation to Selected Tuples', self)
        self.addAnnoAction.setStatusTip('Attach Annotation to Selected Tuples')
        self.addAnnoAction.triggered.connect(self.addAnnotation)
        
        
        #standard Propagation
        anQueryAction=QtGui.QAction(QtGui.QIcon('./image/annotationPropagation.png'), 'SQL Query about Data with Annotation', self)
        anQueryAction.setStatusTip('SQL Query about Data with Annotation')
        anQueryAction.triggered.connect(self.queryAnnoMode)
        
        #summary_aware Propagation
        sanQueryAction=QtGui.QAction(QtGui.QIcon('./image/summary.png'), 'SQL Query about Data with Annotation Summary', self)
        sanQueryAction.setStatusTip('Query with annotation summary')
        sanQueryAction.triggered.connect(self.querySummaryMode)
        
        #Link_in summary instance with current table 
        linkAction=QtGui.QAction(QtGui.QIcon('./image/link.png'), 'Link Summary Methods to Given Tables', self)
        linkAction.setStatusTip('Link Summary Methods to Given Tables')
        linkAction.triggered.connect(self.linkSummaryMethod)
        
        
        
        
        
        
        self.toolBar.addAction(conDBAction)
        self.toolBar.addAction(self.addAnnoAction)
        self.toolBar.addAction(queryAction)
        self.toolBar.addAction(anQueryAction)
        self.toolBar.addAction(sanQueryAction)
        self.toolBar.addAction(linkAction)

        self.toolBar.addAction(exitAction)
        
        #return toolbar

    def styleWidget(self):
        #self.setStyleSheet("background-color:white;");
        with open("./stypleSheet/demoRed.css",'r') as f:
            tema=f.read()

        #print "loading stypleSheet"
        #print tema
        self.setStyleSheet(tema)


    def initUI(self):   
        self.resize(800,1024)
        self.setWindowTitle("InsightNoteGate Demostration")

        self.initToolBar()
        self.initCentralWidget()
        self.styleWidget()

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
        #print "exe:",setPModeQuery
        
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
       
        #print colnames
        
        m=0
        # [,tuple_id,td_sr]
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
            #annos=ProAnnos(str(row[-1])).annos
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
       
        #print colnames
        
        m=0
        #set colnames
        for c in colnames[:-2]:
            newitem=QtGui.QTableWidgetItem(c)
            self.tableWidget.setHorizontalHeaderItem(m,newitem)
            m+=1
        #
        anSummaryCol=QtGui.QTableWidgetItem("Annotation Summary")
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
    
    def executeInputQuery(self,query):

        print "Exect Input query:{}".format(query);
        
        self.setQueryMode()

        try:
            self.cur.execute(self.sqlQuery)
        except psycopg2.ProgrammingError:
            self.conn.rollback()
            return

    
        rows=self.cur.fetchall()
        
        # set sqlTrans
        self.sqlTrans=SQLTranslater()
        self.sqlTrans.setTableName(self.table_name)
        #
        self.sqlTrans.setRows(rows)
        self.sqlTrans.setDescription(self.cur.description)
        
        if(self.queryMode=="standard"):
            self.showTable(rows)
        if(self.queryMode=="standard-propagation"):
            self.showAnnoTable(rows)
        
        if(self.queryMode=="summary-aware"):
            self.showSummaryAnnoTable(rows)
        

    def executeQuery(self):
        self.executeInputQuery(self.sqlQuery) 
        
    def executeSql(self):
        #setting the filter 
        self.sqlQuery=str(self.sqlInput.text())
        print 
        self.executeQuery()
        
    def addClause(self):
        
        clauseWidget=ClauseWidget()

        clauseWidget.setClause(tableCols[self.table_name],operators)
        count=len(self.clauseWidgets)
        self.ClauseGrid.addWidget(clauseWidget,count,0)
        self.clauseWidgets.append(clauseWidget)
        
    
    def filterClause(self):
        #default sql query  
        sqlQuery="select * from bird;"
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

        self.clauseWidgets=[]


            
        #parse orignal sql query 
        sParser=SQLParser(sqlQuery)
        sParser.extract_where_part()
        sParser.insertWhereClause(whereClauses)
        
        query=sParser.formatSQL()
        #self.sqlQuery=query
        #change the sql query 
        self.sqlInput.setText(query);
        #self.executeInputQuery(query)


        #self.executeQuery()
        
        
    def getExistingSummaryInstance(self):
        """
        using sql query to get existing summary instance attached to given table
        """
        #here we need reset PMode
        self.queryMode="standard"
        self.setQueryMode()
        #here set model
        eSIS={}
        qFormat="select summary_method from summary_catalog where table_name=\'{}\' ;"
        for tn in tableList:
            query=qFormat.format(tn)
            try:
                self.cur.execute(query)
                result=self.cur.fetchall()
                eSIS[tn]=[row[0] for row in result]

            except:
                print "get summary Instnace error"
                print query
                self.conn.rollback()



        #print eSIS

        return eSIS

    def linkSummaryMethod(self):
        #link summary method to given table 
        #GuI and real execution into different part 
        
        eSIS=self.getExistingSummaryInstance()


        lsDialog=linkSummaryDialog(existSumInstance=eSIS)
        lsDialog.exec_()
        siList=lsDialog.getSummaryList()
        tableName=lsDialog.getConfigTableName()

        print "tableNmae:",tableName
        print "original attached summary method:",eSIS[tableName]
        print "attached summary methods:", siList

        solution=SummaryLinkManager(tableName)

        solution.setDefaultSummaryMethods(eSIS[tableName])
        solution.setSummaryMethods(siList)

        try:
            resetQuery=solution.resetCatalogQuery()
            setQuery=solution.setCatalog()
            cutQuery=solution.cutResult()
            insertQuery=solution.insertResult()


            if(resetQuery!=None):
                print resetQuery
                self.cur.execute(resetQuery)
                self.conn.commit()
            if(setQuery!=None):
                print setQuery
                self.cur.execute(setQuery)
                self.conn.commit()
            if(cutQuery!=None):
                print cutQuery
                self.cur.execute(cutQuery)
                self.conn.commit()
            if(insertQuery!=None):
                print insertQuery
                self.cur.execute(insertQuery)
                self.conn.commit()

            #self.conn.commit()
        except psycopg2.ProgrammingError:
            #print "rool back"
            self.conn.rollback()
        




def main():
    
    app = QtGui.QApplication(sys.argv)
    #set application setstyle 
    app.setStyle("plastique") 
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
