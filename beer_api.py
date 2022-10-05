# BEER QUEST
#
# This app takes the beer ID from the form and display the beer name, description and picture acquired from:
# https://api.punkapi.com/v2/beers/<beer_ID>

from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/beer', methods=['GET', 'POST'])
def piwo():
    if request.method == 'GET':
        return render_template('beer.html')
    else:
        numer = request.form['beer_ID']
        url = f'https://api.punkapi.com/v2/beers/{numer}'
        data = requests.get(url).json()
        beer = dict(data[0])
        return render_template("beer.html", beer_name=beer['name'], beer_description=beer['description'],
                               url_to_beer_pic=beer['image_url'])


app.run(debug=True)
