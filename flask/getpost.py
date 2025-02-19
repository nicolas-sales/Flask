from flask import Flask, render_template, request

### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return"<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html') # lien vers index.html grâce à render_template

@app.route('/about')
def about():
    return render_template('about.html') # lien vers about.html

@app.route('/form',methods=['GET','POST'])   # GET affiche le formulaire (form.html), POST recupère la valeur du champs name et affiche le message "..."
def form():
    if request.method=='POST':               # Récupère le champ name soumis dans le formulaire
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])   # GET affiche le formulaire (form.html), POST recupère la valeur du champs name et affiche le message "..."
def submit():
    if request.method=='POST':               # Récupère le champ name soumis dans le formulaire
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True) # debug=TRUE , permet au serveur de faire la mise à jour du code automatiquement après avoir sauvegardé