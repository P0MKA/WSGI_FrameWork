from framework.utils import parse_request_params
class GetRequests:

    @staticmethod
    def get_params(environ):
        # получаем параметры запроса
        query_string = environ['QUERY_STRING']

        return parse_request_params(query_string)

class PostRequests:

    @staticmethod
    def get_request_params(env) -> bytes:
        # получаем длину тела
        content_length_data = env.get('CONTENT_LENGTH')
        # приводим к int
        content_length = int(content_length_data) if content_length_data else 0
        print(content_length)
        # считываем данные, если они есть
        # env['wsgi.input'] -> <class '_io.BufferedReader'>
        # запускаем режим чтения

        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b""
        return data

    def parse_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # декодируем данные
            # собираем их в словарь
            result = parse_request_params(data.decode("utf-8"))
        return result

    def get_params(self, environ):
        data = self.get_request_params(environ)
        return self.parse_data(data)
    
params_handler = {
    "GET": GetRequests,
    "POST": PostRequests,
}