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
