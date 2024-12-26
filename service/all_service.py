import pymysql

# 建立数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password="776868312",
                       database='waterconserbancyproject', charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)


def get_user(username, password):
    sql = "SELECT * FROM user WHERE username = %s AND password = %s"
    try:
        conn.ping(reconnect=True)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        return result
    except pymysql.MySQLError as e:
        return type(e), e
    finally:
        cursor.close()


def get_user_by_username(username):
    sql = "SELECT * FROM user WHERE username = %s"
    try:
        conn.ping(reconnect=True)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        return result
    except pymysql.MySQLError as e:
        return type(e), e
    finally:
        cursor.close()


def insert_user(user):
    sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
    try:
        conn.ping(reconnect=True)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, (user['username'], user['password']))
        conn.commit()
        return cursor.rowcount
    except pymysql.MySQLError as e:
        conn.rollback()
        return type(e), e
    finally:
        cursor.close()


def get_water():
    sql = "SELECT * FROM water"
    try:
        conn.ping(reconnect=True)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except pymysql.MySQLError as e:
        return type(e), e
    finally:
        cursor.close()


def search_water(year):
    # 使用 LIKE 语句进行模糊搜索，直接在参数中拼接通配符
    sql = "SELECT * FROM water WHERE year LIKE %s"
    # 在参数中包含通配符
    param = f"%{year}%"
    try:
        conn.ping(reconnect=True)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, (param,))
        result = cursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        return type(e), e
    finally:
        cursor.close()


def getTotalYear():
    alist = get_water()
    count = 1 - (int(alist[0]['year'][:4]) - int(alist[-1]['year'][:4]))
    return count


def get_day():
    water_list = get_water()
    year_twelve = []
    end_index = 6 if len(water_list) > 6 else len(water_list)
    for i in range(end_index):
        year_twelve.append(water_list[-1 - i]['date'])
    return year_twelve


def get_year():
    water_list = get_water()
    year_twelve = []
    end_index = 6 if len(water_list) > 6 else len(water_list)
    for i in range(end_index):
        year_twelve.append(water_list[-1 - i]['year'])
    return year_twelve


def get_number():
    water_list = get_water()
    number = []
    end_index = 6 if len(water_list) > 6 else len(water_list)
    for i in range(end_index):
        number.append(water_list[-1 - i]['number'])
    return number


def get_traffic():
    water_list = get_water()
    traffic = []
    end_index = 6 if len(water_list) > 6 else len(water_list)
    for i in range(end_index):
        traffic.append(water_list[-1 - i]['traffic'])
    return traffic


def get_temperature():
    water_list = get_water()
    temperature = []
    end_index = 6 if len(water_list) > 6 else len(water_list)
    for i in range(end_index):
        temperature.append(water_list[-1 - i]['water_temperature'])
    return temperature


def get_water_level():
    water_list = get_water()
    water_level = []
    end_index = 6 if len(water_list) > 6 else len(water_list)
    for i in range(end_index):
        level = water_list[-1 - i]['level']
        water_level.append(level if level is not None else 0)
    return water_level


def get_water_flow():
    water_list = get_water()
    water_flow = []
    end_index = 6 if len(water_list) > 6 else len(water_list)
    for i in range(end_index):
        water_flow.append(water_list[-1 - i]['flow_rate'])
    return water_flow
print(get_number())