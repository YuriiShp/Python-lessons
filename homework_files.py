import os
import re


class GetFile:

    def __init__(self, f_path):
        if os.path.exists(f_path):
            self.f_path = f_path
        else:
            raise PathError('Wrong Path')

    def count(self):
        f = open(self.f_path, 'r')
        content = f.read()
        symbs = len(content)
        sents = content.count('.') if content.count('.') != 0 else 1
        words = len(re.compile(r'\w+').findall(content))
        f.close()

        return sents, words, symbs


class PathError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)
#
#
# obj = GetFile('/home/yurii/test')
# print(obj.count())


class User:

    def __init__(self, name, last_name, age, company):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.company = company

    def info(self):
        print(f'Name: {self.name}\n'
              f'Last Name: {self.last_name}\n'
              f'Company: {self.company}\n'
              f'Age: {self.age}\n')

    def save(self, f_name):
        f = open(f_name, 'w')
        content = f'Name: {self.name}\nLast Name: {self.last_name}\n' \
                  f'Company: {self.company}\nAge: {self.age}'
        f.write(content)
        f.close()

        print(f'User info added to file {f_name}')

    @classmethod
    def from_file(cls, f_name):
        if os.path.exists(f_name):
            f = open(f_name, 'r')
        else:
            raise PathError('Wrong Path')

        regEx = re.compile(r'Name: (.*)\nLast Name: (.*)\nCompany: (.*)\nAge: (.*)')
        mo = regEx.search(f.read())
        print(mo.groups())
        name, last_name, company, age = mo.groups()

        return cls(name, last_name, age, company)


us1 = User('Yurii', 'Shapoval', 25, 'ysdo')
us1.save('/home/yurii/Documents/personal_data')

us10 = User.from_file('/home/yurii/Documents/personal_data')
us10.info()