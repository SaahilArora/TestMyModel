from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
from flask_bootstrap import Bootstrap
import os

from com.trainmodel.ml.Factory.ModelFactory import ModelFactory

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
Bootstrap(app)
cors = CORS(app, resources={r"/": {"origins": "/"}})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dataset', methods=['POST'])
def uploadFile():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join('./data/', f.filename))
        return Response(status=200)


@app.route('/testmodel', methods=['GET', 'POST'])
def testModel():
    if request.method == 'POST':
        params = request.get_json()
        file = params['file']
        type = params['type']
        algo = params['algo']
        model = ModelFactory()
        model.__getModel__(filename=file, modelType=type, algoType=algo)
        message = {'response': 'Success',
                   'testR2score': model.getTestR2Score(),
                   'testMae': model.getTestMAEScore(),
                   'trainR2score': model.getTrainR2Score(),
                   'trainMae': model.getTrainMAEScore()
                   }
        return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
