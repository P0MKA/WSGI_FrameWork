from datetime import date
from main_app.views import IndexView, AboutView, ContactsView


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/contacts/': ContactsView(),
}