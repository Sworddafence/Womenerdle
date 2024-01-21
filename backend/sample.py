from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import json
from databases import db, SuperVar, User
from multiprocessing import Value
counter = Value('i', 0)
autocorrectkey = ["Harriet Tubman", "Ruth Bader Ginsburg", "Amelia Earhart", "Ada Lovelace", "Virginia Woolf", "Maya Angelou", "Rosa Parks", "Serena Williams", "Simone Biles", "Susan B. Anthony", "Cleopatra", "Marie Curie", "Anne Frank", "Rosalind Franklin", "Grace Hopper", "Helen Keller", "Dolly Parton", "Greta Thunberg", "Sojourner Truth", "Ida B. Wells", "Malala Yousafzai", "Joan of Arc", "Emily Wilding Davison", "Emmeline Pankhurst", "Queen Elizabeth I", "Mary Wollstonecraft", "Indira Gandhi", "Chien-Shiung Wu", "Tawakkol Karman", "Wangari Maathai", "Sinead O'Connor", "Toni Morrison", "Anita Hill", "Gloria Steinem", "Angela Davis", "Marsha P. Johnson", "Simone de Beauvoir", "Fannie Lou", "Dolores Huerta", "Frida Kahlo", "Jane Austen", "Florence Nightingale", "Michelle Obama", "Oprah Winfrey", "Emily Dickinson", "Clara Barton", "Audre Lorde", "Mary Shelley", "Jane Goodall", "Hillary Clinton", "Coco Chanel", "Queen Victoria", "Katherine Johnson", "Margaret Atwood", "Anne Sullivan", "Sacagawea", "Marie Antoinette", "Hellen Keller", "Aung San Suu Kyi", "Benazir Bhutto", "Billie Holiday", "Marie Stopes", "Dorothy Hodgkin", "Barbara McClintock", "Kimberle Crenshaw", "Gloria Anzaldúa", "Cherrie Moraga", "Wilma Mankiller", "Qiu Jin", "Leta Hong Fincher", "Ai Xiaoming", "Lu Pin", "Chun Kyung-ja", "Hedy Lamarr", "Barbara Liskov", "Shafi Goldwasser", "Radia Perlman", "Karen Sparck Jones", "Anita Borg", "Marissa Mayer", "Fei-Fei Li", "Jennifer Widom", "Susan Kare", "Mary Lou Jepsen", "Brenda Laurel", "Elizabeth Blackwell", "Virginia Apgar", "Gerty Cori", "Helen Brooke Taussig", "Dorothy Crowfoot Hodgkin", "Christiane Nüsslein-Volhard", "Gertrude B. Elion", "Jane C. Wright", "Mary Edwards Walker", "Patricia Bath", "Pauline Chen", "Rita Levi-Montalcini", "Lynn Margulis", "Elizabeth Blackburn", "Jennifer Doudna", "Carol Greider", "Martha Chase", "Barbara Seaman", "Rachel Carson", "Dian Fossey", "Mary Anning", "Silvia Federici", "Sheila Rowbotham", "Rosa Luxemburg", "Alexandra Kollontai", "Clara Zetkin", "Juliet Mitchell", "Frigga Haug", "Nancy Fraser", "Selma James", "Heidi Hartmann", "Gayatri Chakravorty Spivak", "Maria Mies", "Zillah Eisenstein", "Iris Marion Young", "Silvia Walby", "Colette Guillaumin", "bell hooks", "Lise Vogel", "Nancy Hartsock", "Kate Millett", "Shulamith Firestone", "Rebecca Walker", "Naomi Wolf", "Judith Butler", "Chimamanda Ngozi Adichie", "Jessica Valenti", "Sor Juana Inez de la Cruz", "Rosario Castellanos", "Elena Poniatowska", "Julia de Burgos", "María Felix", "Leona Vicario", "Adela Velarde Pérez", "Graciela Iturbide", "Remedios Varo", "Gabriela Silang", "Cory Aquino", "Lea Salonga", "Miriam Defensor Santiago", "Maria Ressa", "Pia Alonzo Wurtzbach", "Imelda Marcos", "Gloria Macapagal-Arroyo", "Loida Nicolas Lewis", "Gilda Cordero-Fernando", "Ellen Johnson Sirleaf", "Miriam Makeba", "Funmilayo Ransome-Kuti", "Ama Ata Aidoo", "Leymah Gbowee", "Fatou Bensouda", "Lupita Nyong'o", "Yaa Asantewaa" ]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app)
#db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

#def GrandUser()
def add_comma_between_names(input_string):
    # Split the input string into a list of names
    names = input_string.split('\n')
    
    # Join the names with commas
    result = ', '.join(names)
    return result

# class SuperVar(db.Model):
#     index = db.Column(db.Integer, primary_key=True)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False, nullable=False)
#     hint1 = db.Column(db.String(120), unique=False, nullable=False)
#     hint2 = db.Column(db.String(120), unique=False, nullable=False)
#     hint3 = db.Column(db.String(120), unique=False, nullable=False)
#     hint4 = db.Column(db.String(120), unique=False, nullable=False)
#     hint5 = db.Column(db.String(120), unique=False, nullable=False)
class autocorrect(db.Model):
    name = db.Column(db.String(120), primary_key=True, unique=True)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
   
    #return render_template('index.html', user_input=None)
    # Creating a dummy user for demonstration purposes
    new_user_data = {
        'name': 'Maya Angelou',
        'hint1': 'Renowned poet, memoirist, and civil rights activist.',
        'hint2': 'Wrote the autobiographical novel "I Know Why the Caged Bird Sings.',
        'hint3': 'Worked with Martin Luther King Jr. and Malcolm X in the civil rights movement.',
        'hint4': 'Recited a poem at President Bill Clinton\'s inauguration.',
        'hint5': 'Received numerous awards, including the Presidential Medal of Freedom.',
    }
    new_index = {
        'index': 0
    }

    # if user_to_delete:
    #     db.session.delete(user_to_delete)
    #     db.session.commit()
    #     print(f"User  deleted successfully.")
    # else:
    #     print(f"User not found.")

    all_super_vars = db.session.query(SuperVar).all()
    super_var = None
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
    

    new_auto = autocorrect()

    db.session.commit()

    # Fetch all users
    plusone = super_var.index + 1
    if(plusone > 8):
        plusone = 1
    user = db.session.query(User).filter_by(id=plusone).first() 
    fakeuser = db.session.query(User).filter_by(id=(super_var.index)).first()

    print(f"user: {user}")
    print(f"session['index']: {session.get('index')}")
    if user is None or fakeuser is None:
    # Add more debugging information
        print(f"Error: Unable to fetch user or fakeuser. plusone: {plusone}, super_var.index: {super_var.index}")
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
        
    print(f"user: {user}")
    print(f"session['index']: {session.get('index')}")
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
    #DROPS DATABASE
    # db.session.query(User).delete()
    # db.session.commit()
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
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    index = (out % 10)+1
    fakeuser = db.session.query(User).filter_by(id=(index)).first() 
    data = {
        "name": fakeuser.name,
        "array": [
            fakeuser.hint1,
            fakeuser.hint2,
            fakeuser.hint3,
            fakeuser.hint4,
            fakeuser.hint5
        ],
        "picture": f"/Womenerdle/pictures/{index}/5.jpeg"
    }
    return json.dumps(data)


@app.route('/lists', methods=['GET'])
def lists():
    data = {"array": ["Harriet Tubman", "Ruth Bader Ginsburg", "Amelia Earhart", "Ada Lovelace", "Virginia Woolf", "Maya Angelou", "Rosa Parks", "Serena Williams", "Simone Biles", "Susan B. Anthony", "Cleopatra", "Marie Curie", "Anne Frank", "Rosalind Franklin", "Grace Hopper", "Helen Keller", "Dolly Parton", "Greta Thunberg", "Sojourner Truth", "Ida B. Wells", "Malala Yousafzai", "Joan of Arc", "Emily Wilding Davison", "Emmeline Pankhurst", "Queen Elizabeth I", "Mary Wollstonecraft", "Indira Gandhi", "Chien-Shiung Wu", "Tawakkol Karman", "Wangari Maathai", "Sinead O'Connor", "Toni Morrison", "Anita Hill", "Gloria Steinem", "Angela Davis", "Marsha P. Johnson", "Simone de Beauvoir", "Fannie Lou", "Dolores Huerta", "Frida Kahlo", "Jane Austen", "Florence Nightingale", "Michelle Obama", "Oprah Winfrey", "Emily Dickinson", "Clara Barton", "Audre Lorde", "Mary Shelley", "Jane Goodall", "Hillary Clinton", "Coco Chanel", "Queen Victoria", "Katherine Johnson", "Margaret Atwood", "Anne Sullivan", "Sacagawea", "Marie Antoinette", "Hellen Keller", "Aung San Suu Kyi", "Benazir Bhutto", "Billie Holiday", "Marie Stopes", "Dorothy Hodgkin", "Barbara McClintock", "Kimberle Crenshaw", "Gloria Anzaldúa", "Cherrie Moraga", "Wilma Mankiller", "Qiu Jin", "Leta Hong Fincher", "Ai Xiaoming", "Lu Pin", "Chun Kyung-ja", "Hedy Lamarr", "Barbara Liskov", "Shafi Goldwasser", "Radia Perlman", "Karen Sparck Jones", "Anita Borg", "Marissa Mayer", "Fei-Fei Li", "Jennifer Widom", "Susan Kare", "Mary Lou Jepsen", "Brenda Laurel", "Elizabeth Blackwell", "Virginia Apgar", "Gerty Cori", "Helen Brooke Taussig", "Dorothy Crowfoot Hodgkin", "Christiane Nüsslein-Volhard", "Gertrude B. Elion", "Jane C. Wright", "Mary Edwards Walker", "Patricia Bath", "Pauline Chen", "Rita Levi-Montalcini", "Lynn Margulis", "Elizabeth Blackburn", "Jennifer Doudna", "Carol Greider", "Martha Chase", "Barbara Seaman", "Rachel Carson", "Dian Fossey", "Mary Anning", "Silvia Federici", "Sheila Rowbotham", "Rosa Luxemburg", "Alexandra Kollontai", "Clara Zetkin", "Juliet Mitchell", "Frigga Haug", "Nancy Fraser", "Selma James", "Heidi Hartmann", "Gayatri Chakravorty Spivak", "Maria Mies", "Zillah Eisenstein", "Iris Marion Young", "Silvia Walby", "Colette Guillaumin", "bell hooks", "Lise Vogel", "Nancy Hartsock", "Kate Millett", "Shulamith Firestone", "Rebecca Walker", "Naomi Wolf", "Judith Butler", "Chimamanda Ngozi Adichie", "Jessica Valenti", "Sor Juana Inez de la Cruz", "Rosario Castellanos", "Elena Poniatowska", "Julia de Burgos", "María Felix", "Leona Vicario", "Adela Velarde Pérez", "Graciela Iturbide", "Remedios Varo", "Gabriela Silang", "Cory Aquino", "Lea Salonga", "Miriam Defensor Santiago", "Maria Ressa", "Pia Alonzo Wurtzbach", "Imelda Marcos", "Gloria Macapagal-Arroyo", "Loida Nicolas Lewis", "Gilda Cordero-Fernando", "Ellen Johnson Sirleaf", "Miriam Makeba", "Funmilayo Ransome-Kuti", "Ama Ata Aidoo", "Leymah Gbowee", "Fatou Bensouda", "Lupita Nyong'o", "Yaa Asantewaa" ]}
    return json.dumps(data)
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
