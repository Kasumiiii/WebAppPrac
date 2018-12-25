# server.py
from flask import Flask, render_template, request
# import re
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

from appcnt import Webapp


app = Flask(__name__)

# url = 'mysql+pymysql://root@localhost/test?charset=utf8'
# engine = create_engine(url, echo=True)
# Base = declarative_base()

@app.route('/')
def index():
  return render_template('index.html')


class Judge:
  def __init__(self):
    pass

  @app.route('/welcome', methods=['POST'])
  def judge_data():
    input_list = [
      request.form['name_form'],
      request.form['address_form'],
      request.form['addnum_form'],
      request.form['mail_form'],
      request.form['tel_form'],
    ]
    
    appcnt = Webapp(input_list)
    valid_data, check = appcnt.val()

    #バリデーション成否によって遷移先決定
    if check == True:
      name = valid_data 
      item_list = ['名前', '住所', '郵便番号', 'メールアドレス', '電話番号']
      all_list = appcnt.show_data()
      return render_template('welcome.html', name=name, item_list=item_list, all_list=all_list) 
    elif check == False:
      err_list = valid_data 
      return render_template('index.html', err_list=err_list)

@app.route('/search', methods=['POST'])
def search_data():
  key = request.form['search_form']
  item_list = ['名前', '住所', '郵便番号', 'メールアドレス', '電話番号']
  print(key)
  appcnt = Webapp(key)
  lists = appcnt.search_data()
  return render_template('search.html', item_list = item_list, lists = lists)

@app.route('/detail', methods=['POST'])
def detail_data():
  key = request.form['user_id_b']
  item_list = ['名前', '住所', '郵便番号', 'メールアドレス', '電話番号']
  print(key)
  appcnt = Webapp(key)
  lists = appcnt.detail_data()
  return render_template('detail.html', item_list = item_list, lists = lists)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=80)

