tableList=["bird","test"] 
siList=[
    ('classifier_1','NB','Use Naive Bayes Classification method to classify annotation into Postive and Negative categories'),
    ('classifier_2','SVM','Use Suppor Vector Model Classification method to classify annotation into differnt categories: Evolution, Habit, Observation'),
    ('cluster_1','KMEANS','Use K-Means method for clustering annotation'),
    ('cluster_2','Gaussian mixtures','Use Gaussian method for clustering annotation'),
    ('snippet_1','LDA','Use LDA method to generate snippet for long annotation '),
    ('snippet_2','Text Rank','Use Text Rank method to generate snippet for long annotation ')
]

tableCols={
	"bird":["id","name","country","description","habit"],
	"test":["id","content"]
}

operators=["=","!=",">",">=","<","<="]
