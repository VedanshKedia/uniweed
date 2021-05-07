from flask import Flask
from flask_restful import Api
from Disease.resources.item import Item_Disease, Ping
from Weed.resources.item import Item_Weed, Ping
from db import db
from Disease.resources.create_db import filldb_disease
from Weed.resources.create_db import filldb_weed

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
api.add_resource(Item_Disease, '/predict/disease')
# api.add_resource(Item_Weed, '/predict/weed')
api.add_resource(Item_Weed, '/predict')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
            filldb_weed()
            filldb_disease()

    # app.run(port=5000)
    app.run(host='0.0.0.0')
