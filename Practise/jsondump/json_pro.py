import json


class Person:
    def __init__(self, **args):
        self.name = args['name']
        self.age = args['age']


person1 = Person(name="付柏萍", age=23)
person2 = Person(name="李江阳", age=22)
with open("json.txt", "w") as f:
    json.dump([person1, person2], f, default=lambda obj: obj.__dict__, ensure_ascii=False, indent=2, sort_keys=True)
