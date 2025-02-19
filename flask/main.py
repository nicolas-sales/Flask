from flask import Flask, render_template

### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return"<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html') # lien vers index.html grâce à render_template

@app.route('/about')
def about():
    return render_template('about.html') # lien vers about.html

if __name__=="__main__":
    app.run(debug=True) # debug=TRUE , permet au serveur de faire la mise à jour du code automatiquement après avoir sauvegardé