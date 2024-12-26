import json

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from service.all_service import *
from math import ceil
from flask_paginate import Pagination, get_page_args

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
traffic = get_traffic()
temperature = get_temperature()
flow = get_water_flow()


@app.route('/part2')
def indexPart2():
    return render_template('part2.html', water_list=water_list, totalYear=totalYear, day=day,
                           number=number, level=level, traffic=traffic, temperature=temperature, flow=flow)


@app.route('/part1')
def indexPart1():
    return render_template('part1.html')


def get_paginated_data(data, page, per_page):
    offset = (page - 1) * per_page
    return data[offset: offset + per_page]


@app.route('/part3')
def indexPart3():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    per_page = 15
    total = len(water_list)
    pagination_water_list = water_list[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('part3.html', water_list=pagination_water_list, pagination=pagination)


# 分页路由
@app.route('/paginate', methods=['GET'])
def paginate():
    page = request.args.get('page', 1, type=int)
    pageSize = 15
    start = (page - 1) * pageSize
    end = start + pageSize
    data = water_list[start:end]
    total = len(water_list)
    return jsonify({'data': data, 'total': total})


# 搜索路由
@app.route('/search', methods=['GET'])
def search():
    year = request.args.get('year', '')
    filtered_data = [item for item in water_list if item['year'] == year]
    total = len(filtered_data)
    return jsonify({'data': filtered_data, 'total': total})


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
