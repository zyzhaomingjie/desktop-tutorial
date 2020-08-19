import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
import seaborn as sns 

df=pd.DataFrame(datasets.load_iris()['data'],columns=datasets.load_iris()['feature_names']) 

iris = datasets.load_iris() 
X = iris.data[:, :4] ##表示我们取特征空间中的4个维度

kmeans = KMeans(n_clusters=3).fit(X)

kmeans.cluster_centers_###类均值


y = kmeans.predict(X)

sns.scatterplot(X[:,0],X[:,2],hue=y)
