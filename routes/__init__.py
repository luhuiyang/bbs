from flask import (
    session,
    redirect,
)

from models.user import User


def current_user():
    uid = session.get('user_id', '')
    u = User.find_by(id=uid)
    return u


def login_required(function):
    def func():
        u = current_user()
        # log('登录鉴定, user', u)
        if u is None:
            # 没登录 不让看 重定向到 /login
            return redirect('/')
        else:
            # 登录了, 正常返回路由函数响应
            return function()

    return func
