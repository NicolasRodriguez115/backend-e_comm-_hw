from flask import Flask
from database import db
from models.schemas import ma

from models.order import Order
from models.product import Product
from models.customer import Customer

from routes.customerBP import customer_blueprint
from routes.productsBP import product_blueprint
from routes.orderBP import order_blueprint
from routes.employeeBP import employee_blueprint

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    
    return app

def blueprint_config(app):

    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(employee_blueprint, url_prefix='/employee')

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()

    app.run()