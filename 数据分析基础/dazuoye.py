import pandas as pd

tags = pd.read_csv('tags.csv')
ratings = pd.read_csv('ratings.csv')
links = pd.read_csv('links.csv')
movies = pd.read_csv('movies.csv')
gtags = pd.read_csv('gtags.csv')
scores = pd.read_csv('scores.csv')


#1一共有多少不同的用户
a = tags['userId'].drop_duplicates()
b = ratings['userId'].drop_duplicates()
c = a.append(b)
result1 = len(c.drop_duplicates())


#2一共有多少不同的电影
a = tags['movieId'].drop_duplicates()
b = ratings['movieId'].drop_duplicates().append(a)
c = movies['movieId'].drop_duplicates().append(b)
d = links['movieId'].drop_duplicates().append(c)
e = scores['movieId'].drop_duplicates().append(d)
result2 = len(e.drop_duplicates())


#3一共有多少不同的电影种类
movie_kind = set()
a = movies['genres'].drop_duplicates()
for lists in a.str.split('|'):
    for list in lists:
        movie_kind.add(list)
result3 = len(movie_kind)
    

#4一共有多少电影没有外部链接
a = links['movieId'].drop_duplicates()
result4 = result2 -  len(a.drop_duplicates())


#52018年一共有多少人进行过电影评分
import datetime
ratings['timestamp_1'] = ratings['timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(x))
ratings['year'] = pd.DatetimeIndex(ratings['timestamp_1']).year
df = ratings.query('(year == 2018)')
result5 = len(df['userId'].drop_duplicates())


#62018年评分5分以上的电影及其对应的标签 
df_5 = df[df['rating']>=5]
df_s = df_5[['movieId', 'rating']].drop_duplicates()
tags_s = tags[['movieId', 'tag']].drop_duplicates()
result6 = pd.merge(left=df_s, right=tags_s, on="movieId", how="inner")

 
#7绘制电影复仇者联盟（The Avengers）122912每个月评分的平均值变化曲线图
ratings_122912 = ratings[ratings['movieId'] == 122912].query('(year == 2018)')
ratings_122912['month'] = pd.DatetimeIndex(ratings_122912['timestamp_1']).month
ratings_122912 = ratings_122912[['month', 'rating']].groupby(['month'])['rating'].mean().reset_index()
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10,6))
# 设置绘图风格
plt. style.use("ggplot")
# 设置中文编码和符号的正常显示
plt.rcParams["font.sans-serif"] = "KaiTi"
plt.rcParams["axes.unicode_minus"] = False
plt.plot(ratings_122912.month, # x轴数据
         ratings_122912.rating, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='brown') # 点的填充色
# 添加标题和坐标轴标签
plt.title('复仇者联盟（The Avengers）122912每个月评分的平均值变化曲线图')
plt.xlabel('月份')
plt.ylabel('平均评分')

# 剔除图框上边界和右边界的刻度
plt.tick_params(top = 'off', right = 'off')

# 为了避免x轴日期刻度标签的重叠，设置x轴刻度自动展现，并且45度倾斜
#fig.autofmt_xdate(rotation = 45)

# 显示图形
plt.show()















