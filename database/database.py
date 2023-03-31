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
            output.append(
                {'_id': str(item['_id']), 'name': item['name'], 'sell_in': item['sell_in'], 'quality': item['quality'],
                 'type': item['type']})
        return jsonify({'result': output})

    def add_item(self, name, sell_in, quality, type):
        try:
            self.isInputCorrect(sell_in, quality, type)
        except:
            return jsonify({'result': 'Error adding item, please verify that sell in and quality are numbers and type '
                                      'is one of the following: normal, conjured, aged brie, sulfuras, backstage'})
        try:
            sell_in = int(sell_in)
            quality = int(quality)
            item_id = self.collection.insert_one(
                {'name': name, 'sell_in': sell_in, 'quality': quality, 'type': type}).inserted_id
            new_item = self.collection.find_one({'_id': item_id})
            output = {'_id': str(new_item['_id']), 'name': new_item['name'], 'sell_in': new_item['sell_in'],
                      'quality': new_item['quality'],
                      'type': new_item['type']}
            self.inventario.create_item(item_id, name, sell_in, quality, type)
            return jsonify({'result': output})
        except:
            return jsonify({'result': 'Error adding item'})

    @staticmethod
    def isDigit(value1, value2):
        try:
            int(value1)
            int(value2)
            return True
        except ValueError:
            return "Error: sell_in and quality must be numbers"

    @staticmethod
    def isTypeCorrect(type):
        types = ['aged brie', 'sulfuras', 'backstage', 'conjured', 'normal']
        try:
            if type not in types:
                raise ValueError(f"Tipo no válido: {type}")
            return True
        except ValueError as error:
            return str(error)

    @staticmethod
    def isInputCorrect(sell_in, quality, type):
        if DB.isDigit(sell_in, quality) and DB.isTypeCorrect(type):
            return True
        else:
            raise Exception
