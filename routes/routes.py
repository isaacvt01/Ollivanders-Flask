import click
from flask import Blueprint, request, render_template, jsonify
from database.database import DB

# Se crea una instancia de Blueprint para poder crear rutas
bp = Blueprint('routes', __name__)

# Se crea una instancia de la base de datos
db = DB()


# Ruta para mostrar los items de la base de datos
@bp.route('/items', methods=['GET'])
def get_all_items():
    return db.get_all_items()


# Ruta para agregar un item a la base de datos
@bp.route('/add_items', methods=['POST'])
def add_item():
    name = request.json['name']
    sell_in = request.json['sell_in']
    quality = request.json['quality']
    type = request.json['type']
    return db.add_item(name, sell_in, quality, type)


# Ruta para actualizar un item del inventario
@bp.route('/update_item', methods=['PUT'])
def update_item():
    item_id = request.json['_id']
    name = request.json['name']
    sell_in = request.json['sell_in']
    quality = request.json['quality']
    return db.update_item(item_id, name, sell_in, quality)


# Ruta para mostrar un item
@bp.route('/item/<item_id>', methods=['GET'])
def get_item(item_id):
    return db.get_item(item_id)


# Ruta para inicializar la base de datos
@bp.route('/inicializar', methods=['POST'])
def init_db():
    return db.init_db()


@bp.route('/delete_item', methods=['DELETE'])
def delete_item():
    item_id = request.json['_id']
    return db.delete_item(item_id)


@bp.route('/get_inventory', methods=['GET'])
def get_inventory():
    return db.get_inventory()


@bp.route('/update_inventory', methods=['PUT'])
def update_inventory():
    return db.update_inventory()

@bp.route('/delete_many', methods=['DELETE'])
def delete_many_items():
    type = request.json.get('type')
    return db.delete_many_items(type)

@bp.route('/form/all_items', methods=['GET'])
def all_items_html():
    return render_template('all_items_temp.html', items=db.get_all_items().json['result'])