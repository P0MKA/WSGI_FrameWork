from wsgiref.simple_server import make_server
from whitenoise import WhiteNoise

from framework.main import Framework
from framework.urls import routes, fronts


app = Framework(routes, fronts)
app = WhiteNoise(app)
app.add_files('./static', 'static/')

with make_server('', 8000, app) as httpd:
    print("Полетели на порту 8000...")
    # Отвечать на запросы, пока процесс не будет убит
    httpd.serve_forever()