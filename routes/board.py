from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)


@main.route("/admin")
def index():
    u = current_user()
    if u.role != 1:
        return redirect(url_for('topic.index'))
    bs = Board.all()
    return render_template('board/admin_index.html', bs=bs)
    ...


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    if u.role == 1:
        m = Board.new(form)
    return redirect(url_for('topic.index'))


@main.route("/delete")
def delete():
    id = int(request.args.get('board_id'))
    u = current_user()
    # 判断 token 是否是我们给的
    if u.role == 1:
        print('删除 board 用户是', u, id)
        Board.delete(id)
        return redirect(url_for('topic.index'))
    else:
        abort(404)
