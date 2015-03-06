class AnnoWithSummary:
    
    def __init__(self,inputStr):
        self.presentation={}
        self.summary={}
        self.parse(inputStr)
        self.resParse()
        #self.debugSummary()
        
    def parse(self,inputStr):
        
        inputSplits=inputStr.split("--")
        #inputparsers=[item.split(":") for item in inputSplits]
        
        for item in inputSplits:
            inputParsers=item.split(":")
            attr=inputParsers[0]
            val=":".join(inputParsers[1:])
            
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
    
    
    def resParse(self):
        resStr=self.presentation["resdes"]
        
        resSplits=resStr.split("|")
        #print resSplits
        
        for resSplit in resSplits:
            [name,instance,result]=resSplit.split(":")
            instance=instance.split("-")[0]
            self.summary[instance]=result
    
    def debugSummary(self):
        
        for instance in self.summary:
            print "{}:{}".format(instance,self.summary[instance])
    
    
    def getSummaryInstnaces(self):
        return self.summary.keys()
        


class SummaryInstance:
    
    def __init__(self,instanceName):
        self.name=instanceName
        self.configDesc=["Type","Invariant","Function"]
        self.config={}
        self.result={}
    
    
    def initConifig(self,configList):
        #self.config=configList
        tempConfig=zip(self.configDesc,configList)
        
        for (attr,val) in tempConfig:
            self.config[attr]=val
    
    
    def classifierInc(self,resultTag,anno):
        
        if resultTag in self.result:
            self.result[resultTag].append(anno)
        else:
            self.result[resultTag]=[anno]
        
    
    def incResult(self,resultTag,anno):
        self.classifierInc(resultTag,anno)
        
        
    def debugPresentation(self):
        for attr in self.config:
            print "{}:{}".format(attr,self.config[attr])
        
        for resultTag in self.result:
            print "{}:{}".format(resultTag,len(self.result[resultTag]))
    
    
    def configPresentation(self):
        result=""
        for attr in self.config:
            result+=str(attr)+":"
            result+=self.config[attr]
            result+="\n"
        
        return result
    
    def getResults(self):
        #return [[key,value] for key,value in self.result]
        
        return [[key,self.result[key] ]for key in self.result]
    
    #


class SummaryAnnos:
    
    def __init__(self,inputStr):
        self.annos=[]
        self.parse(inputStr)
        self.instanceConfig()
        
    def parse(self,inputStr):
        if(inputStr==None):
            return 
        
        inputSplits=inputStr.split("||")
        for item in inputSplits:
            newAnno=AnnoWithSummary(item)
            self.annos.append(newAnno)
    
    def numOfAnno(self):
        return len(self.annos)
    
    def isEmpty(self):
        return self.numOfAnno==0
        
    def instanceConfig(self):
        
        self.summaryConfig={}
        self.summaryConfig["classifier_1"]=["classify","t","Naive Bayes"]
        self.summaryConfig["classifier_2"]=["classify","t","SVM"]
        self.summaryConfig["cluster_1"]=["cluster","f","KMEANS"]
        self.summaryConfig["cluster_2"]=["cluster","f","Gaussian mixtures"]
        self.summaryConfig["snippet_1"]=["snippet_1","t","LDA"]
        self.summaryConfig["snippet_2"]=["snippet_2","t","Text Rank"]
        
        
    
    
    def summaryList(self):
        
        #
        #instances=set()
        anno=self.annos[0]
        instances=anno.getSummaryInstnaces()
        
        siList=[]
        for instance in instances:
            si=SummaryInstance(instance)
            si.initConifig(self.summaryConfig[instance])
            siList.append(si)
        
        
        for si in siList:
            for anno in self.annos:
                if si.name in anno.summary:
                    si.incResult(anno.summary[si.name],anno)
        #print instances
        
        # for si in siList:
#             si.debugPresentation()
        return siList
        
        
        



if __name__=="__main__":
    
    inputStr="id:14--author:unkown--timestamp:00:00:00--value:this is one test --table_name:test--tuple_id:1--tuple_columns:1,2--resdes:summary_method:cluster_1-result:0|summary_method:classifier_1-result:T||id:15--author:unkown--timestamp:00:00:00--value:this is third annotation --table_name:test--tuple_id:1--tuple_columns:1,2--resdes:summary_method:classifier_1-result:T||id:16--author:unkown--timestamp:00:00:00--value:this is one test addded annotation. --table_name:test--tuple_id:1--tuple_columns:2--resdes:summary_method:classifier_1-result:T||id:18--author:unkown--timestamp:00:00:00--value:this is one stupid one. --table_name:test--tuple_id:1--tuple_columns:2--resdes:summary_method:classifier_1-result:T"
    
    proAnnos=SummaryAnnos(inputStr)
    
    #proAnnos.summaryList()
    
    # for anno in proAnnos.annos:
#         print anno.rawRows()