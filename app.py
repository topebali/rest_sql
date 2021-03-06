import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_file = "sqlite:///{}".format(os.path.join(project_dir, "data.db"))

#app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "mike"
#app.config['JWT_SECRET_KEY'] = 'mike'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)


#@app.before_first_request
#def create_tables():
    #db.create_all()

#from db import db
#db.init_app(app)

jwt = JWT(app, authenticate, identity) #/auth



api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')




if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
