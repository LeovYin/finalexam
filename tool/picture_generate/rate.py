import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 文件路径（替换为你的实际文件路径）
file_path = r"D:\xxtzl\water.csv"  # 替换为你的文件路径
output_path = r"D:\PythonProject\rate "  # 保存图片的路径

# 尝试读取数据集
try:
    # 读取数据
    data = pd.read_csv(file_path)

    # 检查数据是否加载成功
    print("数据加载成功！以下是前5行数据：")
    print(data.head())

    # 为了分析方便，重命名表头
    data.columns = ['编号', '年份', '日期', '水位', '流量', '流速', '水温', '漂浮鱼卵数']

    # 删除水位和漂浮鱼卵数为空的数据
    data = data.dropna(subset=['流速', '漂浮鱼卵数'])

    # 过滤漂浮鱼卵数大于 1000 的数据
    data = data[data['漂浮鱼卵数'] <= 1000]

    # 按年份分组并制作每年图表
    for year in data['年份'].unique():
        year_data = data[data['年份'] == year]

        # 设置 matplotlib 支持中文
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为 SimHei
        plt.rcParams['axes.unicode_minus'] = False  # 防止负号无法显示

        # 绘制每年的水位对漂浮鱼卵数量的影响散点图并保存
        plt.figure(figsize=(10, 6))
        sns.regplot(
            x='流速',
            y='漂浮鱼卵数',
            data=year_data,
            scatter_kws={'color': 'blue', 's': 30, 'label': '数据点'},
            line_kws={'color': 'red', 'label': '回归线'},
            ci=None
        )
        plt.title(f"{year} 流速对漂浮鱼卵数量的影响", fontsize=16, color='blue')
        plt.xlabel("流速 (m)", fontsize=12)
        plt.ylabel("漂浮鱼卵数", fontsize=12)
        plt.ylim(0, 800)  # 限制纵坐标范围
        plt.legend(fontsize=12)
        plt.grid(alpha=0.3)
        plt.savefig(f"{output_path}\\{year}_流速影响图.png", bbox_inches='tight')  # 保存为PNG文件
        plt.close()

    print("图表已生成并保存。")

except Exception as e:
    print(f"加载数据失败，错误信息：{e}")