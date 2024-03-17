from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    return render_template("users.html", usuarios =users)

@app.route('/user/new')
def new():
    return render_template("new.html")

#agregar
@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data={
        "id":id
    }
    return render_template("edit_user.html", persona=User.get_one(data))

#mostrar
@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show_user.html", persona=User.get_one(data))


@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data={
        'id':id
    }
    User.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True, port=8000)