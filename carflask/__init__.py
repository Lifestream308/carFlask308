from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# Below is elephant sql database 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jowfndzs:s_fKMzxmDIg6D1gpNd2s_fLNlahUzEh3@heffalump.db.elephantsql.com/jowfndzs'
# Below is Heroku database  ....    update: Heroku did "maintenance" looks like database was changed/moved
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bwefhrbxvfhmuc:afab3e90282c5ee93ae50e6d96041c61ace9b0e3d10bdd3b26187f4bbe7fa65b@ec2-34-227-135-211.compute-1.amazonaws.com:5432/ddvqeel8ank3q5'
# This is the name of the database after Heroku's maintenance
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hdjumfrahltkmf:34241e5f4ddb3c9e1b9c3f3087679700717b313f6b6be821ba37caf86cbf1a2f@ec2-18-208-55-135.compute-1.amazonaws.com:5432/du4jictpj9ia8'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
ma = Marshmallow(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from carflask import routes

# To create Database go into Python, >>>from carflask import db           >>>db.create_all()     
# To delete Database go into Python, >>>from carflask import db           >>>db.drop_all()