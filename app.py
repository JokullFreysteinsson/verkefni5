import os
from flask import Flask, render_template, session, redirect, url_for, request, escape
app = Flask(__name__)
app.config["SECRET_KEY"] = "leyni"

# database
vorur = [
[0, "Peysa", "peysa.jpg", 2500],
[1, "Skór", "skor.jpg", 7890],
[2,"Buxur","buxur.jpg", 6000],
[3,"Húfa","hufa.jpg",1600],
[4,"Jakki","jakki.jpg",10000]
]

@app.route("/")
def index():
    karfa = []
    fjoldi = 0
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)
    return render_template("index.tpl.html",v=vorur,fjoldi=fjoldi)

@app.route("/add/<int:id>")
def frett(id):
    karfa =[]
    fjoldi=0
    if 'karfa' in session:
        karfa = session['karfa']
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)
    else:
        karfa.append(vorur(id))
        session['karfa'] = karfa
        fjoldi = len(karfa)
    render_template("index.tpl.html",v=vorur ,fjoldi=fjoldi)

@app.route("/karfa")
def karfa():
    karfa = []
    summa = 0
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)
        for i in karfa:
            summa += int(i[3])
        return render_template("karfa.tpl.html", k = karfa, tom = False, fjoldi=fjoldi)
    else:
        return render_template("karfa.tpl", k = karfa, tom = True)

@app.route('/logout',methods={'GET','POST'})
def logout():
    session.pop("karfa", None)
    return redirect(url_for('index'))

@app.route("/add/<int:id>")
def vorur(id):
    karfa = []
    fjoldi=0
    if 'karfa' in session:
        karfa = session['karfa']
        karfa.append(vorur(id))
        session['karfa'] = karfa
        fjoldi = len(karfa)
    else:
        karfa.append(vorur(id))
        session['karfa'] = karfa
        fjoldi = len(karfa)
    return render_template("index.tpl.html",v=vorur ,fjoldi=fjoldi)

@app.route("/eyda")
def eyda():
    session.pop('karfa',None)
    return render_template("eyda.tpl.html")

@app.route("/result", methods = ["POST"])
def result():
    if request.methode == "POST":
        kwargs={
            'name': request.form["nafn"],
            'email': request.form["email"],
            'phone': request.form["simi"],
            'price': request.form["samtals"]
        }
        return render_template('result.tpl.html',**kwargs)
if __name__ == '__main__':
    app.run(debug=True)