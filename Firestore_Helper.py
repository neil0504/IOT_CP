import sqlite3
# Firebase Imports and initialization
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)


# db = firestore.client()


class FirestoreHelper:
    _db = firestore.client()

    _PARAMETER_COLLECTION_NAME = "HEALTH_DATA"
    _PARAMETER_TABLE_NAME = "Data"
    _PARAMETER_ID = 0
    _PARAMETER_USERNAME = "user_name"
    _PARAMETER_PATIENT_NAME = "patient_name"
    _PARAMETER_ENTRY_TIME = "entry_time"
    _PARAMETER_TEMP = "temperature"
    _PARAMETER_HEART_RATE = "heart_rate"
    _PARAMETER_SPO2 = "oxygen_level"

    def __init__(self):
        self.PARAMETER_COLLECTION_NAME = FirestoreHelper._PARAMETER_COLLECTION_NAME
        self.PARAMETER_USERNAME = FirestoreHelper._PARAMETER_USERNAME
        # self.PARAMETER_ID = "id"
        self.PARAMETER_PATIENT_NAME = FirestoreHelper._PARAMETER_PATIENT_NAME
        self.PARAMETER_ENTRY_TIME = FirestoreHelper._PARAMETER_ENTRY_TIME
        self.PARAMETER_TEMP = FirestoreHelper._PARAMETER_TEMP
        self.PARAMETER_HEART_RATE = FirestoreHelper._PARAMETER_HEART_RATE
        self.PARAMETER_SPO2 = FirestoreHelper._PARAMETER_SPO2

        # self.conn = None
        # self.cursor = None
        # self.create()

    # def create(self):
    #     database_name = f"{self.PARAMETER_TABLE_NAME}.sqlite"
    #     self.conn = sqlite3.connect(database_name)
    #     self.cursor = self.conn.cursor()
    #     query = f"CREATE TABLE IF NOT EXISTS {self.PARAMETER_TABLE_NAME}" \
    #             f"({self.PARAMETER_ID} INTEGER NOT NULL PRIMARY KEY, " \
    #             f"{self.PARAMETER_PATIENT_NAME} TEXT, " \
    #             f"{self.PARAMETER_ENTRY_TIME} TEXT, " \
    #             f"{self.PARAMETER_TEMP} TEXT, " \
    #             f"{self.PARAMETER_HEART_RATE} TEXT, " \
    #             f"{self.PARAMETER_SPO2} TEXT)"
    #     self.cursor.execute(query)

    def get_data(self):
        try:
            query = f"SELECT * FROM {self.PARAMETER_TABLE_NAME}"
            data = self.cursor.execute(query).fetchall()
            l = []
            print(data)
            for data_item in data:
                d = {
                    f"{self.PARAMETER_ID}": data_item[0],
                    f"{self.PARAMETER_PATIENT_NAME}": data_item[1],
                    f"{self.PARAMETER_ENTRY_TIME}": data_item[2],
                    f"{self.PARAMETER_TEMP}": data_item[3],
                    f"{self.PARAMETER_HEART_RATE}": data_item[4],
                    f"{self.PARAMETER_SPO2}": data_item[5]
                }
                l.append(d)
            return {"data": l}
        except Exception as e:
            raise Exception(e)

    def insert(self, patient_name, entry_time, temperature, heart_rate, oxygen_level):
        try:
            FirestoreHelper._db.collection(FirestoreHelper._PARAMETER_COLLECTION_NAME).document(FirestoreHelper._PARAMETER_ID + 1).set({"creation": "successfull",
                                                                            "Key": [pubKey.n, pubKey.e],
                                                                            "text": "Hello World!"})
            # self.cursor.execute(
            #     f"INSERT INTO {self.PARAMETER_TABLE_NAME} ({self.PARAMETER_PATIENT_NAME}, {self.PARAMETER_ENTRY_TIME}, {self.PARAMETER_TEMP}, {self.PARAMETER_HEART_RATE}, {self.PARAMETER_SPO2}) VALUES(?, ?, ?, ?, ?)",
            #     (patient_name, entry_time, temperature, heart_rate, oxygen_level))
            # self.conn.commit()
            return {"insert_status": "successfull"}
        except Exception as e:
            raise Exception(e)
            # return {"insert_status": "unsuccessfull"}

    # def delete_cat(self, cat_name):
    #     try:
    #         self.cursor.execute(f"DELETE  FROM {self.TABLE_NAME} WHERE cat_name=?", (cat_name, ))
    #         self.conn.commit()
    #     except Exception as e:
    #         raise Exception(e)
    #
    # def update_cat(self):
    #     pass
