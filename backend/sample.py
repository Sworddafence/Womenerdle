from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#def GrandUser()


class SuperVar(db.Model):
    index = db.Column(db.Integer, primary_key=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    hint1 = db.Column(db.String(120), unique=False, nullable=False)
    hint2 = db.Column(db.String(120), unique=False, nullable=False)
    hint3 = db.Column(db.String(120), unique=False, nullable=False)
    hint4 = db.Column(db.String(120), unique=False, nullable=False)
    hint5 = db.Column(db.String(120), unique=False, nullable=False)


with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
   
    #return render_template('index.html', user_input=None)
    # Creating a dummy user for demonstration purposes
    new_user_data = {
        'name': 'd4',
        'hint1': 'd',
        'hint2': 'd',
        'hint3': 'd',
        'hint4': 'd',
        'hint5': 'd',
    }
    new_index = {
        'index': 0
    }


    all_super_vars = db.session.query(SuperVar).all()
    for super_var in all_super_vars:
        print(super_var.index)
        super_var.index = super_var.index + 1
        if(super_var.index > 8):
            super_var.index = 1
        


    
    existing_user = User.query.filter_by(name=new_user_data['name']).first()
   
    if existing_user:
        # Update the existing user's hints or handle as needed
        existing_user.hint1 = new_user_data['hint1']
        existing_user.hint2 = new_user_data['hint2']
        existing_user.hint3 = new_user_data['hint3']
        existing_user.hint4 = new_user_data['hint4']
    else:
        # Create a new user
        new_user = User(**new_user_data)
        db.session.add(new_user)
        
    db.session.commit()

    # Fetch all users
    plusone = super_var.index + 1
    if(plusone > 8):
        plusone = 1
    user = db.session.query(User).filter_by(id=plusone).first() 
    fakeuser = db.session.query(User).filter_by(id=(super_var.index)).first()
    #users = User.query.all()
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['index'] = user.id
        if user_input == fakeuser.name:
            user_input= "POG"
            return redirect("/success")
        else:
            user_input="FAIIIIIIL"
            return redirect("/two")
    return render_template('index.html', user=user, num = plusone )

@app.route('/two', methods=['GET', 'POST'])
def home_two():
    
    index = session.get('index') 
    if(index == 0):
        index = 9
    user = db.session.query(User).filter_by(id=index).first() 
    fakeuser = db.session.query(User).filter_by(id=(index-1)).first()
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['index'] = user.id
        if user_input == fakeuser.name:
            user_input= "POG"
            return redirect("/success")
        else:
            user_input="FAIL"
            return redirect("/three") 
    return render_template('second.html', user = fakeuser)

@app.route('/three', methods=['GET', 'POST'])
def home_three():
    #db.session.query(User).delete()
    #db.session.commit()
    index = session.get('index') 
    user = db.session.query(User).filter_by(id=index).first() 
    fakeuser = db.session.query(User).filter_by(id=(index-1)).first()
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['index'] = user.id
        if user_input == fakeuser.name:
            user_input= "POG"
            return redirect("/success")
        else:
            user_input="FAIL"
            return redirect("/four") 
    return render_template('third.html', user = fakeuser)

@app.route('/four', methods=['GET', 'POST'])
def home_four():
    
    index = session.get('index') 
    user = db.session.query(User).filter_by(id=index).first() 
    fakeuser = db.session.query(User).filter_by(id=(index-1)).first()
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['index'] = user.id
        if user_input == fakeuser.name:
            user_input= "POG"
            return redirect("/success")
        else:
            user_input="FAIL"
            return redirect("/five") 
    return render_template('fourth.html', user = fakeuser)
@app.route('/five', methods=['GET', 'POST'])
def home_five():
    
    index = session.get('index') 
    user = db.session.query(User).filter_by(id=index).first() 
    fakeuser = db.session.query(User).filter_by(id=(index-1)).first()
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['index'] = user.id
        if user_input == fakeuser.name:
            user_input= "POG"
            return redirect("/success")
        else:
            user_input="FAIL"
            return redirect("/failure") 
    return render_template('fifth.html', user = fakeuser)

@app.route('/failure', methods=['GET', 'POST'])
def fail():
    
    index = session.get('index') 
    index = index - 1
    user = db.session.query(User).filter_by(id=index).first() 
    fakeuser = db.session.query(User).filter_by(id=(index-1)).first()
    
    return render_template('failure.html', user = fakeuser)

@app.route('/success', methods=['GET', 'POST'])
def success():
    
    index = session.get('index') 
    index = index - 1
    user = db.session.query(User).filter_by(id=index).first() 
    fakeuser = db.session.query(User).filter_by(id=(index-1)).first()
    
    return render_template('failure.html', user = user)

@app.route('/hints', methods=['GET'])
def hints():
    superindex = db.session.query(SuperVar).first()       
    if(superindex.index > 8):
        superindex.index = 1 
    superindex.index = superindex.index + 1
    db.session.commit()
    fakeuser = db.session.query(User).filter_by(id=(superindex.index-1)).first() 
    

    data = {
        "name": fakeuser.name,
        "array": [
            fakeuser.hint1,
            fakeuser.hint2,
            fakeuser.hint3,
            fakeuser.hint4,
            fakeuser.hint5
        ],
        "picture": "gold"
    }
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
