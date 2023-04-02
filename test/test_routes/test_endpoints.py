from flask import Flask
from flask_testing import TestCase
from routes.routes import bp
from database.database import DB
import json


class TestRoutes(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(bp)
        return app

    def setUp(self):
        self.client = self.app.test_client()
        self.db = DB()
        self.db.collection.delete_many({})
        self.db.collection.insert_many([
            {"name": "item1", "sell_in": 5, "quality": 10, "type": "normal"},
            {"name": "item2", "sell_in": 10, "quality": 20, "type": "normal"}
        ])

    def test_get_all_items(self):
        response = self.client.get('/items')
        data = json.loads(response.data)['result']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'item1')
        self.assertEqual(data[1]['quality'], 20)

    def test_add_item(self):
        response = self.client.post('/add_items', json={
            "name": "item3",
            "sell_in": 15,
            "quality": 30,
            "type": "normal"
        })
        data = response.json['result']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'item3')
        self.assertEqual(data['quality'], 30)
        self.assertEqual(data['type'], 'normal')

    def test_update_item(self):
        item = self.client.post('/add_items', json={
            "name": "item3",
            "sell_in": 15,
            "quality": 30,
            "type": "normal"
        })

        item_id = item.json['result']['_id']
        response = self.client.put('/update_item', json={
            "_id": item_id,
            "name": "item1",
            "sell_in": 15,
            "quality": 30
        })
        data = response.json['result']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, 1)
        item = self.client.get('/item/' + item_id).json['result']
        self.assertEqual(item['name'], 'item1')
        self.assertEqual(item['quality'], 30)
        self.assertEqual(item['sell_in'], 15)

    def test_init_db(self):
        response = self.client.post('/inicializar')
        self.assertEqual(response.status_code, 200)
        items_name = ['Aged Brie', 'Sulfuras, Hand of Ragnaros', 'Backstage passes to a TAFKAL80ETC concert',
                      'Conjured Mana Cake']
        for item in items_name:
            self.assertTrue(item in str(response.data))

    def test_delete_item(self):
        item_id = self.client.post('/add_items', json={
            "name": "item3",
            "sell_in": 15,
            "quality": 30,
            "type": "normal"
        }).json['result']['_id']
        deleted_item = self.client.delete('/delete_item', json={
            "_id": item_id
        })
        self.assertEqual(deleted_item.status_code, 200)
        self.assertEqual(deleted_item.status_code, 200)
        self.assertEqual(deleted_item.json['result'], 1)
        response = self.client.get('/item/' + item_id).json['result']
        self.assertEqual(response, 'No results found')

    def test_update_inventory(self):
        response = self.client.put('/update_inventory')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 'Inventario actualizado')

    def test_delete_many(self):
        response = self.client.delete('/delete_many', json={
            "type": "normal"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 'Items deleted')
        response = self.client.get('/items').json['result']
        self.assertEqual(len(response), 0)

    def test_add_item_with_non_numeric_sell_in_and_quality(self):
        response = self.client.post('/add_items', json={
            "name": "item3",
            "sell_in": "not_a_number",
            "quality": "not_a_number",
            "type": "normal"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 'Error adding item')

    def test_update_item_with_non_numeric_sell_in_and_quality(self):
        item = self.client.post('/add_items', json={
            "name": "item3",
            "sell_in": 15,
            "quality": 30,
            "type": "normal"
        })

        item_id = item.json['result']['_id']
        response = self.client.put('/update_item', json={
            "_id": item_id,
            "name": "item1",
            "sell_in": "not_a_number",
            "quality": "not_a_number"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 'Error updating item')
