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
