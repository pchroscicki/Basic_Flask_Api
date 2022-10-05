# THE MOST INTERESTING FACTS ABOUT DOGS

# This app takes a number provided by user and display the corresponding number of facts about dogs from:
# https://dog-api.kinduff.com/api/facts?number=<number>, separated by <br>.


from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/dogs', methods=['GET', 'POST'])
def psy():
    if request.method == 'GET':
        return render_template('dogs.html')
    else:
        number = request.form['facts_number']
        url = 'https://dog-api.kinduff.com/api/facts?number=' + number
        data = requests.get(url).json()
        facts = data['facts']
        return '<br>'.join(facts)


app.run(debug=True)