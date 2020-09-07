# class Car():
#     def __init__(self, hp, max_speed):
#         self.__hp = hp
#         self.__max_speed = max_speed
#
#     def info_hp(self):
#         return self.__hp
#
#     def info_speed(self):
#         return self.__max_speed
#
#
# class Bus(Car):
#     def __init__(self, hp, max_speed, color, count):
#         super().__init__(hp, max_speed)
#         self.count = count
#         self._color = color
#         self._free_seats = count
#
#     def add_passenger(self, passengers=1):
#         if passengers <= self._free_seats:
#             self._free_seats -= passengers
#             print(f'plus {passengers} passengers')
#         else:
#             print('no free seats')
#
#
# b = Bus(200, 100, 'blue', 25)
# b.add_passenger(6)
# b.add_passenger(6)
# b.add_passenger(6)
# b.add_passenger(6)
# b.add_passenger(7)
#
# print(b._Car__max_speed)


# class Person():
#
#     def __init__(self, name, last_name, phone_number):
#         self.input = {'name': name, 'last name': last_name, 'phone number': phone_number}
#         self.name = name
#         self.last_name = last_name
#         self.phone_number = phone_number
#
#     def info(self):
#         return self.input
#
#
# class Student(Person):
#     def __init__(self, name, last_name, phone_number):
#         super().__init__(name, last_name, phone_number)
#         self.knowledge = []
#
#     def set_knowledge(self, knowledge):
#         self.knowledge.append(knowledge)
#
#     def get_knowledge(self):
#         return self.knowledge
#
#
# class Teacher(Person):
#     def __init__(self, name, last_name, phone_number, list_dict_know, list_students):
#         super().__init__(name, last_name, phone_number)
#         self.knowledge = list_dict_know
#         self.students = list_students
#
#     def teach(self, student_index, knowledge_key):
#         if student_index < len(self.students):
#             for k in self.knowledge:
#                 if k.get(knowledge_key):
#                     self.students[student_index].set_knowledge(k.get(knowledge_key))
#
#
# s1 = Student('Name1', 'Lname1', 6566)
# s2 = Student('Name2', 'Lname2', 6695)
#
# print(s1.get_knowledge())
# print(s1.get_knowledge())
#
# l_s = [s1, s2]
# kn_l = [{'topic1': 'content1', 'topic2': 'content2', 'topic3': 'content3'}]
# t = Teacher('Name3', 'Lname3', 55565, kn_l, l_s)
# t.teach(0, 'topic1')
#
# print(s1.get_knowledge())
# print(s2.get_knowledge())

#
# class Human:
#
#     def __init__(self, **kwargs):
#         self.data = kwargs
#
#     def info(self):
#         for k in self.data:
#             print(f'{k}: {self.data.get(k)}')
#
#     def get_data(self):
#         return self.data
#
#
# h = Human(name='Hooman', age=20, country='Ukraine', job='manager')
# h.info()
# res = h.get_data()
# print(res)

#
