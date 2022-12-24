import json
from classes import Candidate


def load_candidates(json_file):
    '''загрузит данные из файла'''
    cadidate_list = []
    with open(json_file) as file:
        candidates_base_json = file.read()
        candidates_base = json.loads(candidates_base_json)
    return candidates_base

candidates_base = load_candidates('candidates.json')

def get_all(candidates_base):
    '''Покажет всех кандидатов'''
    text = ''
    for candidate in candidates_base:
        candidate = Candidate(candidate['pk'], candidate['name'], candidate['picture'], candidate['position'],
                              candidate['gender'], candidate['age'], candidate['skills'])
        text += f'<pre>Имя кандидата - {candidate.name}\n{candidate.position}\n{candidate.skills}\n<pre>'
    return text

def get_by_pk(pk):
    '''Вернет кандидата по pk'''
    text = ''
    for candidate in candidates_base:

        if pk == candidate['pk']:
            text += f'<img src="{candidate["picture"]}" /><br><br>'
            text += 'Имя -' + candidate['name'] + '<br>'
            text += candidate['position'] + '<br>'
            text += candidate['skills'] + '<br>'
            text += candidate['gender'] + '<br>'
            text += str(candidate['age']) + '<br>'
            return text

def get_by_skill(candidates_base, requested_skill):
    '''Вернет кандидатов по навыку
    Тут я решил сделать через класс'''
    requested_skill = requested_skill.strip().lower()
    text = ''
    competents_candidates = ''

    for candidate in candidates_base:
        candidate = Candidate(candidate['pk'], candidate['name'], candidate['picture'], candidate['position'],
                                  candidate['gender'], candidate['age'], candidate['skills'])

        candidate_skills = str(candidate.skills).lower()
        candidate_skills = candidate_skills.split(', ')

        if requested_skill in candidate_skills:
            text += f'<img src="{candidate.picture}" /><br><br>'
            text += 'Имя -' + candidate.name + '<br>'
            text += candidate.position + '<br>'
            text += candidate.skills + '<br>'
            text += candidate.gender + '<br>'
            text += str(candidate.age) + '<br>' + '\n'

    return text


# def get_by_skill(candidate_base, requested_skill):
#     '''Вернет кандидатов по навыку'''
#
#     competents_candidates = []
#
#     for candidate in candidate_base:
#         candidate = Candidate(candidate['pk'], candidate['name'], candidate['picture'], candidate['position'],
#                                   candidate['gender'], candidate['age'], candidate['skills'])
#
#         candidate_skills = str(candidate.skills).lower()
#         candidate_skills = candidate_skills.split(', ')
#
#         for skill in candidate_skills:
#             skill = skill.strip()
#             skill = skill.lower()
#
#         if requested_skill in candidate_skills:
#             competents_candidates.append(candidate.name)
#             print(', '.join(competents_candidates))
#     return ', '.join(competents_candidates)