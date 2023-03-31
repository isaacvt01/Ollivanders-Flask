from database.database import DB
from flask import jsonify
from flask import Flask

def test_connection():
    app = Flask(__name__)
    db = DB()

    with app.app_context():
        assert db.get_all_items().json['result'] is not None