from validator import Validator 

class Webapp:
  def __init__(self, answer):
    self._answer = answer

  def val(self):
    # print(self._answer)
    
    validator = Validator()
    err = validator.check(self._answer)

    if err is None:
      val_data = self._answer
      return val_data
    else:
      return err
