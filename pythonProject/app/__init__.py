from flask import Flask

from .main.routes import main
from .extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://passionfroid:PassionFroid@cluster0.fszq8.mongodb.net/challdb?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.register_blueprint(main)

    return app
