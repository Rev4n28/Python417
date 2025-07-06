from jinja2 import Environment, FileSystemLoader
from jinja2 import Template

inputs = [
    {"name": "firstname", "placeholder": "Имя", "type": "text"},
    {"name": "lastname", "placeholder": "Фамилия", "type": "text"},
    {"name": "address", "placeholder": "Адрес", "type": "text"},
    {"name": "phone", "placeholder": "Телефон", "type": "tel"},
    {"name": "email", "placeholder": "Почта", "type": "email"},

]

# html = """
# {% macro fun_input(list_of_inputs) %}
#     {% for i in list_of_inputs %}
#     <input type="{{ i.type }}" name="{{ name }}" placeholder="{{ placeholder }}">
#     {% endfor %}
# {% endmacro %}
#
# <p>{{ fun_input('username') }}</p>
# """

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('home.html')
msg = tm.render(users=inputs)

print(msg)
