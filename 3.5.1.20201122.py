import pandas as pd

s = pd.Series(['丁一', '王二', '张三'])
print(s)

a = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
print(a)

b = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['A', 'B', 'C'])
print(b)

c = pd.DataFrame()
data = [1, 3, 5]
score = [2, 4, 6]
c['data'] = data
c['score'] = score
print(c)