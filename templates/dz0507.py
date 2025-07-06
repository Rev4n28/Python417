from jinja2 import Environment, FileSystemLoader
from jinja2 import Template

inputs = [
    {"name": "firstname", "placeholder": "Имя", "type": "text"},
    {"name": "lastname", "placeholder": "Фамилия", "type": "text"},
    {"name": "address", "placeholder": "Адрес", "type": "text"},
    {"name": "phone", "placeholder": "Телефон", "type": "tel"},
    {"name": "email", "placeholder": "Почта", "type": "email"},

]

html = """
{% macro fun_input(list_of_inputs) %}
    {% for i in list_of_inputs %}
    <input type="{{ i.type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{% endmacro %}

<p>{{ fun_input('username') }}</p>
"""


tm = Template(html)
msg = tm.render()

print(msg)

# # file_loader = FileSystemLoader('templates')
# # env = Environment(loader=file_loader)
#
# html = """
# {% macro fun_input(name, placeholder='', type='') %}
#     <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
# {% endmacro %}
#
# <p>{{ fun_input('firstname', 'Имя', 'text') }}</p>
# <p>{{ fun_input('last', 'Фамилия', 'text') }}</p>
# <p>{{ fun_input('address', 'Адрес', 'text') }}</p>
# <p>{{ fun_input('phone', 'Телефон', 'tel') }}</p>
# <p>{{ fun_input('email', 'Почта', 'email') }}</p>
# """
#
