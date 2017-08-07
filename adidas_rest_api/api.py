from flask_restful import Resource, Api
from flask import Flask
from resources import AdidasProduct

app = Flask(__name__)
api = Api(app)

api.add_resource(AdidasProduct, '/adidas/<string:id>', endpoint='adidas')

if __name__ == '__main__':
    app.run()