import click
from flask import Blueprint, request, render_template, jsonify
from database.database import DB

# Se crea una instancia de Blueprint para poder crear rutas
bp = Blueprint('routes', __name__)

# Se crea una instancia de la base de datos
Db = DB()


# Ruta para mostrar los items de la base de datos
@bp.route('/items', methods=['GET'])
def get_all_items():
    return Db.get_all_items()


@bp.route('/add_items', methods=['POST'])


def add_item():
    name = request.json['name']
    sell_in = request.json['sell_in']
    quality = request.json['quality']
    type = request.json['type']
    return Db.add_item(name, sell_in, quality, type)
