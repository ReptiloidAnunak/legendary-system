class Question():
    def __init__(self, text, difficulty, correct_unswer, asked, user_answer, points):
        self.text = text
        self.difficulty = difficulty
        self.correct_unswer = correct_unswer
        self.asked = asked
        self.user_answer = user_answer
        self.points = points

    def get_points(self):
        """Возвращает int, количество баллов.
Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
"""

        points = int(self.difficulty)*10
        return points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
    с верным ответов иначе False.
"""

        user_answer = self.user_answer
        correct_answer = self.correct_unswer

        if  user_answer == correct_answer:
            return True
        else:
            return False


    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
                Сложность 4/5
                """
        return f'Вопрос: {self.text}\n{self.difficulty}'

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        return f'Ответ верный, получено {self.points} баллов'

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ {self.correct_unswer}'