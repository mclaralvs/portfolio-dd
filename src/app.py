from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('index.html')

@app.route('/sobre-mim')
def about():
 return render_template('about.html')

@app.route('/academico')
def academic():
 return render_template('academic.html')

@app.route('/contatos')
def contact():
 return render_template('contact.html')

if __name__ == '__main__':
 app.run()