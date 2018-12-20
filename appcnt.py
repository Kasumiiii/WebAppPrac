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
