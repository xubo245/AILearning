import sys
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd


def main(argv):
  print("hello")

  # 读取表格
  data = xlrd.open_workbook("developers.xlsx")

  # 获取表格的sheets
  table = data.sheets()[0]

  # 输出行数量
  print(table.nrows)  # 8

  # 输出列数量
  print(table.ncols)  # 4

  # 获取第一行数据
  row1data = table.row_values(0)
  print(row1data)  # ['列1', '列2', '列3', '列4']
  print(row1data[0])  # 列1

  from pyecharts.charts import Bar

  # 读取表格
  # data = xlrd.open_workbook("developers.xlsx")

  # 获取表格的sheets
  table = data.sheets()[0]

  # 输出行数量
  print(table.nrows)

  # 输出列数量
  print(table.ncols)

  # 获取第一行数据
  row1data = table.row_values(0)
  print(row1data)  # ['列1', '列2', '列3', '列4']
  print(row1data[0])  # 列1

  xdata = []
  ydata = []
  for i in range(1, table.nrows):
    print(table.row_values(i))
    xdata.append(table.row_values(i)[0])
    ydata.append(table.row_values(i)[1])

  print(xdata)
  print(ydata)

  # 数据可视化，柱状图
  bar = Bar()
  bar.add_xaxis(xdata)
  bar.add_yaxis("名称1", ydata)
  bar.render("show.html")

  plt.bar(xdata, ydata)
  x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
  y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
  plt.plot(x, y)
  plt.show()

  a = np.random.randn(100)
  s = pd.Series(a)
  plt.hist(s)
  plt.show()

  x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
  y = [5, 4, 8, 12, 7]
  plt.bar(x, y)
  plt.show()

  x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
  y = [5, 4, 8, 12, 7]
  plt.barh(x, y)
  plt.show()

  nums = [25, 37, 33, 37, 6]
  labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Others']
  plt.pie(x=nums, labels=labels)
  plt.show()

  # 生成0-1之间的10*4维度数据
  data = np.random.normal(size=(10, 4))
  lables = ['A', 'B', 'C', 'D']
  # 用Matplotlib画箱线图
  plt.boxplot(data, labels=lables)
  plt.show()

  # flights = sns.load_dataset("flights")
  # data = flights.pivot('year', 'month', 'passengers')
  # sns.heatmap(data)
  # plt.show()

  N = 1000
  x = np.random.randn(N)
  y = np.random.randn(N)

  plt.scatter(x, y, marker='x')
  plt.show()

  N = 10000
  x = np.random.randn(N)
  y = np.random.randn(N)

  plt.scatter(x, y, marker='x')
  plt.show()

  labels = np.array([u"推进", "KDA", u"生存", u"团战", u"发育", u"输出"])
  stats = [83, 61, 95, 67, 76, 88]
  # 画图数据准备，角度、状态值
  angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
  stats = np.concatenate((stats, [stats[0]]))
  angles = np.concatenate((angles, [angles[0]]))
  # 用Matplotlib画蜘蛛图
  fig = plt.figure()
  ax = fig.add_subplot(111, polar=True)
  ax.plot(angles, stats, 'o-', linewidth=2)
  ax.fill(angles, stats, alpha=0.25)
  # 设置中文字体
  # font = FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc", size=14)
  # ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties=font)
  plt.show()

  # tips = sns.load_dataset("tips")
  # tips.head(10)
  # # 散点图
  # sns.jointplot(x="total_bill", y="tip", data=tips, kind='scatter')
  #
  # # Hexbin图
  # sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
  # plt.show()

  df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=['a', 'b', 'c', 'd'])

  # 堆面积图
  df.plot.area()

  # 面积图
  df.plot.area(stacked=False)

  df = pd.DataFrame(
    np.random.randn(1000, 2),
    columns=['a', 'b'])
  df['b'] = df['b'] + np.arange(1000)

  # 关键字参数gridsize；它控制x方向上的六边形数量，默认为100，较大的gridsize意味着更多，更小的bin
  df.plot.hexbin(x='a', y='b', gridsize=25)

  print("end")

if __name__ == '__main__':
    # If user want to test OBS, please input OBS path, ak, sk and endpoint.
    main(sys.argv)
    print("Success")
