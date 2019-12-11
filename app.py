from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

with open('hyper.json') as json_file:
        data = json.load(json_file)

@app.route("/")
def home():
    return render_template('main.html', posts=data['cars'])

@app.route("/cars")
def cars():
    return render_template('main.html', posts=data['cars'])

# @app.route("/id")
# def car_id():
#     return render_template('cars.html', car_id ="101")

@app.route('/cars/<id>')
def car_id(id):
    global data
    foundCar = False
    id = request.view_args['id']
    for car in data['cars']:
      if car['car_id'] == id:
        carById = car
        foundCar = True

    if foundCar:
        print(carById)
        return render_template("carsid.html",car=carById)
    else:
        # render notfound page
        return render_template('error.html', posts=data['cars'])

@app.route('/cars/<string:id>/colors')
def colors(id):
    global data
    found = False
    for car in data['cars']:
        if car['car_id'] == id:
            print(car)
            colors = car['colors']
            found = True
    if found:
        print(colors)
        return render_template("colors.html",colors=colors)
    else:
        # render notfound page
        return render_template('error.html', posts=data['cars'])

@app.route('/cars/<string:id>/colors/<string:color_id>')
def colorsById(id,color_id):
    global data
    found = False
    for car in data['cars']:
        if car['car_id'] == id:
            print(car)
            colors = car['colors']
            found = True
    if found: 
        for color in colors:
            if color['id'] == color_id:
                return render_template("color.html",color=color)
        # render notfound page
        return render_template("colors.html",colors=colors)
    else:
        # render notfound page
        return render_template('error.html', posts=data['cars'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
