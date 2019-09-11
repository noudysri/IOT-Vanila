from os import environ

from flask import Flask, jsonify
import model

app = Flask(__name__)


@app.route('/devicemanagement')
def home():
    return jsonify({'server':'devicemanagement', 'time':model.test_microservice1()})

# if __name__ == "__main__":
#     app.run()
