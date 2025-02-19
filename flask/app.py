from flask import Flask

### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return"Welcome to this best Flask course. This should be an amazing course"

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__=="__main__":
    app.run(debug=True) # debug=TRUE , permet au serveur de faire la mise à jour du code automatiquement après avoir sauvegardé