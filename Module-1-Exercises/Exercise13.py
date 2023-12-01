from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
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


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# Task 1, check if number is prime
@app.route('/prime_number/<int:num>', methods=['GET'])
def check_prime(num):
    result = {"Number": num, "isPrime": is_prime(num)}
    return jsonify(result)


# Task 2, ICAO code of an airport, then return name and location of it in JSON
@app.route('/airport/<icao>')
def check_airport(icao):
    result = get_airport_info(icao)
    return result

if __name__ == '__main__':
    app.run(debug=True)
    app.run(use_reloader=True, host='127.0.0.1', port=5000)