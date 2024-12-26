import pandas as pd
import matplotlib.pyplot as plt

# 获取用户输入的中文名称作为文件名（这里示例直接赋值为"饼状图"，也可改成input获取输入）
file_name = "鱼苗漂浮情况饼状图"

# 读取CSV文件
data = pd.read_csv(r"dataset/sjj.csv")

# 去除包含空值的行
data = data.dropna()

# 定义新的区间划分规则和对应的标签
bins = [0, 1, 20, 40, 60, 80, 100, 500, float('inf')]
labels = ['0', '1-20', '20-40', '40-60', '60-80', '80-100', '100-500', '500以上']

# 使用cut函数对number列进行区间划分
data['number_interval'] = pd.cut(data['number'], bins=bins, labels=labels)

# 统计各区间出现的频次
number_counts = data['number_interval'].value_counts()

# 设置饼状图的颜色
colors = plt.cm.Paired(range(len(number_counts)))

# 设置图像的大小
plt.figure(figsize=(9,5))  # 调整图像的宽度和高度

# 绘制饼状图，添加阴影效果和爆炸效果
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # 将第一个扇区（最大值）略微突出
wedges, texts, autotexts = plt.pie(
    number_counts,
    labels=number_counts.index,
    autopct='%1.1f%%',
    startangle=200,  # 设置开始角度，使图表更美观
    shadow=True,    # 添加阴影效果
    explode=explode, # 突出显示第一个扇区
    colors=colors,   # 设置颜色
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.6}  # 设置扇区的边界线
)

# 设置标题字体颜色为蓝色
plt.title("鱼卵漂浮数量占比图", color='blue', fontsize=16)

# 添加图例，设置字体颜色为蓝色，并将图例位置放到左侧
plt.legend(
    wedges,
    number_counts.index,
    title="区间",
    loc="center left",
    bbox_to_anchor=(-0.2, 0, 0.5, 1),
    fontsize=12,
    title_fontsize='13',
    frameon=False
)

# 设置字体颜色为蓝色
plt.rcParams['text.color'] = 'blue'
plt.rcParams['axes.labelcolor'] = 'blue'  # 确保标签颜色为蓝色
plt.rcParams['xtick.color'] = 'blue'  # 设置x轴刻度颜色
plt.rcParams['ytick.color'] = 'blue'  # 设置y轴刻度颜色

# 绘制等比
plt.axis('equal')

# 使 matplotlib 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 保存图片，文件名使用包含中文的名称（注意确保运行环境支持中文路径存储等情况）
plt.savefig(f"{file_name}.png", bbox_inches='tight')  # 使用'bbox_inches'确保图片不被裁切
plt.show()