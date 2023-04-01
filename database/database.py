from bson import ObjectId
from flask import jsonify
from pymongo import MongoClient
from domain.GildedRose import GildedRose
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde el archivo .env


class DB():

    def __init__(self):
        self.client = MongoClient(
            os.getenv('MONGO_URI'))  # Crea la conexion con la base de datos a partir de la variable de entorno
        self.db = self.client['gildedrose']  # Crea la base de datos
        self.collection = self.db['articulos']  # Crea la coleccion
        self.inventario = GildedRose([])  # Crea el inventario
        self.load_inventory()  # Carga el inventario de la base de datos

    def __repr__(self) -> str:
        return f"{self.db}"

    # Devuelve un json con todos los items de la base de datos
    def get_all_items(self):
        output = []
        for item in self.collection.find():
            output.append(
                {'_id': str(item['_id']), 'name': item['name'], 'sell_in': item['sell_in'], 'quality': item['quality'],
                 'type': item['type']})
        return jsonify({'result': output})

    # Añade un item a la base de datos, devuelve un json con el item añadido
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

    # Actualiza un item de la base de datos, devuelve un json con el item actualizado
    def update_item(self, _id, name, sell_in, quality):
        try:
            self.isDigit(sell_in, quality)
            updated = self.collection.update_one({'_id': ObjectId(_id)},
                                                 {'$set': {'name': name, 'sell_in': int(sell_in),
                                                           'quality': int(quality)}})
            self.inventario.update_item_inventory(ObjectId(_id), name, sell_in, quality)
            return jsonify({'result': updated.modified_count})
        except:
            return Exception

        # Elimina un item por su id

    def delete_item(self, _id):
        try:
            deleted = self.collection.delete_one({'_id': ObjectId(_id)})
            self.inventario.delete_item_inventory(ObjectId(_id))
            return jsonify({'result': deleted.deleted_count})
        except:
            return Exception

    # Devuelve un json con el item de la base de datos
    def get_item(self, _id):
        item = self.collection.find_one({'_id': ObjectId(_id)})
        if item is not None:
            output = {'_id': str(item['_id']), 'name': item['name'], 'sell_in': item['sell_in'],
                      'quality': item['quality'], 'type': item['type']}

        else:
            output = 'No results found'

        return jsonify({'result': output})

    # Revisa que los valores introducidos sean numeros
    @staticmethod
    def isDigit(value1, value2):
        try:
            int(value1)
            int(value2)
            return True
        except ValueError:
            return "Error: sell_in and quality must be numbers"

    # Revisa que el tipo de item sea correcto
    @staticmethod
    def isTypeCorrect(type):
        types = ['aged brie', 'sulfuras', 'backstage', 'conjured', 'normal']
        try:
            if type not in types:
                raise ValueError(f"Tipo no válido: {type}")
            return True
        except ValueError as error:
            return str(error)

    # Revisa que los valores introducidos sean correctos
    @staticmethod
    def isInputCorrect(sell_in, quality, type):
        if DB.isDigit(sell_in, quality) and DB.isTypeCorrect(type):
            return True
        else:
            raise Exception

    # Inicializa la base de datos con los items de ejemplo
    def init_db(self):
        self.inventario.items.clear()
        self.collection.drop()
        self.collection.insert_many([
            {'name': 'Aged Brie', 'sell_in': 2, 'quality': 0, 'type': 'aged brie'},
            {'name': 'Sulfuras, Hand of Ragnaros', 'sell_in': 0, 'quality': 80, 'type': 'sulfuras'},
            {'name': 'Backstage passes to a TAFKAL80ETC concert', 'sell_in': 15, 'quality': 20, 'type': 'backstage'},
            {'name': 'Conjured Mana Cake', 'sell_in': 3, 'quality': 6, 'type': 'conjured'}])

        for item in self.collection.find():
            self.inventario.create_item(item['_id'], item['name'], item['sell_in'], item['quality'], item['type'])
        return str(self.inventario.items)

    # Cargar el inventario con los items de la base de datos al iniciar la aplicación
    def load_inventory(self):
        self.inventario.items.clear()
        for item in self.collection.find():
            self.inventario.create_item(item['_id'], item['name'], item['sell_in'], item['quality'], item['type'])
        return str(self.inventario.items)

    def get_inventory(self):
        output = []
        for item in self.inventario.items:
            output.append({'name': item.name, 'sell_in': item.sell_in, 'quality': item.quality})
        return jsonify({'result': output})
