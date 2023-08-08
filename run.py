from wsgiref.simple_server import make_server
from whitenoise import WhiteNoise

from framework.settings import SERVER_IP_ADDRESS, SERVER_PORT, FRAMEWORK_TYPE
from framework.main import FrameworkFucktory
from framework.urls import routes, fronts


app = FrameworkFucktory.create(FRAMEWORK_TYPE, routes, fronts)
app = WhiteNoise(app)
app.add_files("./static", "static/")

with make_server(SERVER_IP_ADDRESS, SERVER_PORT, app) as httpd:
    print("Полетели на порту 8000...")
    # Отвечать на запросы, пока процесс не будет убит
    httpd.serve_forever()