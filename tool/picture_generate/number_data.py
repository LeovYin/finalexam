
import csv
import matplotlib.pyplot as plt
import os

# 设置文件路径
file_path = r"D:\Downloads\water.csv"
save_path = '../picture/number_data chart/number_data.png'

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"File not found at path: {file_path}")
else:
    # 设置 matplotlib 支持中文显示
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 初始化字典来存储每年的数据
    data_by_year = {}

    # 读取 CSV 文件
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = row['year']
            date = row['date']
            number = row['number']

            # 检查 'number' 是否为空
            if number:
                number = float(number)

                # 将数据按年份分类存储
                if year not in data_by_year:
                    data_by_year[year] = []
                data_by_year[year].append((date, number))

    # 为每一年绘制 number 随 date 变化的二维折线图
    for year, data in data_by_year.items():
        dates = [d[0] for d in data]
        numbers = [d[1] for d in data]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, numbers, marker='o', label=f'Year {year}')

        plt.title(f'鱼卵数量随时间变化图 {year}')
        plt.xlabel('日期')
        plt.ylabel('鱼卵数量 (个)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        # 设置 x 轴坐标刻度倾斜 45°
        plt.xticks(rotation=45)
        # 保存图表到指定路径
        plt.savefig(save_path.replace('.png', f'_{year}.png'))
        plt.close()  # 关闭图表以避免重复绘制
