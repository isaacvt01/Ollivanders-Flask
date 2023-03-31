from flask import jsonify
from pymongo import MongoClient
from domain.GildedRose import GildedRose
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde el archivo .env

class DB():

    def __init__(self):
        items = []
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client['gildedrose']
        self.collection = self.db['articulos']
        self.inventario = GildedRose(items)


    def __repr__(self) -> str:
        return f"{self.db}"

    def get_all_items(self):
        output = []
        for item in self.collection.find():
            output.append({'_id': str(item['_id']), 'name': item['name'], 'sell_in': item['sell_in'], 'quality': item['quality'], 'type': item['type']})
        return jsonify({'result': output})