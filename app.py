# .venv\scripts\activate
# flask --debug run

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import database
import handling

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("menu.html")


@app.route('/vakken', methods=['post', 'get'])
def vakken():
    if request.method == 'POST':
        vakid = request.form.get('vakid')
        vaknaam = request.form.get('vaknaam')
        vakuur = request.form.get('vakuur')
        database.update_vakken(vakid, vaknaam, vakuur)
    vakken = database.get_vakken().tolist()
    return render_template("vakken.html", vakken=vakken)


@app.route('/deletevakken')
def deletevakken():
    database.delete_vakken()
    return redirect(url_for('vakken'))


@app.route('/laadvakken', methods=['post', 'get'])
def laadvakken():
    database.check_vakken()
    if request.method == 'POST':
        # de functie die lang duurt kan hier
        if not database.check_vakken:
            return redirect(url_for('vakken'))
        else:
            return redirect(url_for('invoer'))
    return render_template("laadvakken.html")


@app.route('/invoer', methods=['post', 'get'])
def invoer():
    if request.method == 'POST':
        formid = request.form
        if "dag" in formid:
            dagen = request.form.get('dagen')
            uuren_per_dag = request.form.get('uuren_per_dag')
            database.update_daguur(dagen, uuren_per_dag)
            # print(f"dagen: {dagen} || uuren = {uuren_per_dag}")

        elif "droptables" in formid:
            checkbox = bool(request.form.get('delconfirm'))
            print(checkbox)
            if checkbox:
                database.delete_tables()

        # elif "vakuuren" in formid:
        #     u1 = request.form.get('u1')
        #     u2 = request.form.get('u2')
        #     u3 = request.form.get('u3')
        #     u4 = request.form.get('u4')
        #     u5 = request.form.get('u5')
        #     u6 = request.form.get('u6')
        #     u7 = request.form.get('u7')
        #     u8 = request.form.get('u8')
        #     u9 = request.form.get('u9')
        #     u10 = request.form.get('u10')
        #     database.update_vakuur(u1, u2, u3, u4, u5, u6, u7, u8, u9, u10)

        elif "leerling" in formid:
            leerlingnmr = request.form.get('leerlingnmr')
            voornaam = request.form.get('voornaam')
            achternaam = request.form.get('achternaam')
            vak = np.asarray(request.form.getlist('vak'))
            print(vak)
            database.update_leerlingen(
                leerlingnmr, voornaam, achternaam, vak)

    vakken = database.get_vakken().tolist()
    return render_template("menu2.html", vakken=vakken)


@app.route('/laad', methods=['post', 'get'])
def laad():
    if request.method == 'POST':
        # de functie die lang duurt kan hier
        if not database.check_tables():
            return redirect(url_for('invoer'))
        else:
            data = handling.delays()
            handling.run()
            return redirect(url_for('roosters'))
    return render_template("laad.html")


@app.route('/roosters')
def roosters():
    return render_template("roosters.html")
