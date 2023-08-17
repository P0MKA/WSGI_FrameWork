from wsgiref.simple_server import make_server

from framework.app import create_app
from framework.settings import SERVER_IP_ADDRESS, SERVER_PORT

app = create_app()

if __name__ == "__main__":
    with make_server(SERVER_IP_ADDRESS, SERVER_PORT, app) as httpd:
        print("Полетели на порту 8000...")
        # Отвечать на запросы, пока процесс не будет убит
        httpd.serve_forever()