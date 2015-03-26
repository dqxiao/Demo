class SummaryLinkManager:

	def __init__(self,tableName):
		self.tableName=tableName
		self.catalogResetFormat="delete from summary_catalog where table_name=\'{}\'"
		self.catalogInsertFormat="insert into summary_catalog(table_name,summary_method) values {}"
		self.fiterSummaryResult="delete from summary_result where {}"
		self.insertSummaryResult="insert into summary_result(id,summary_method,result) (select id,summary_method,result from clone_summary_result where {})"

	def resetCatalogQuery(self):
		query=self.catalogResetFormat.format(self.tableName)

		return query 

	def setDefaultSummaryMethods(self,siList):
		self.defaultSummaryMethods=siList

	def setSummaryMethods(self,siList):
		#
		siList=[item.split("\n")[0] for item in siList]
		self.summaryMethods=siList


	def setCatalog(self):

		valuesFormat="(\'{}\',\'{}\')"
		values=[]
		for item in self.summaryMethods:
			values.append(valuesFormat.format(self.tableName,item))

		query=self.catalogInsertFormat.format(",".join(values))

		return query 

	def cutResult(self):

		diffSet=set(self.defaultSummaryMethods)-set(self.summaryMethods)


		filterFormat="summary_method=\'{}\'"
		filters=[]

		for item in diffSet:
			filters.append(filterFormat.format(item))

		#query=self.filterFormat(self.tableName,"")
		if(filters==[]):
			return None
		else:
			query=self.fiterSummaryResult.format(" or ".join(filters))
			return query 


	def insertResult(self):

		diffSet=set(self.summaryMethods)-set(self.defaultSummaryMethods)

		adds=[]
		addFormat="summary_method=\'{}\'"
		for item in diffSet:
			adds.append(addFormat.format(item))

		if(adds==[]):
			return None
		else:
			query=self.insertSummaryResult.format(" or ".join(adds))
			return query 



if __name__=="__main__":

	solution=SummaryLinkManager("bird")

	solution.setDefaultSummaryMethods(["classifier_1","classifier_2"])
	solution.setSummaryMethods(["classifier_1","cluster_1","snippet_1"])


	print solution.resetCatalogQuery()
	print solution.setCatalog()

	print "cut result"
	print solution.cutResult()

	print solution.insertResult()







		





