import sqlite3
# Firebase Imports and initialization
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from abc import ABC, abstractmethod
from datetime import datetime

cred = credentials.Certificate('./serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)


# db = firestore.client()


class FirestoreHelper:
    __db = firestore.client()
    __PARAMETER_COLLECTION_NAME = "HEALTH_DATA"
    # _PARAMETER_TABLE_NAME = "Data"
    __PARAMETER_ID = 0
    __PARAMETER_USERNAME = "user_name"
    __PARAMETER_PATIENT_NAME = "patient_name"
    __PARAMETER_ENTRY_TIME = "entry_time"
    __PARAMETER_TEMP = "temperature"
    __PARAMETER_HEART_RATE = "heart_rate"
    __PARAMETER_SPO2 = "oxygen_level"

    # def get_data(self):
    #     try:
    #         query = f"SELECT * FROM {self.PARAMETER_TABLE_NAME}"
    #         data = self.cursor.execute(query).fetchall()
    #         l = []
    #         print(data)
    #         for data_item in data:
    #             d = {
    #                 f"{self.PARAMETER_ID}": data_item[0],
    #                 f"{self.PARAMETER_PATIENT_NAME}": data_item[1],
    #                 f"{self.PARAMETER_ENTRY_TIME}": data_item[2],
    #                 f"{self.PARAMETER_TEMP}": data_item[3],
    #                 f"{self.PARAMETER_HEART_RATE}": data_item[4],
    #                 f"{self.PARAMETER_SPO2}": data_item[5]
    #             }
    #             l.append(d)
    #         return {"data": l}
    #     except Exception as e:
    #         raise Exception(e)

    def execute_insert(self, parameter_username, parameter_patient_name, parameter_entry_time, parameter_temp,
                       parameter_heart_rate, parameter_spo2):
        # data = self.insert_data()

        data_json = {
            f"{FirestoreHelper.__PARAMETER_USERNAME}": f"{parameter_username}",
            f"{FirestoreHelper.__PARAMETER_PATIENT_NAME}": f"{parameter_patient_name}",
            f"{FirestoreHelper.__PARAMETER_ENTRY_TIME}": f"{parameter_entry_time}",
            f"{FirestoreHelper.__PARAMETER_TEMP}": f"{parameter_temp}",
            f"{FirestoreHelper.__PARAMETER_HEART_RATE}": f"{parameter_heart_rate}",
            f"{FirestoreHelper.__PARAMETER_SPO2}": f"{parameter_spo2}",
        }
        try:
            FirestoreHelper.__db.collection(FirestoreHelper.__PARAMETER_COLLECTION_NAME).document(
                parameter_username).set(data_json)
            return {"insert_status": "successfull"}
        except Exception as e:
            # {"insert_status": "unsuccessfull"}
            raise Exception(e)

    def execute_get_data(self, parameter_username):
        try:
            doc_ref = FirestoreHelper.__db.collection(FirestoreHelper.__PARAMETER_COLLECTION_NAME).document(
                parameter_username)
            doc = doc_ref.get()
            if doc.exists:
                data = doc.to_dict()
                return {"data": data}
            else:
                data = {}

        except Exception as e:
            # {"insert_status": "unsuccessfull"}
            raise Exception(e)

    def get_parameter_username(self):
        return FirestoreHelper.__PARAMETER_USERNAME

    def get_parameter_patient_name(self):
        return FirestoreHelper.__PARAMETER_PATIENT_NAME

    def get_parameter_entry_time(self):
        return FirestoreHelper.__PARAMETER_ENTRY_TIME

    def get_parameter_temp(self):
        return FirestoreHelper.__PARAMETER_TEMP

    def get_parameter_heart_rate(self):
        return FirestoreHelper.__PARAMETER_HEART_RATE

    def get_parameter_spo2(self):
        return FirestoreHelper.__PARAMETER_SPO2


    # @abstractmethod
    # def insert_data(self) -> list:
    #     pass

    # @abstractmethod
    # def insert_data(self, parameter_username, parameter_patient_name, parameter_entry_time, parameter_temp, parameter_heart_rate, parameter_spo2) -> list:
    #     pass
