from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# Below is elephant sql database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jowfndzs:s_fKMzxmDIg6D1gpNd2s_fLNlahUzEh3@heffalump.db.elephantsql.com/jowfndzs'
# Below is Heroku database for other project, commented out
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zfarqkcstxzwbb:753cc730dcb60bdf7d6f7ca62b1bf694d86a9a023c1b1588fbde3e435d64271e@ec2-3-223-242-224.compute-1.amazonaws.com:5432/d60vpf3tooiq23'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
ma = Marshmallow(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from carflask import routes

# To create Database go into Python, >>>from carflask import db           >>>db.create_all()     
# To delete Database go into Python, >>>from carflask import db           >>>db.drop_all()