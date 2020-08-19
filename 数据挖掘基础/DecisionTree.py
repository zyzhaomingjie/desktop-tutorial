from sklearn import tree
from matplotlib import pyplot as plt
from sklearn import datasets

# 导入数据
X,y=datasets.load_iris(return_X_y=True) # X与y
target_names=datasets.load_iris().target_names # y的值列表:0:setosa,1:versicolor,2:virginica
feature_names=datasets.load_iris().feature_names # 特征X的名称列表

# 构建深度为3的决策树模型
clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X, y)

# 给出把未知样本预测为哪一类
clf.predict([[6,1,3,1]]) 

# 给出把未知样本预测为每一类的概率
clf.predict_proba([[6,1,3,1]])  

# 可视化决策树
plt.figure(figsize=(10,5))
tree.plot_tree(clf) 

# 解释：
# 从可视化的决策树中可以直观清晰的看出，决策树的第一层以petal width是否小于等于0.8
# 作为分裂标准，其中左子树的样本全为setosa，且基尼系数为0，纯度达到最优；
# 因此可以认为，当petal width小于等于0.8时，最可能为setosa花。
￼


