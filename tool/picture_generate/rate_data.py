import csv
import matplotlib.pyplot as plt
import os

# 设置文件路径
file_path = r"D:\Downloads\water.csv"
save_path = '../picture/flowrate_data chart/water_temperature.png'

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"File not found at path: {file_path}")
else:
    # 设置 matplotlib 使用支持中文的字体
    plt.rcParams['font.sans-serif'] = ['SimSun']  # 使用 'SimSun' 字体
    plt.rcParams['axes.unicode_minus'] = False  # 确保负号显示正常

    # ... 其余的绘图代码 ...

    # 初始化字典来存储每年的数据
    data_by_year = {}

    # 读取 CSV 文件
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = row['year']
            date = row['date']
            flow_rate= row['flow_rate']

            # 检查 'flow_rate' 是否为空
            if flow_rate:
                flow_rate = float(flow_rate)

                # 将数据按年份分类存储
                if year not in data_by_year:
                    data_by_year[year] = []
                data_by_year[year].append((date, flow_rate))

    # 为每一年绘制 water_temperature 随 date 变化的二维折线图
    for year, data in data_by_year.items():
        dates = [d[0] for d in data]
        flow_rates = [d[1] for d in data]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, flow_rates, marker='o', label=f'Year {year}')

        plt.title(f'流速随时间变化图 {year}')
        plt.xlabel('日期')
        plt.ylabel('流速 (m³/s)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        # 设置 x 轴坐标刻度倾斜 45°
        plt.xticks(rotation=45)
        # 保存图表到指定路径
        plt.savefig(save_path.replace('.png', f'_{year}.png'))
        plt.close()  # 关闭图表以避免重复绘制