from flask import Flask, render_template
import json
import os

app = Flask(__name__)

f = open('products.json')
 
products = json.load(f)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
  
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def get_products():
    return render_template('products_layout.html', products=products, title='Products')
  
if __name__ == '__main__':  
    app.run(debug=True) 