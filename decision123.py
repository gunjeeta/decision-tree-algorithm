from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
f=[[120,0],[150,0],[80,1],[100,1]]
l=['apple','apple','orange','orange']
clf=DecisionTreeClassifier()
clf1=GaussianNB()
trained=clf.fit(f,l)
trained1=clf1.fit(f,l)
####training data
res=trained.predict([[120,0],[100,1],[180,0],[120,1]])
res1=trained1.predict([[120,0],[100,1],[180,0],[120,1]])
print(res)
print(res1)

###no change in gaussian therefore likeliness of answer is more stable in gaussian
