from flask import Flask, render_template, request, jsonify
import Scrape

app = Flask(__name__)

def getOrDefault(city):
    if city is None:
        return "udaipur"
    else:
        return city

@app.route('/')
def index():
    city = getOrDefault(request.args.get('city'))
    data = Scrape.scrape(city)
    return render_template('index.html', data=data)

@app.route('/post', methods=['POST'])
def post():
    city = request.form['data']
    try:
        data = Scrape.scrape(city)
        response = {
            'status': 'success',
            'city': city,
            'restaurants': [{'name': name, 'image_link': image_link} for name, image_link in data]
        }
        return jsonify(response)
    except:
        response = {
           'status': 'error',
           'message': 'City not found'
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
