from flask import Flask, jsonify

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(debug=True)
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

