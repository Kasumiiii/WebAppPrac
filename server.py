# server.py
from flask import Flask, render_template, request
import re
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from appcnt import Webapp


app = Flask(__name__)

url = 'mysql+pymysql://root@localhost/test?charset=utf8'
engine = create_engine(url, echo=True)
Base = declarative_base()

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
      request.form['add_form'],
      request.form['addnum_form'],
      request.form['mail_form'],
      request.form['tel_form'],
    ]
    
    appcnt = Webapp(input_list)
    valid_data = appcnt.val() 
    print(valid_data) 

#@app.route('/welcome', methods=['POST'])
#  def welcome(self, data):
    print( valid_data[0] )
                #バリデーション
                #v.validate(name, add, addnum, mail, tel)

                #ins = "INSERT INTO users (name, address, addnum, mail, tel) VALUES (%s, %s, %s, %s, %s)"
                #data = [( name, add, addnum, mail, tel )]
                #for d in data:
                #    engine.execute(ins,d)	
    name = valid_data[0] 
    return render_template('welcome.html', name=name ) 

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=80)
