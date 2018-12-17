#from server import Judge 
from validator import Validator 

class Webapp:
  def __init__(self, answer):
    self._answer = answer

  #print('hello_Webapp')
  def val(self):
    print(self._answer)
    validator = Validator()
    valid_data = validator.check(self._answer)
    return valid_data
