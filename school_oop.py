
# 1. Функції

# avg() returns average value of the list
def avg(input_list):
    numerator = sum(input_list)
    denominator = len(input_list) if len(input_list) != 0 else 1
    return round(numerator / denominator, 0)


# 2. Класи


class Person:
    def __init__(self, name, last_name, phone_number, address):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def bio(self):
        print(f'Name: {self.name} '
              f'\nLast Name: {self.last_name}'
              f'\nPhone Number: {self.phone_number}'
              f'\nHome Address: {self.address}')


class Student(Person):
    def __init__(self, name, last_name, phone_number, address):
        super().__init__(name, last_name, phone_number, address)
        self.scores = dict()

    # встановити список предметів для учня
    def set_subjects(self, subj_list):
        self.scores.clear()
        for subject in subj_list:
            self.scores.update({subject: []})

    # додати оцінку по предмету
    def set_score(self, subject, score):
        self.scores[subject].append(score)

    # вирахувати середній бал з кожного предмету
    def avg_scores(self):
        res = dict()
        for k, v in self.scores.items():
            res.update({k: avg(v)})
        return res


class Teacher(Person):
    def __init__(self, subject, name, last_name, phone_number, address):
        super().__init__(name, last_name, phone_number, address)
        self.subject = subject  # профільний предмет вчителя

    # Поставити оцінку учню по профільному предмету
    def score_stud(self, stud, score):
        stud.set_score(self.subject, score)

    # Перевірити успішність учнів у списку (середній бал з кожного предмету)
    @staticmethod
    def check_performance(stud_list):
        res = dict()
        for stud in stud_list:
            k = f'{stud.name} {stud.last_name}'
            v = stud.avg_scores()
            res.update({k: v})
        return res


class Director(Person):
    def __init__(self, name, last_name, phone_number, address):
        super().__init__(name, last_name, phone_number, address)
        self._of_school = None

    # Зарахувати нового учня до певного класу
    def admit_stud(self, stud, school_class):
        if school_class in self._of_school.classes:
            school_class.add_stud(stud)

    # Відрахувати учня зі школи
    def expel_stud(self, stud):
        for school_class in self._of_school.classes:
            if stud in school_class:
                school_class.remove_stud(stud)

    # Найняти вчителя
    def hire_teacher(self, teacher):
        self._of_school.add_teach(teacher)

    # Звільнити вчителя
    def fire_teacher(self, teacher):
        self._of_school.remove_teach(teacher)


class SchoolClass:
    def __init__(self, grade, teacher, stud_list, subj_list):
        self.grade = grade
        self.teacher = teacher
        self.stud_list = stud_list
        self.subj_list = subj_list

        # присвоїти список предметів всім учням класу
        for stud in self.stud_list:
            stud.set_subjects(self.subj_list)

    # метод перевірки наявності учня в класі
    def __contains__(self, item):
        condition_1 = item in self.stud_list
        condition_2 = item == self.teacher
        return True if condition_1 or condition_2 else False

    # додати учня до класу
    def add_stud(self, stud):
        if stud not in self.stud_list:
            self.stud_list.append(stud)
            stud.set_subjects(self.subj_list)
        else:
            print('student already in this class')

    # прибрати учня з класу
    def remove_stud(self, stud):
        if stud in self.stud_list:
            stud.set_subjects([])
            self.stud_list.remove(stud)
        else:
            print('student is not in this class')

    # змінити класного керівника
    def change_teach(self, teacher):
        self.teacher = teacher

    #
    def remove_teach(self):
        self.teacher = None

    # отримати успішність класу
    def get_performance(self):
        res = dict()
        for stud in self.stud_list:
            k = f'{stud.name} {stud.last_name}'
            v = dict()
            for subject in self.subj_list:
                v.update({subject: stud.avg_scores()[subject]})
            res.update({k: v})
        return res

    # інформація про клас
    def info(self):
        print(f'Grade: {self.grade} \nTeacher:')
        if self.teacher:
            print(f'{self.teacher.name} {self.teacher.last_name}')
        print('Students:')
        for stud in self.stud_list:
            print(f'{stud.name} {stud.last_name}')


class School:
    def __init__(self, director, teachers, classes):
        self.director = director
        self.teachers = teachers
        self.classes = classes

        #
        self.director._of_school = self

    # додати вчителя
    def add_teach(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        else:
            print('teacher already in this school')

    # прибрати вчителя
    def remove_teach(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
            for school_class in self.classes:
                if teacher in school_class:
                    school_class.remove_teach()
        else:
            print('teacher is not in this school')

    # додати клас
    def add_class(self, school_class):
        if school_class not in self.classes:
            self.classes.append(school_class)
        else:
            print('school already contains this class')

    # інформація про школу
    def info(self):
        for school_class in self.classes:
            print(f'\nGrade: {school_class.grade} \nTeacher:')
            if school_class.teacher:
                print(f'{school_class.teacher.name} {school_class.teacher.last_name}')
            print('Students:')
            for stud in school_class.stud_list:
                print(f'{stud.name} {stud.last_name}')


# students
m_stan = Student('Stan', 'March', '123-456', 'sp. 1')
b_kyle = Student('Kyle', 'Broflovski', '123-567', 'sp. 2')
c_eric = Student('Eric', 'Cartman', '123-678', 'sp. 3')
m_kenny = Student('Kenny', 'McCormick', '123-789', 'spr. 4')
s_leo = Student('Leopold', 'Stotch', '123-890', 'sp. 5')
t_wendy = Student('Wendy', 'Testaburger', '123-904', 'sp. 6')
b_token = Student('Token', 'Black', '123-321', 'sp. 7')
v_jimmy = Student('Jimmy', 'Valmer', '123-432', 'sp. 8')
b_timmy = Student('Timmy', 'Burch', '123-543', 'sp. 9')
# students_list = [m_stan, b_kyle, c_eric, m_kenny, s_leo, t_wendy, b_token, v_jimmy, b_timmy]

# teachers
teach_math = Teacher('math', 'John', 'Smith', '123-654', 'sp. 10')
teach_bio = Teacher('biology', 'Joe', 'Johnson', '123-765', 'sp. 11')
teach_phs = Teacher('physics', 'Bob', 'Jack', '123-876', 'sp. 12')
teach_eng = Teacher('english', 'Lisa', 'Stange', '123-987', 'sp. 13')
teach_chem = Teacher('chemistry', 'Walter', 'White', '123-098', 'sp. 14')
teach_geo = Teacher('geography', 'Randy', 'March', '123-109', 'sp. 15')
teachers_list = [teach_math, teach_bio, teach_phs, teach_eng, teach_chem, teach_geo]

# director
principal = Director('Herbert', 'Garrison', '123-666', 'sp.16')

# school classes
grade_4 = SchoolClass(4, teach_math, [m_stan, b_kyle, c_eric], ['math', 'english', 'geography'])
grade_5 = SchoolClass(5, teach_eng, [m_kenny, s_leo, t_wendy], ['math', 'english', 'geography', 'biology'])
grade_6 = SchoolClass(6, teach_chem, [b_token, v_jimmy], ['math', 'english', 'geography', 'biology', 'chemistry', 'physics'])
classes_list = [grade_4, grade_5, grade_6]

# school
sp_elementary = School(principal, teachers_list, classes_list)

# grade_4.info()
# teach_eng.score_stud(c_eric, 2)
# teach_eng.score_stud(c_eric, 4)
# print(teach_eng.check_performance([c_eric, b_token]))
# print(grade_4.get_performance())

# grade_6.info()
# grade_6.add_stud(b_timmy)
# grade_6.info()
# grade_6.add_stud(v_jimmy)
#
# grade_6.remove_stud(b_token)
# grade_6.info()
# grade_6.remove_stud(b_token)

# grade_5.info()
# grade_5.change_teach(teach_geo)
# grade_5.info()

# grade_6.info()
# principal.expel_stud(b_token)
# grade_6.info()

# grade_6.info()
# principal.expel_stud(b_token)
# grade_6.info()

sp_elementary.info()





