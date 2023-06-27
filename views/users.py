from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import render_template
from models import db, Users

users_app = Blueprint(
    "users_app",
    __name__,
    url_prefix="/users",
)


@users_app.get("/", endpoint="list")
def get_users_list():
    users: list[Users] = Users.query.order_by(Users.id).all()
    return render_template("users/list.html", users=users)


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_user():
    if request.method == "GET":
        return render_template("users/add.html")

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    gender = request.form.get('gender')
    user = Users(firstname=firstname, lastname=lastname, email=email, gender=gender)
    db.session.add(user)
    db.session.commit()
    url = url_for("users_app.list")
    return redirect(url)



