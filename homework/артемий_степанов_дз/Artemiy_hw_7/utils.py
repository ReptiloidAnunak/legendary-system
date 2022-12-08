def load_students():
    '''Загружает список студентов из файла'''
    import os
    import json

    students_path = os.path.join ('data', 'students.json')
    with open(students_path):
        students = json.load (open (students_path, 'r',encoding = 'UTF-8'))

    return students


def load_professions():
    '''Загружает список профессий из файла'''
    import os
    import json

    professions_path = os.path.join ('data', 'professions.json')
    with open(professions_path, 'r', encoding = 'UTF-8'):
        professions = json.load (open (professions_path))

    return professions


def get_student_by_pk(pk):
    '''Получает словарь с данными студента по его pk'''
    for element in load_students ():
        if pk == element['pk']:
            return {element['full_name']: element['skills']}

        else:
            continue
    print ('У нас нет такого студента')
    quit ()


def get_profession_by_title(title):
    '''Получает словарь с инфо о профе по названию'''
    for element in load_professions ():
        if element['title'] == title:
            return {element['title']: element['skills']}
            pass
        else:
            continue
    print ('У нас нет такой специальности')
    quit ()


def check_fitness(student, profession):
    '''Возвращает словарь с процентом, пересечением и различием'''
    skill_student = {}
    skill_profession = {}
    phrase_dict = {}

    for skill in student.values ():
        skill_student = set (skill)

    for skill in profession.values ():
        skill_profession = set (skill)

    intersection_st_prof = skill_profession.intersection (skill_student)
    phrase_dict['has'] = intersection_st_prof

    difference_st_prof = skill_profession.difference (skill_student)
    phrase_dict['lacks'] = difference_st_prof

    intersection_len = len (intersection_st_prof)
    skill_profession_len = len (skill_profession)
    phrase_dict["fit_percent"] = int ((intersection_len) / (skill_profession_len / 100))

    return phrase_dict
