import json

from flask import Flask, render_template, request, redirect, url_for, flash
from service.all_service import *
from math import ceil

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于会话和闪现消息


@app.route('/')
def index():
    return render_template('login.html', failure=False)


@app.route('/register')
def indexRegister():
    return render_template('register.html')


def check_credentials(username, password):
    user = get_user(username, password)
    return user is not None


@app.route('/login')
def indexLogin():
    return render_template('login.html', failure=False)


@app.route('/login', methods=['post'])
def login():
    username = request.form['username']
    password = request.form['password']
    if check_credentials(username, password):
        # 登录成功，重定向到首页或其他页面
        return redirect(url_for('indexPart2'))
    else:
        # 登录失败，显示错误消息
        return render_template('login.html', failure=True)


water_list = get_water()
totalYear = getTotalYear()

day = get_day()
number = get_number()
level = get_water_level()


@app.route('/part2')
def indexPart2():
    return render_template('part2.html', water_list=water_list, totalYear=totalYear, day=day,
                           number=number, level=level)

@app.route('/part1')
def indexPart1():
    return render_template('part1.html')

@app.route('/part3')
def indexPart3():
    # 获取分页参数
    page = request.args.get('page', 1, type=int)
    pageSize = 15  # 每页显示的数据条数
    totalPage = ceil(len(water_list) / pageSize)  # 总页数
    return render_template('part3.html', water_list=water_list)

@app.route('/register', methods=['post', 'GET'])
def register():
    register_failure = False

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if get_user_by_username(username) is None:
            user = {'username': username, 'password': password}
            insert_user(user)
            return redirect(url_for('login'))
        else:
            register_failure = True
            flash('注册失败！', 'error')
            return render_template('register.html', register_failure=register_failure)


if __name__ == '__main__':
    app.run(debug=True)
