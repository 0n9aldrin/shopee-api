from flask import Flask
import requests
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()

class StudentsList(Resource):
    def get(self):
        parser.add_argument("keyword")
        args = parser.parse_args()
        return args["keyword"]

api.add_resource(StudentsList, '/api/')


if __name__ == "__main__":
    app.run(debug=True)
