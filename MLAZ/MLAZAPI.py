import json
from flask import Flask, request
from .models.regression.simple_linear_regression import SimpleLinearRegression

app = Flask(__name__)


@app.route('/api/regression/simple_linear_regression', methods=['POST'])
def simple_linear_regression_predict():
    content = request.json
    x_val = content['x_val']
    training_data = content['training_data']
    regression_obj = SimpleLinearRegression()
    regression_obj.train_model(training_data_json=training_data)
    y_predicted = regression_obj.predict(x_val)
    return json.dumps({'y_predicted': y_predicted})

@app.errorhandler(404)
def not_found(e):
    return '', 404
