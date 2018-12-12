# server.py
from flask import Flask, render_template, request
from cerberus import Validator
import re
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
#バリデーション定義
schema = {
    'name': {
        'type': 'string',
        'required': True,
        'empty': False,
    },
    'add': {
        'type': 'string',
        'required': True,
        'empty': False,
    },
    'addnum': {
        'type': 'string',
        'required': True,
        'regex': '^[0-9]{3}-[0-9]{4}$',
    },
    'phones': {
        'type': 'string',
        'required': True,
        'regex': '^[0-9]{2,4}-[0-9]{2,4}-[0-9]{3,4}$',
    },
}
"""
# バリデータを作成
v = Validator(schema)

app = Flask(__name__)

url = 'mysql+pymysql://root@localhost/test?charset=utf8'
engine = create_engine(url, echo=True)
Base = declarative_base()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():

                name = request.form['name_form']
                add = request.form['add_form']
                addnum = request.form['addnum_form']
                mail = request.form['mail_form']
                tel = request.form['tel_form']

		#バリデーション
                v.validate(name, add, addnum, mail, tel)

		#ins = "INSERT INTO users (name, address, addnum, mail, tel) VALUES (%s, %s, %s, %s, %s)"
                #data = [( name, add, addnum, mail, tel )]
                #for d in data:
                #    engine.execute(ins,d)	

                pprint(v.errors)
                return render_template('welcome.html', name=name ) 

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=80)
