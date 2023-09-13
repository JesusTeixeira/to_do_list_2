import json
from flask import render_template, Blueprint, request, redirect, url_for

from database.models import Todo
from database.database import Database, select

bp = Blueprint("todo", __name__, template_folder="templates")


@bp.route("/")
def home():
    query = select(Todo)
    todo_list = Database().get_all(query)
    return render_template("base.html", todo_list=todo_list)


@bp.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        task = Todo(
            name=request.form["name"],
        )

        Database().run_insert(task)
        return redirect("/")


@bp.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):
    query = select(Todo).where(Todo.task_id == task_id)
    task: Todo = Database().get_one(query)

    if data := request.form:
        task.name = data["name"]
        Database().run_insert(task)
        return redirect("/")

    return render_template("edit.html", todo=task)


@bp.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    if request.method == "POST":
        query = select(Todo).where(Todo.task_id == task_id)
        task = Database().get_one(query)
        Database().run_delete(task)
    return redirect("/")


# rotas da pagina
