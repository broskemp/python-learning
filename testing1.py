from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='spy_fly',
    user='root',
    password='yuckyt0r1!',
    autocommit=True
)


def get_airport_info(icao):
    sql = " select ident as 'ICAO', country.name as 'Name', airport.name as 'Location' from airport, country "
    sql += " where airport.iso_country = country.iso_country and ident = '" + icao + "'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result[0])
    return result[0]

@app.route('/airport/<icao>')
def check_airport(icao):
    result = get_airport_info(icao)
    return result

if __name__ == '__main__':
    app.run(debug=True)
    app.run(use_reloader=True, host='127.0.0.1', port=5000)