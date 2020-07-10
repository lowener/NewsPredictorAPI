import os
from flask import Flask
from flask import request
import json
from classificator import Classificator

app = Flask(__name__)
classificator = Classificator()

@app.route('/predict', methods = ['POST'])
def predict_req():
    results = {'class': None, 'class_name': None}
    data = request.form
    results['class'], results['class_name'] = classificator.classify(data)
    return json.dumps(results)



if __name__ == "__main__":
    port = os.getenv('PORT', 9200)
    app.run(host='0.0.0.0', port=port)
