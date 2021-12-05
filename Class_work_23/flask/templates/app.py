from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine

# app config
app = Flask(__name__)
app.config.from_pyfile('./settings.py')
# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# DB config
db = MongoEngine(app)

# Flask admin config
admin = Admin(
    app,
    name='TEST ',
    template_mode='bootstrap3',
)

# setup module
import api_test.views
