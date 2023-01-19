# .venv\scripts\activate
# flask --debug run

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import database
import handling
import algorithm2	

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
            global alleRoosters
            alleRoosters = handling.run()
            # alleRoosters = np.array([[np.array(['2134', 'dfgs', 'sdgdsf'], dtype='<U11').tolist(),        np.array([[0, 3, 0, 1, 0, 2, 0, 0],               [0, 0, 2, 0, 4, 0, 6, 0],               [0, 0, 0, 5, 0, 0, 7, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8).tolist(),        np.array([['1', 'Informatica', '4'],               ['4', 'Scheikunde', '3'],               ['6', 'Wiskunde', '6'],               ['7', 'Nederlands', '3']], dtype=object).tolist()],       [np.array(['4', 'John', 'Doe'], dtype='<U11').tolist(),        np.array([[0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8).tolist(),        np.array([['1', 'Informatica', '4'],               ['2', 'Natuurkunde', '5'],               ['3', 'Engels', '5'],               ['4', 'Scheikunde', '3'],               ['5', 'Duits', '2'],               ['6', 'Wiskunde', '6'],               ['7', 'Nederlands', '3']], dtype=object).tolist()],       [np.array(['2342', 'non', 'vak'], dtype='<U11').tolist(),        np.array([[0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8).tolist(),        np.array([], dtype=object).tolist()],       [np.array(['32758', 'struis', 'vogel'], dtype='<U11').tolist(),        np.array([[0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0],               [0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8).tolist(),        np.array([['1', 'Informatica', '4'],               ['7', 'Nederlands', '3'],               ['8', 'Frans', '3']], dtype=object).tolist()]], dtype=object).tolist()
            # alleRoosters = algorithm2.printrooster()
            return redirect(url_for('roosters'))
    return render_template("laad.html")


@app.route('/roosters')
def roosters():

    global alleRoosters
    return render_template("roosters.html", roosters=alleRoosters)
