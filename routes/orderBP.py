from flask import Blueprint
from controllers.orderController import find_all, find_all_paginate

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=['GET'])(find_all)
order_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)