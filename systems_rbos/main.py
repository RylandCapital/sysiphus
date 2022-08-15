import pymongo
import os

from systems_rbos.build import build
from dotenv import load_dotenv

load_dotenv()
MONGO = os.getenv("MONGO")

client = pymongo.MongoClient(MONGO)
db = client.sysiphus

#rbos
rbos_data = build()

collection = db.rbos
collection.drop()
collection.insert_many(rbos_data.to_dict(orient='records'))

#next system






