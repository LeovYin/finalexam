import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump, load

# 加载数据
file_path = '../../dataset/sjj.csv'
data = pd.read_csv(file_path)

# 定义特征和目标变量
features = ['level', 'traffic', 'flow_rate', 'water_temperature', 'number']
output_feature = 'number'  # 假设我们预测 'number'

# 分离输入特征和目标变量
input_features = [f for f in features if f != output_feature]
X = data[input_features]
y = data[[output_feature]]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 标准化数据
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 创建一个更复杂的MLP模型
complex_model = MLPRegressor(
    hidden_layer_sizes=(100, 100, 50, 25,),
    max_iter=1000,
    random_state=42,
    activation='relu',  # 可以尝试不同的激活函数
    solver='adam',  # 使用自适应学习率算法
    alpha=0.001,  # L2 正则化参数
    early_stopping=True,  # 启用早停
    n_iter_no_change=10  # 如果10次迭代没有改善，则停止训练
)

complex_model.fit(X_train_scaled, y_train.values.ravel())

# 保存训练过程中的损失值
complex_history = complex_model.loss_curve_

# 假设我们有以下输入数据
input_data = [[164.48, 11000, 2.035, 22.59]]  # 需要预测number

# 使用之前相同的标准化器对输入数据进行标准化
input_data_scaled = scaler.transform(input_data)

# 使用复杂模型进行预测
predicted_number_complex = complex_model.predict(input_data_scaled)

# 计算测试集上的损失值
y_pred_complex = complex_model.predict(X_test_scaled)
complex_loss = mean_squared_error(y_test, y_pred_complex)

# 输出预测值和损失值
print(f"Predicted number: {predicted_number_complex[0]}")
print(f"Loss (MSE) on test set: {complex_loss}")
print(f"Training loss history: {complex_history}")

# 训练模型并保存
complex_model.fit(X_train_scaled, y_train.values.ravel())
dump(complex_model, 'complex_model.joblib')  # 保存模型
dump(scaler, 'scaler.joblib')  # 保存标准化器


# 创建一个函数来加载模型并进行预测
def predict_number(level, traffic, flow_rate, water_temperature):
    # 加载模型和标准化器
    model = load('complex_model.joblib')
    scaler = load('scaler.joblib')

    # 将输入数据标准化
    input_data = [[level, traffic, flow_rate, water_temperature]]
    input_data_scaled = scaler.transform(input_data)

    # 使用模型进行预测
    predicted_number = model.predict(input_data_scaled)

    return predicted_number[0]


# 使用函数进行预测
predicted_value = predict_number(164.48, 11000, 2.035, 22.59)
print(f"Predicted number: {predicted_value}")
