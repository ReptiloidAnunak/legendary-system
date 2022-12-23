from flask import Flask, template_rendered

app = Flask(__name__)
@app.route('/')
def page_index():
    return '''
<!DOCTYPE HTML>
<html>
 <head>
  <title>Кот Джони</title>
 </head>
 <body bgcolor='#BDB76B'>
    <h1><center>Страница кота Джоника<center></h2>
     <div>
      <center><img src="https://sun9-54.userapi.com/impf/c840524/v840524212/bf29/sdhJZy_nfTE.jpg?size=1280x960&quality=96&sign=6d8442125c9bccdef597abcf6001d64b&type=album" height=500 width=700><center>
      <p>Я кот Джоник, известный в узких кругах своим умом и обаянием. Люблю слушать <a href="https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%BA-%D0%BC%D1%83%D0%B7%D1%8B%D0%BA%D0%B0">классический рок</a> и <del>играть</del> сидеть на гитаре.</p>
      <bre>Если хотите поддержать мое творчество, отправьте мой <mark><a href="https://www.sheba.ru/menu/">любимый корм</a></mark> по адресу <ins>г. Москва, ул. Пушкина, д. Колотушкина</ins>.</bre>
      <p>По вопросам сотрудничества пишите на почту: <strong>johnnycat@cmail.com</strong></p>
     </div>
 </body>
</html>
'''
app.run()