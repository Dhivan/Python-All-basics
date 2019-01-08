class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'The name is {} age is {}'.format(self.name, self.age)


class teacher(person):
    def __init__(self, name, age, sub):
        person.__init__(self, name, age)
        self.sub = sub

    def __str__(self):
        return person.__str__(self) + "sub is {}".format(self.sub)


t = teacher('hi', 22, 'rng')
print(t)
