from datetime import date
import main_app.views as main_app

def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    "/": main_app.IndexView(),
    "/about/": main_app.AboutView(),
    "/contacts/": main_app.ContactsView(),
    "/courses/": main_app.CoursesListView(),
    "/courses/create/": main_app.CreateCourseView(),
    "/courses/copy/": main_app.CopyCourseView(),
    "/categories/": main_app.CategoryListView(),
    "/categories/create/": main_app.CreateCategoryView(),
}