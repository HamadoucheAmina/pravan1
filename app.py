from flask import Flask, render_template, jsonify
import json
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass_root'
app.config['MYSQL_DATABASE_DB'] = 'db_university'

mysql.init_app(app)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('studentdata.html')


@app.route('/api/dataGenre')
def getGenreData():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(sexe) FROM resultats WHERE sexe = 'F'")
    data = cursor.fetchall()
    jsondata = [{'Genre': 'Femme', 'Count': data}]

    cursor.execute("SELECT COUNT(sexe) FROM resultats WHERE sexe = 'H'")
    data = cursor.fetchall()
    jsondata.append({'Genre': 'Homme', 'Count': data})

    return jsonify(jsondata)


@app.route('/api/dataSpec')
def getSpecData():
    conn = mysql.connect()
    cursor = conn.cursor()

    data19 = []
    data20 = []
    data21 = []

    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_1' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_1' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_1' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_2' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_2' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_2' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_3' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_3' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_3' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_4' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_4' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_4' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_5' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_5' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_5' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_6' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_6' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_6' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_7' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_7' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(specialite) FROM resultats WHERE specialite='SPECIALITE_7' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})

    jsondata = [data19, data20, data21]

    return jsonify(jsondata)


@app.route('/api/dataAdmitted')
def getAdmittedData():
    conn = mysql.connect()
    cursor = conn.cursor()

    data19 = []
    data20 = []
    data21 = []

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_1' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_1' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_1' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_2' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_2' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_2' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_3' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_3' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_3' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_4' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_4' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_4' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_5' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_5' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_5' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_6' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_6' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_6' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_7' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_7' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne >= 10 AND specialite='SPECIALITE_7' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})

    jsondata = [data19, data20, data21]

    return jsonify(jsondata)


@app.route('/api/dataDenied')
def getDeniedData():
    conn = mysql.connect()
    cursor = conn.cursor()

    data19 = []
    data20 = []
    data21 = []

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_1' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_1' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_1' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_1', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_2' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_2' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_2' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_2', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_3' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_3' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_3' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_3', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_4' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_4' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_4' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_4', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_5' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_5' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_5' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_5', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_6' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_6' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_6' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_6', 'Count': data[0][0]})

    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_7' AND annee=2019")
    data = cursor.fetchall()
    data19.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_7' AND annee=2020")
    data = cursor.fetchall()
    data20.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})
    cursor.execute("SELECT COUNT(moyenne) FROM resultats WHERE moyenne < 10 AND specialite='SPECIALITE_7' AND annee=2021")
    data = cursor.fetchall()
    data21.append({'Spec': 'SPECIALITE_7', 'Count': data[0][0]})

    jsondata = [data19, data20, data21]

    return jsonify(jsondata)


@app.route('/api/dataAVG')
def getAvgData():
    conn = mysql.connect()
    cursor = conn.cursor()
    dataF = []
    dataH = []

    cursor.execute(
        "SELECT AVG(moyenne) FROM resultats WHERE sexe='F' AND annee=2019")
    data = cursor.fetchall()
    dataF.append({'Année': 2019, 'Moyenne': data[0][0]})
    cursor.execute(
        "SELECT AVG(moyenne) FROM resultats WHERE sexe='F' AND annee=2020")
    data = cursor.fetchall()
    dataF.append({'Année': 2020, 'Moyenne': data[0][0]})
    cursor.execute(
        "SELECT AVG(moyenne) FROM resultats WHERE sexe='F' AND annee=2021")
    data = cursor.fetchall()
    dataF.append({'Année': 2021, 'Moyenne': data[0][0]})

    cursor.execute(
        "SELECT AVG(moyenne) FROM resultats WHERE sexe='H' AND annee=2019")
    data = cursor.fetchall()
    dataH.append({'Année': 2019, 'Moyenne': data[0][0]})
    cursor.execute(
        "SELECT AVG(moyenne) FROM resultats WHERE sexe='H' AND annee=2020")
    data = cursor.fetchall()
    dataH.append({'Année': 2020, 'Moyenne': data[0][0]})
    cursor.execute(
        "SELECT AVG(moyenne) FROM resultats WHERE sexe='H' AND annee=2021")
    data = cursor.fetchall()
    dataH.append({'Année': 2021, 'Moyenne': data[0][0]})

    jsondata = [dataF, dataH]

    return jsonify(jsondata)


@app.route('/api/dataMAXAVG')
def getAVGMAXData():
    conn = mysql.connect()
    cursor = conn.cursor()

    dataF = []
    dataH = []

    cursor.execute("SELECT max(moyenne) FROM resultats WHERE annee=2019 AND sexe='F'")
    data = cursor.fetchall()  # retourne ((moyenne,),)
    dataF.append({'Annee': 2019, 'Moyenne': data[0][0]})
    cursor.execute("SELECT max(moyenne) FROM resultats WHERE annee=2019 AND sexe='H'")
    data = cursor.fetchall()
    dataH.append({'Annee': 2019, 'Moyenne': data[0][0]})
    cursor.execute("SELECT max(moyenne) FROM resultats WHERE annee=2020 AND sexe='F'")
    data = cursor.fetchall()
    dataF.append({'Annee': 2020, 'Moyenne': data[0][0]})
    cursor.execute("SELECT max(moyenne) FROM resultats WHERE annee=2020 AND sexe='H'")
    data = cursor.fetchall()
    dataH.append({'Annee': 2020, 'Moyenne': data[0][0]})
    cursor.execute("SELECT max(moyenne) FROM resultats WHERE annee=2021 AND sexe='F'")
    data = cursor.fetchall()
    dataF.append({'Annee': 2021, 'Moyenne': data[0][0]})
    cursor.execute("SELECT max(moyenne) FROM resultats WHERE annee=2021 AND sexe='H'")
    data = cursor.fetchall()
    dataH.append({'Annee': 2021, 'Moyenne': data[0][0]})

    jsondata = [dataF, dataH]

    return jsonify(jsondata)


@app.route('/api/dataSPECAVG')
def getAVGSpecData():
    conn = mysql.connect()
    cursor = conn.cursor()

    data19 = []
    data20 = []
    data21 = []

    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_1' AND annee=2019")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data19.append({'Spec': 'SPECIALITE_1', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_1' AND annee=2020")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data20.append({'Spec': 'SPECIALITE_1', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_1' AND annee=2021")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data21.append({'Spec': 'SPECIALITE_1', 'Moyennes': data_list})

    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_2' AND annee=2019")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data19.append({'Spec': 'SPECIALITE_2', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_2' AND annee=2020")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data20.append({'Spec': 'SPECIALITE_2', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_2' AND annee=2021")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data21.append({'Spec': 'SPECIALITE_2', 'Moyennes': data_list})

    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_3' AND annee=2019")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data19.append({'Spec': 'SPECIALITE_3', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_3' AND annee=2020")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data20.append({'Spec': 'SPECIALITE_3', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_3' AND annee=2021")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data21.append({'Spec': 'SPECIALITE_3', 'Moyennes': data_list})

    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_4' AND annee=2019")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data19.append({'Spec': 'SPECIALITE_4', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_4' AND annee=2020")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data20.append({'Spec': 'SPECIALITE_4', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_4' AND annee=2021")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data21.append({'Spec': 'SPECIALITE_4', 'Moyennes': data_list})

    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_5' AND annee=2019")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data19.append({'Spec': 'SPECIALITE_5', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_5' AND annee=2020")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data20.append({'Spec': 'SPECIALITE_5', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_5' AND annee=2021")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data21.append({'Spec': 'SPECIALITE_5', 'Moyennes': data_list})

    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_6' AND annee=2019")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data19.append({'Spec': 'SPECIALITE_6', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_6' AND annee=2020")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data20.append({'Spec': 'SPECIALITE_6', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_6' AND annee=2021")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data21.append({'Spec': 'SPECIALITE_6', 'Moyennes': data_list})

    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_7' AND annee=2019")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data19.append({'Spec': 'SPECIALITE_7', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_7' AND annee=2020")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data20.append({'Spec': 'SPECIALITE_7', 'Moyennes': data_list})
    cursor.execute("SELECT moyenne FROM resultats WHERE specialite='SPECIALITE_7' AND annee=2021")
    data = cursor.fetchall()
    data_list = []
    for i in range(0, len(data)):
        data_list.append(data[i][0])

    data21.append({'Spec': 'SPECIALITE_7', 'Moyennes': data_list})

    jsondata = [data19, data20, data21]

    return jsonify(jsondata)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
