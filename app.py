from flask import Flask
from flask_restful import Api
from resources.item import Item, Ping
from db import db
from resources.create_db import filldb

# import predict_weed
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True
# app.secret_key = 'jose'
api = Api(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()
#     filldb()


# api.add_resource(Item, '/item/<string:name>')

api.add_resource(Ping, '/')
api.add_resource(Item, '/predict')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
            filldb()

    # app.run(port=5000)
    app.run(host='0.0.0.0')
