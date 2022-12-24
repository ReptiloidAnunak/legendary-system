from flask import Flask

app = Flask(__name__)
@app.route('/')
def page_index():
    return '''
<!DOCTYPE html>
<html>
 <head>
  <meta charset='utf-8'>
  <title>Pizza</title>
 </head>

 <body bgcolor='#DEB887'>
  <h1><center>Пиццы<center></h1>
  <forma>
   <h2><center>Итальяна<center></h2>
   <center><img src="https://e0.edimdoma.ru/data/posts/0002/1429/21429-ed4_wide.jpg?1631194036" height='200' width='300'><center>
   <p><center>Пепперони, моцарелла, оливки, красный перец<center><p> 
   <p><center><input type="submit" value="Добавить в корзину"><center></p>
  </forma>
   
  <forma>
   <h2><center>Аргентина<center></h2>
   <center><img src="https://i.obozrevatel.com/food/recipemain/2020/2/4/pizza-foto3.jpg?size=424x424" height='200' width='300'><center>
   <p><center>Моцарелла, чорипан, оливки, хамон<center><p>
   <p><center><input type="submit" value="Добавить в корзину"><center></p>
  </forma>
  
 </body>
</html>  
  '''

app.run(host='0.0.0.0', port=8000)