from whitenoise import WhiteNoise

from framework.settings import FRAMEWORK_TYPE, DATABASE_URI
from framework.urls import routes, fronts
from framework.main import FrameworkFucktory
from database.storage import init_db
from main_app import views

def create_app():
    app = FrameworkFucktory.create(FRAMEWORK_TYPE, routes, fronts)
    app = WhiteNoise(app)
    app.add_files("./static", "static/")

    init_db(DATABASE_URI)

    return app