# .venv\scripts\activate
# flask --debug run

from flask import Flask, render_template, request, redirect, url_for
import database
import handling

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("menu.html")


@app.route('/invoer', methods=['post', 'get'])
def about():
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

        elif "vakuuren" in formid:
            u1 = request.form.get('u1')
            u2 = request.form.get('u2')
            u3 = request.form.get('u3')
            u4 = request.form.get('u4')
            u5 = request.form.get('u5')
            u6 = request.form.get('u6')
            u7 = request.form.get('u7')
            u8 = request.form.get('u8')
            u9 = request.form.get('u9')
            u10 = request.form.get('u10')
            database.update_vakuur(u1, u2, u3, u4, u5, u6, u7, u8, u9, u10)

        elif "leerling" in formid:
            leerlingnmr = request.form.get('leerlingnmr')
            voornaam = request.form.get('voornaam')
            achternaam = request.form.get('achternaam')
            v1 = bool(request.form.get('v1'))
            v2 = bool(request.form.get('v2'))
            v3 = bool(request.form.get('v3'))
            v4 = bool(request.form.get('v4'))
            v5 = bool(request.form.get('v5'))
            v6 = bool(request.form.get('v6'))
            v7 = bool(request.form.get('v7'))
            v8 = bool(request.form.get('v8'))
            v9 = bool(request.form.get('v9'))
            v10 = bool(request.form.get('v10'))
            vakbin = handling.vak_naar_bin(
                v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)
            database.update_leerlingen(
                leerlingnmr, voornaam, achternaam, vakbin)

    return render_template("menu2.html")


@app.route('/laad', methods=['post', 'get'])
def laad():
    if request.method == 'POST':
        # de functie die lang duurt kan hier
        data = handling.delays()
        return redirect(url_for('roosters'))
    return render_template("laad.html")


@app.route('/roosters')
def roosters():
    return render_template("roosters.html")
