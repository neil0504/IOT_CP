from flask import Flask, request, json
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
BASE = '127.0.0.1'
api = Api(app)


class GetData(Resource):

    def get(self):
        return "Get request to GetData"

    def post(self):
        return "Post request to GetData"


api.add_resource(GetData, "/getData")
if __name__ == '__main__':
    app.run(host=BASE, port=int("80"), debug=True)
