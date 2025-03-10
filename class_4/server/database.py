from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import os 
app = Flask(__name__)

# set absolute path to database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///site.db'

db = SQLAlchemy(app)

class Product(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(100), nullable=False)
  discountPrice=db.Column(db.Float)
  price=db.Column(db.Float, nullable=False)
  stock=db.Column(db.Integer, nullable=False)
  description=db.Column(db.String(500), nullable=False)
  image=db.Column(db.String(200), nullable=False)
  
  def __repr__(self) -> str: 
      return f"Product('{self.id}', '{self.name}', '{self.discountPrice}', '{self.price}', '{self.stock}', '{self.description}', '{self.image}')";
  
  
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home_layout.html')
  
@app.route('/about')
def about():
    return render_template('about_layout.html')

@app.route('/products')
def get_products():
    products = Product.query.all()
    return render_template('products_layout.html', products=products, title='All Products')

@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    
    try:
      user = User(username=form.username.data, email=form.email.data, password=form.password.data)
      db.session.add(user)
      db.session.commit()
    except:
      flash(f'User already exists!', 'red')
      return redirect(url_for('register'))
    
    flash(f'Account created for {form.username.data}!', 'blue')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)
  
@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':  
    app.run(debug=True) 
    
    
    