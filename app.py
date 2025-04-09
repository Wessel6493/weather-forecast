from flask import Flask, render_template, request
import locale
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/forecast', methods=['POST', 'GET'])
def forecast():

    country = request.form.get('country')
    city = request.form.get('city')

    api_key = '3182c1d7601e46c6b95135756251102' 

    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city},{country}&days=3'
     
    

    # print(f"{url}")
    response = requests.get(url)
    data = response.json()
    # return data
    forecast_days = data['forecast']['forecastday']
    locale.setlocale(locale.LC_TIME, 'nl_NL')  
    for day in forecast_days:
        datum = datetime.datetime.strptime(day['date'], "%Y-%m-%d")
        day['day_name'] = datum.strftime("%A")
    # return forecast_days
    # forecast_days = data['forecast']['forecastday'];

    return render_template('forecast.html', country=country, city=city, forecast_days=forecast_days)

if __name__ == '__main__':
    app.run(debug=True)