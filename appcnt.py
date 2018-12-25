from validator import Validator 
from db_cnt import DBcnt

class Webapp:
  def __init__(self, answer):
    self._answer = answer

  def val(self):
    # print(self._answer)
    
    validator = Validator()
    err = validator.check(self._answer)

    if not err :
      val_data = self._answer
      db_cnt = DBcnt()
      db_cnt.add_data(val_data)
      return val_data, True
    else:
      return err, False
  
  def show_data(self):
    db_cnt = DBcnt()
    all_data = db_cnt.show_data()
    return all_data
  
  def search_data(self):
    db_cnt = DBcnt()
    search_data = db_cnt.search_data(self._answer)
    return search_data

  def detail_data(self):
    db_cnt = DBcnt()
    detail_data = db_cnt.detail_data(self._answer)
    return detail_data