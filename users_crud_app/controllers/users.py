from flask import render_template, request, redirect

from users_crud_app import app

# import the class from friend.py
from users_crud_app.models.user import User


@app.route("/user/new")
def user_new():
    # call the get all classmethod to get all friends
    return render_template("createUser.html")


# this localhost :5000/..... if you do ('/<name>) its is wanting for things that change
@app.route('/users')
def show_users():
    allUsers = User.get_all()
    return render_template('allUsers.html', users=allUsers)


@app.route('/users/<int:id>')
def show_user(id):
    data = {
        'id_nums': id,
    }
    one_user = User.get_one(data)
    print(one_user)
    return render_template('show_users.html', user=one_user[0])


@app.route('/users/save', methods=['POST'])
def save_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/users')


@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id_nums': id,
    }
    one_user = User.get_one(data)
    print(one_user)
    return render_template('edit_user.html', user=one_user[0])


@app.route('/users/update', methods=['POST'])
def update_user():
    data = {
        'id_nums': request.form['id'],
        'fname': request.form['first_name'],
        'lname': request.form['last_name'],
        'email': request.form['email']
    }
    print(data)
    User.update_user(data)
    return redirect('/users')


@app.route('/users/delete/<int:id>')
def delete(id):
    data = {
        "id": id,
    }
    User.delete(data)
    return redirect('/users')
