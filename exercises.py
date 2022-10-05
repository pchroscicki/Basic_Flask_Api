from flask import Flask, request, render_template

app = Flask (__name__)

@app.route('/')
def main_page():
    return "Hello"

@app.route('/hello/<name>')
def welcome_user(name):
    return f"Witaj {name}!"

from datetime import datetime
@app.route('/time')
def current_time():
    return datetime.now().strftime('%H:%M:%S')

@app.route('/day')
def current_day():
    return datetime.now().strftime('%c')

@app.route('/sum/<num1>/<num2>')
def sum(num1, num2):
    return str(float(num1) + float(num2))

from random import randint
@app.route('/draw')
def draw_numbers():
    return f"{randint(1, 10)}, {randint(1, 10)}, {randint(1, 10)}"

import random
@app.route('/lotto')
def lotto():
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    result = numbers[0:6]
    return f'{result}'[1:-1]

@app.route('/welcome', methods=["GET", "POST"])
def welcome():
    if request.method == "GET":
        return render_template("welcome.html")
    else:
        name = request.form["first_name"]
        return f"Witaj {name}!"

@app.route('/calculator', methods=["GET", "POST"])
def calculator():
    if request.method == "GET":
        return render_template("calculator.html")
    else:
        a = float(request.form["number1"])
        b = float(request.form["number2"])
        if request.form["operation"] == "add":
            return render_template("calculator.html", result=a+b)
        elif request.form["operation"] == "substraction":
            return render_template("calculator.html", result=a-b)
        elif request.form["operation"] == "multiply":
            return render_template("calculator.html", result=a*b)
        elif request.form["operation"] == "divide":
            return render_template("calculator.html", result=a/b)

x = random.randint(1, 101)
@app.route('/number_guessing', methods=["GET", "POST"])
def number_guessing():
    if request.method == "GET":
        return render_template("guessing.html", to_be_guessed=random.randint(1, 100))
    else:
        bet = int(request.form['bet'])
        target = int(request.form["target"])
        if bet < target:
            return render_template("guessing.html", result="Too small! Try again! ", to_be_guessed=target)
        elif bet > target:
            return render_template("guessing.html", result="Too big! Try again", to_be_guessed=target)
        else:
            return render_template("guessing.html", result="Correct! You win!", to_be_guessed=random.randint(1, 100))

@app.route('/full_name', methods=["GET", "POST"])
def full_name():
    if request.method == "GET":
        return render_template("full_name.html")
    else:  # POST
        a = request.form["first_name"]
        b = request.form["surname"]
        return render_template("full_name.html", result=f"Hello {a} {b}!")

app.run(debug=True)