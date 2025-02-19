from flask import Flask, render_template, request, redirect, url_for
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

#@app.route('/submit',methods=['GET','POST'])   # GET affiche le formulaire (form.html), POST recupère la valeur du champs name et affiche le message "..."
#def submit():
    #if request.method=='POST':               # Récupère le champ name soumis dans le formulaire
    #    name=request.form['name']
    #    return f'Hello {name}!'
    #return render_template('form.html')

## Variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FALLED"
    
    return render_template('result.html', results=res)

## Variable rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FALLED"
    
    exp={'score':score,"res":res}
    
    return render_template('result1.html', results=exp)


## if conditon
@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result.html', results=score)


## Variable rule
@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template('result.html', results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
            science=float(request.form['science'])
            maths=float(request.form['maths'])
            c=float(request.form['c'])
            data_science=float(request.form['datascience'])

            total_score=(science+maths+c+data_science)/4
            return redirect(url_for('successres', score=total_score))

    return render_template('getresult.html')


if __name__=="__main__":
    app.run(debug=True) # debug=TRUE , permet au serveur de faire la mise à jour du code automatiquement après avoir sauvegardé