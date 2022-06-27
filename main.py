from flask import Flask, request, json
from flask_restful import Resource, Api, abort, reqparse
from Database_Helper import DatabaseHelper
from Firestore_Helper_Class import FirestoreHelper

app = Flask(__name__)
api = Api(app)
database_helper = DatabaseHelper()


class GetData(Resource):

    def get(self):
        json_data = request.get_json()
        firebase_helper = FirestoreHelper()
        json_data = firebase_helper.execute_get_data(json_data[firebase_helper.get_parameter_username()])
        # json_data = database_helper.get_data()
        return json_data


class SendData(Resource):

    def post(self):
        # print(request.get_data())
        json_data = request.get_json()
        # insert_status = database_helper.insert(json_data[database_helper.COLUMN_PATIENT_NAME],
        #                                        json_data[database_helper.COLUMN_ENTRY_TIME],
        #                                        json_data[database_helper.COLUMN_TEMP],
        #                                        json_data[database_helper.COLUMN_HEART_RATE],
        #                                        json_data[database_helper.COLUMN_SPO2])
        firebase_helper = FirestoreHelper()
        insert_status = firebase_helper.execute_insert(json_data[firebase_helper.get_parameter_username()],
                                                       json_data[firebase_helper.get_parameter_patient_name()],
                                                       json_data[firebase_helper.get_parameter_entry_time()],
                                                       json_data[firebase_helper.get_parameter_temp()],
                                                       json_data[firebase_helper.get_parameter_heart_rate()],
                                                       json_data[firebase_helper.get_parameter_spo2()])
        return insert_status


api.add_resource(GetData, "/getData")
api.add_resource(SendData, "/sendData")
if __name__ == '__main__':
    app.secret_key = "ItIsASecret"
    app.debug = True
    app.run()
