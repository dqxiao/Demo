import sqlparse
from sqlparse.tokens import Keyword, DML 
import re 

class SQLParser:
    
    def __init__(self,rawQuery):
        self.rawQuery=rawQuery.rstrip(";")
        self.parsed=sqlparse.parse(rawQuery)
        self.bWhere=None
        self.whereClause=None
        self.aWhere=None
    
    
    def extract_where_part(self):
        #for paring query into different part 
        stmt=self.parsed[0]
        whereEx="where (.*)"
        sortEx="order by "
        wherePattern=re.compile(whereEx)
        whereIndex=None
        whereEnd=None
        index=0
        for item in stmt.tokens:
              
              if wherePattern.match(item.value):
                  if whereIndex==None:
                      whereIndex=index
              else:
                  if item.ttype is Keyword and item.value.upper()=="ORDER":
                      whereEnd=index
              index+=1
        
        #
        if(whereIndex==None and whereEnd==None):
            self.bWhere=self.rawQuery
            return
        
        if(whereIndex!=None):
            
            self.bWhere=" ".join([stmt.tokens[i].value for i in xrange(whereIndex)])
            #print stmt.tokens[whereIndex].value
            match=wherePattern.match(stmt.tokens[whereIndex].value)
            self.whereClause=match.groups()[0]
            self.aWhere=" ".join([stmt.tokens[i].value for i in xrange(whereIndex+1,len(stmt.tokens))])
            return 
        
        if(whereIndex==None and whereEnd!=None):
            self.bWhere=" ".join([stmt.tokens[i].value for i in xrange(whereEnd)]);
            self.aWhere=" ".join([stmt.tokens[i].value for i in xrange(whereEnd,len(stmt.tokens))])
            return
            #
        
        
    
    def debug(self):
        
        print "bWhere:{}".format(self.bWhere)
        if self.whereClause==None:
            print "no where clause"
        else:
            print "where:{}".format(self.whereClause)
        
        print "aWhere:{}".format(self.aWhere)
        
    def insertWhereClause(self,whereClauseList):
        if len(whereClauseList)==0:
            return 
             
        addWhere=" and ".join(whereClauseList)
        # if self.whereClause==None:
   #          self.whereClause=addWhere
   #      else:
   #          self.whereClause+=" and "
   #          self.whereClause+=addWhere
        
        self.whereClause=addWhere
    
    def formatSQL(self):
        result=""
        result+=self.bWhere
        if self.whereClause!=None:
            result+=" where "
            result+=self.whereClause
        if self.aWhere!=None:
            result+=" "
            result+=self.aWhere
        
        return result 
        



if __name__=="__main__":
    #three simple test case 
    #query="select * from test";
    #query="select * from test where id=1"
    query="select * from test order by id"
    sParser=SQLParser(query)
    sParser.extract_where_part()
    #sParser.debug()
    sParser.insertWhereClause(["content='me","id<=2"])
    
    print sParser.formatSQL()
    #sParser.debug()
        
        
        
                
        
        
                
                
                
                
            
            
            
        