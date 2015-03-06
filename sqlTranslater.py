class SQLTranslater:
    
    
    def __init__(self):
        
        self.conn=True
        
    
    def setTableName(self,tableName):
        self.tableName=tableName
        
    def setDescription(self,description):
        
        self.desc=description
        self.colNames=[item[0] for item in self.desc]
        
    def setRows(self,rows):
        self.rows=rows
    
    
    def colIndexToFields(self,colIndex):
        selectColumns=[self.colNames[i] for i in xrange(colIndex[0],colIndex[1]+1)]
        return selectColumns
    
    
    def translateInterval(self,interval):
        
        if(interval[0]==interval[1]):
            return "id={}".format(interval[0])
        else:
            return "id>={} and id<={}".format(interval[0],interval[1])
        
    
    def tableIndexToRow(self,rowIndex):
        
        selectRowIds=[self.rows[i][0] for i in xrange(rowIndex[0],rowIndex[1]+1)]
        
        #selectRowIds=[1,7,8,9,11,12]
        comIds=[]
        
        
        
        comIds.append([selectRowIds[0],selectRowIds[0]])
        for item in selectRowIds:
            if item==comIds[-1][1]:
                continue
            if item==comIds[-1][1]+1:
                comIds[-1][1]+=1
            else:
                comIds.append([item,item])
        
        # for cItem in comIds:
#             print cItem

        comQuery=[self.translateInterval(item) for item in comIds]
        
        return comQuery
    
    
    def tranSelectQuery(self,rowIndex,colIndex):
        #input: 
        #      colIndex in tableView [2,6]
        #      rowIndex in tableView [1,2]
        #      continues 
        queryFormat="select {} from {} where {}"
        
        
        fields=",".join(self.colIndexToFields(colIndex))
        condition=" or ".join(self.tableIndexToRow(rowIndex))
        
        
        query=queryFormat.format(fields,self.tableName,condition)
        
        return query
        
        
        #



if __name__=="__main__":
    
    sqlTrans=SQLTranslater("test")
    
    sqlTrans.tableIndexToRow([1,2])    
        
        
        
        
        