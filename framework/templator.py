from jinja2 import Environment, PackageLoader, select_autoescape

def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка, в которой находится шаблон
    :param kwargs: параметры
    """
    env = Environment(
        loader=PackageLoader("main_app"),
        autoescape=select_autoescape()
    )
    template = env.get_template(template_name)


    return template.render(**kwargs)
