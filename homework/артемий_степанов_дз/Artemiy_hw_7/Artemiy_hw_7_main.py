'''Импорт модулей и файлов'''

from utils import load_students
from utils import load_professions
from utils import get_student_by_pk
from utils import get_profession_by_title
from utils import check_fitness

#Переменные глобальные и первинонеобходимые

students = load_students()
professions = load_professions()
fullname = ''

pk = int(input('\nВведите номер студента: '))

student = get_student_by_pk(pk)

#Основной блок

for name in student:
    fullname = name
    print(name)
    knowlege = ', '.join(student[name])
    print('Знает', knowlege)


title = input(f'Выберите специальность для оценки студента {fullname}:').strip().capitalize()

profession = get_profession_by_title(title)


phrase_dict = check_fitness(student, profession)
knowlege = ', '.join(phrase_dict["has"])
incompetence = ', '.join(phrase_dict["lacks"])
print('\n')
#####################################################_ИТОГИ_#############################################################

print(f'Пригодность {phrase_dict["fit_percent"]}%\n{fullname} знает {knowlege}\n{fullname} не знает {incompetence}')