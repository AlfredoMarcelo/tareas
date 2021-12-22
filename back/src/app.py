from flask import Flask
from flask_migrate import Migrate
from models import db


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
Migrate(app,db)

db.init_app(app)
@app.route('/')
def home():
    return 'holamundo'

if __name__ == '__main__':
    app.run()