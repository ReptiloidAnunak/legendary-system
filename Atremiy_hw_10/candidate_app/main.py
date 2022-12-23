# Импорт необходимых функций
from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidate_by_name, get_candidates_by_skill

# Маршрутизация
app = Flask(__name__)
@app.route('/')
def page_index():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidates/<int:id>')
def page_candidate(id):
    candidate = get_candidate(id)
    if candidate == None:
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Кандидат</title>
</head>
<body bgcolor="#20B2AA">
    <br><br><br><br><br><br>
    <center><h1>Кандидат с таким номером не зарегистрирован</h1></center>
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <center><p><a href='/'> Перейти<br>на Главную страницу </a></p></center>
</body>
</html>'''
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def page_search(candidate_name):
    candidates = get_candidate_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    skill_name = skill_name.title()
    return render_template('skill.html', candidates=candidates, skill_name=skill_name)

# Запуск кода
app.run()

