from flask import Flask

app = Flask(__name__)
@app.route('/')
def page_index():
    return '''
<!DOCTYPE html>
<html>
 <head>
  <meta charset='utf-8'>
  <title>Shivaratri</title>
 </head>
 <body bgcolor='#7B68EE'>
 <h1><center><em><font face="serif">Shivaratri</em><center></h1>
 
 <h4><center><font color="#000000" face="serif">Регистрация<center></h2>
 <div>
  <form action="http://httpbin.org/get">
     <p><input type="text" name="name" placeholder="Имя"></p>
     <p><input type="password" name="pass" placeholder="Пароль"></p>
     <p><input type="password" name="pass" placeholder="Еще раз пароль"></p>
     <p>Запомнить меня<input type="checkbox" name="subscribe"></p>
     <p><input type="submit" value="Отправить"></p>
  </form>
 
 </div>
 
 <div>
 
 </div>
 
  <div>
 
 </div>
 
 </body>
</html>
'''
app.run()


@app.route('/data')
def page_index():
    return '''
    <!DOCTYPE html>
<html>
 <head>
  <meta charset='utf-8'>
  
 <head>
 <body bgcolor='#87CEEB'>
 
 </body>
</html>
'''