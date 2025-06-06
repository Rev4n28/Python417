import json
from random import choice


def gen_person():
    key = ''
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'e', 'k', 'l', 'm', 'n']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(key) != 10:
        key += choice(num)

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        key: {
            "name": name,
            "tel": tel}
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('numbers.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open('numbers.json', 'w') as f:
        json.dump(data, f, indent=3)


for i in range(5):
    write_json(gen_person())
