from flask import Flask
from .libs.config import FlaskConfig

app = Flask(__name__)
app.config.from_object(FlaskConfig)

from .views.web import bweb
app.register_blueprint(bweb)

from .views.api import bapi
app.register_blueprint(bapi, url_prefix="/api")
