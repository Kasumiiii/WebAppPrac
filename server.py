# server.py
from flask import Flask, render_template, request

from appcnt import Webapp


app = Flask(__name__)

item_list = ['名前', '住所', '郵便番号', 'メールアドレス', '電話番号']

@app.route('/')
def index():
  return render_template('index.html', item_list=item_list)


class Judge:
  def __init__(self):
    pass

  @app.route('/welcome', methods=['GET','POST'])
  def judge_data():
    if request.form['page_name']=='index':
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
        all_list = appcnt.show_data()
        index_check = True
        return render_template('welcome.html', name=name, item_list=item_list, all_list=all_list, index_check=index_check) 
      elif check == False:
        err_list = valid_data 
        return render_template('index.html', err_list=err_list)

    #詳細画面からデータを変更、削除された際の処理
    elif request.form['page_name']=='detail':
      if request.form['ch_mode']=='削除':
        sel_id = request.form['user_id_b']
        appcnt = Webapp(sel_id)
        appcnt.delete_data()
        all_list = appcnt.show_data()
        index_check = False
        return render_template('welcome.html', item_list=item_list, all_list=all_list, index_check=index_check) 
    
    #データ変更後の処理
    elif request.form['page_name']=='updata':
      input_list = [
        request.form['user_id_b'],
        request.form['name_form'],
        request.form['address_form'],
        request.form['addnum_form'],
        request.form['mail_form'],
        request.form['tel_form'],
      ]
      
      appcnt = Webapp(input_list)
      updata, check = appcnt.update_data()

      #バリデーション成否によって遷移先決定
      if check == True: 
        all_list = appcnt.show_data()
        index_check=True
        return render_template('welcome.html', name=updata, item_list=item_list, all_list=all_list, index_check=index_check)
      elif check == False:
        err_list = updata 
        return render_template('index.html', err_list=err_list)  

    #その他画面からアクセスがあった場合の処理
    else:
      appcnt = Webapp('pass')
      all_list = appcnt.show_data()
      index_check=False
      return render_template('welcome.html', item_list=item_list, all_list=all_list, index_check=index_check)



@app.route('/search', methods=['POST'])
def search_data():
  key = request.form['search_form']
  # print(key)
  appcnt = Webapp(key)
  lists = appcnt.search_data()
  return render_template('search.html', item_list = item_list, lists = lists)

@app.route('/detail', methods=['POST'])
def detail_data():
  key = request.form['user_id_b']
  # print(key)
  appcnt = Webapp(key)
  lists = appcnt.detail_data()
  # print(lists, "def detail_data")
  return render_template('detail.html', item_list = item_list, lists = lists)

@app.route('/updata', methods=['GET', 'POST'])
def update_data():
  key = request.form['user_id_b']
  print(key)
  appcnt = Webapp(key)
  lists = appcnt.detail_data()
  print(lists, "def detail_data")
  return render_template('updata.html', item_list = item_list, lists = lists)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=80)

