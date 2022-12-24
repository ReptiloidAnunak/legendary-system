import json
from classes import Candidate
from flask import Flask

from utils import load_candidates, get_all, get_by_pk, get_by_skill
candidates_base = load_candidates('candidates.json')

all_candidates = (get_all(candidates_base))

app = Flask(__name__)
@app.route('/')
def page_index():
    return f'<h1>Главная страница<h1> {all_candidates}'


@app.route('/candidates/<int:pk>')
def get_candidate(pk):
    if get_by_pk(pk) == None:
        return '<h2>Такого кандидата не существует<h2>'
    else:
        return f'<h1>Кандидат номер {pk}<h1><pre>{get_by_pk(pk)}</pre>'

@app.route('/skills/<skill>')
def page_skills(skill):
    return f'<h1>Навык {skill}<h1><pre>{get_by_skill(candidates_base, skill)}<pre>'
app.run()