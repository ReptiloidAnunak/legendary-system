import json
from flask import Flask, render_template

def load_candidates_from_json(path='candidates.json'):
    '''Возвращает список всех кандидатов из базы'''

    with open(path) as file:
        candidates_base_json = file.read()
        candidates = json.loads(candidates_base_json)
    return candidates


def get_candidate(id):
    """Возвращает одного кандидата по его id"""

    candidates = load_candidates_from_json()
    for candidate in candidates:
        if int(id) == candidate['id']:
            return candidate


def get_candidate_by_name(name):
    """Возвращает одного кандидата по его имени"""

    result = []
    base = load_candidates_from_json()

    for candidate in base:
        if name == candidate['name']:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    '''Возвращает кандидатов по навыку'''

    skill_name = skill_name.strip().lower()
    base = load_candidates_from_json()
    good_candidates = []

    for candidate in base:
        candidate_skills = candidate['skills'].strip().lower().split(', ')

        for skill in candidate_skills:
            count = 0

            if skill_name == skill:
                good_candidates.append(candidate)
                count += 1
            continue

    return good_candidates



