from flask import Flask, render_template
from flask_admin import BaseView, expose, Admin

app = Flask(__name__)
app.config.from_pyfile('./settings.py')
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Flask admin config
admin = Admin(
    app,
    name='NBU_analytics_tool',
    template_mode='bootstrap3',
)

class MyView(BaseView):
    @expose('/')
    def index(self):
        return 'Hello World!'

admin.add_view(MyView(name='LOOOOOOOOL', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))

@app.route('/')
def index():
    return render_template('index.html')
