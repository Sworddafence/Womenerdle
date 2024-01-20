from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    hint1 = db.Column(db.String(120), unique=False, nullable=False)
    hint2 = db.Column(db.String(120), unique=False, nullable=False)
    hint3 = db.Column(db.String(120), unique=False, nullable=False)
    hint4 = db.Column(db.String(120), unique=False, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('index.html', user_input=user_input)
    #return render_template('index.html', user_input=None)
    # Creating a dummy user for demonstration purposes
    new_user_data = {
        'name': 'Testing',
        'hint1': 'Hint 1',
        'hint2': 'Hint 2',
        'hint3': 'Hint 3',
        'hint4': 'Hint 4'
    }

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
    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
