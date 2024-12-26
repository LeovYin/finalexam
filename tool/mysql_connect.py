import pymysql

# 建立数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password="776868312",
                       database='waterconserbancyproject', charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)


def mysql_connect(sql_code):
    try:
        conn.ping(reconnect=True)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_code)
        if sql_code.strip().lower().startswith("select"):
            result = cursor.fetchall()
            return result
        else:
            conn.commit()
            return cursor.rowcount  # 返回影响的行数
    except pymysql.MySQLError as e:
        conn.rollback()
        return type(e), e
    finally:
        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接
