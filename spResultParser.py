class Annotation:
    
    def __init__(self,inputStr):
        self.presentation={}
        self.parse(inputStr)
        
    def parse(self,inputStr):
        
        inputSplits=inputStr.split("--")
        #inputparsers=[item.split(":") for item in inputSplits]
        
        for item in inputSplits:
            inputParsers=item.split(":")
            attr=inputParsers[0]
            val="".join(inputParsers[1:])
            
            self.presentation[attr]=val
    
    def description(self):
        #all represetation need to show 
        return ["id","author","timestamp","value"]
    
    def rawRows(self):
        
        return [self.presentation[item] for item in self.description()]
        
        
    def labelPre(self):
        
        result=""
        for attr in self.description():
            result+=str(attr)+":"
            result+=self.presentation[attr]
            result+="\n"
        
        return result
        
        


class ProAnnos:
    
    def __init__(self,inputStr):
        self.annos=[]
        self.parse(inputStr)
        
    def parse(self,inputStr):
        if(inputStr==None):
            return 
        
        inputSplits=inputStr.split("||")
        for item in inputSplits:
            newAnno=Annotation(item)
            self.annos.append(newAnno)
    
    def numOfAnno(self):
        return len(self.annos)
    
    def isEmpty(self):
        return self.numOfAnno==0
    
    


if __name__=="__main__":
    
    inputStr="id:14--author:unkown--timestamp:00:00:00--value:this is one test --table_name:test--tuple_id:1--tuple_columns:1,2||id:15--author:unkown--timestamp:00:00:00--value:this is third annotation --table_name:test--tuple_id:1--tuple_columns:1,2"
    
    proAnnos=ProAnnos(inputStr)
    
    for anno in proAnnos.annos:
        print anno.rawRows()
    