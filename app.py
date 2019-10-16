import os
from flask import Flask, render_template, session, redirect, url_for, request, escape
app = Flask(__name__)
#app.config["SECRET_KEY"] = "leyni"
app.secret_key = os.urandom(8)   
#print(os.urandom(8))
# database 
vorur = [   [0,"Peysa","peysa.jpg", 2500],
            [1, "Skór","skor.jpg", 7890],
            [2,"Buxur","buxur.jpg", 6000],
            [3,"Húfa","hufa.jpg",1600],
            [4,"Jakki","jakki.jpg",10000],
            [5,"Frakki","jakki.jpg",20000]
        ]

@app.route("/")
def index():
    karfa = []
    fjoldi=0
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)
    return render_template("index.tpl.html", v=vorur, fjoldi=fjoldi)

@app.route("/add/<int:id>")
def add(id): 
    karfa = []
    fjoldi=0    
    if 'karfa' in session:
        karfa = session['karfa']
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)
    # ef breytan karfa er 0
    else:
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)

    return render_template("index.tpl.html", v=vorur, fjoldi=fjoldi)
# ATH! return vantaði hér

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
        return render_template("karfa.tpl.html", k = karfa, tom = True)

@app.route('/logout')
def logout():
    session.pop("karfa", None)
    return redirect(url_for('index'))

@app.route("/eyda")
def eyda():
    session.pop('karfa',None)
    return render_template("eyda.html")

# hér var @llt routið ekki rétt !
# Eyðum einni vöru úr körfunni
@app.route("/eydavoru/<int:id>")
def eydavoru(id):
    karfa = []
    karfa = session['karfa']
    vara = 0
    # Finnum hvar í session listanum valin vara er í körfunni og eyðum henni
    for i in range(len(karfa)): 
        if karfa[i][0]  == id:
            vara = i
    karfa.remove(karfa[vara])
    session['karfa'] = karfa
    return render_template("eydavoru.html")

@app.route("/result", methods = ["POST"])
def result():
    if request.method == "POST":
        kwargs={
            'name': request.form["nafn"],
            'email': request.form["email"],
            'phone': request.form["simi"],
            'price': request.form["samtals"]
        }
    return render_template('result.tpl.html',**kwargs)

if __name__ == '__main__':
    app.run(debug=True)