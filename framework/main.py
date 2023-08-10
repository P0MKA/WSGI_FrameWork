from main_app import views
from framework.handlers import params_handler


class PageNotFound404:
    def __call__(self, request):
        return "404 NOT FOUND", f"404 page not found"


class Framework:
    def __init__(self, urls, controllers):
        self.urls = urls
        self.controllers = controllers

    def __call__(self, environ, start_response):
        request = {}

        path = environ["PATH_INFO"]

        method = environ["REQUEST_METHOD"]
        request["method"] = method

        request["params"] = params_handler[method]().get_params(environ)

        if not path.endswith("/"):
            path = f"{path}/"

        if path in self.urls:
            view = self.urls[path]
        else:
            view = PageNotFound404()

        for controller in self.controllers:
            controller(request)

        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]

class LogFramework(Framework):
    def __call__(self, environ, start_response):
        print(
            f"{environ['REQUEST_METHOD']} {environ['PATH_INFO']} params "
            f"{params_handler[environ['REQUEST_METHOD']]().get_params(environ)}"
        )
        return super().__call__(environ, start_response)


class FakeFramework(Framework):
    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-Type", "text/html")])
        return [b"Hello from Fake"]


class FrameworkFucktory:
    frameworks = {
        "app": Framework,
        "log": LogFramework,
        "fake": FakeFramework,
    }

    @classmethod
    def create(cls, framework_type, *args):
        return cls.frameworks[framework_type](*args)