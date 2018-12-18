import re

class Validator:
  def __init__(self):
    pass

  def check(self, data):
    i = 0
    #エラーメッセージを入れるリストmsg
    msg = []
    
    #空白チェック
    while i < 5:
      if not data[i]:
        msg.append('{0}番目のデータが未登録です' .format(i+1) )
      i = i+1

    #項目ごとにバリデーション実施
    addnum_regex = '^[0-9]{3}-[0-9]{4}$'
    addmatch = re.match(addnum_regex, data[2])
    if addmatch is None:
      msg.append('郵便番号の値が不正です')

    mail_regex = '^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+.[a-zA-Z0-9_]+$'
    mailmatch = re.match(mail_regex, data[3])
    if mailmatch is None:
      msg.append('メールアドレスの値が不正です')

    tel_regex = '^[0-9]{2,4}-[0-9]{2,4}-[0-9]{3,4}$'
    telmatch = re.match(tel_regex, data[4])
    if telmatch is None:
      msg.append('電話番号の値が不正です')

    #msgを返す(バリデーションエラーがない場合、msgの中身は空)
    return msg