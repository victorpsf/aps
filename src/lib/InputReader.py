from src.lib.Converter import Converter 

class InputReader:
  def __init__(self, text):
    self.text      = text
    self.readed    = ''
    self.trying    = 0
    self.maxTrying = 20

  def read(self, type_value, text = None):
    self.readed = input(self.text if text is None else text)

    # invalid type value
    if type(type_value) is not str:
      raise Exception('InputReader error: invalid type to reader')

    try:
      if   type_value == 'int':
        return Converter(self.readed).interger()
      elif type_value == 'float':
        return Converter(self.readed).float()
      elif type_value == 'str':
        return Converter(self.readed).string()
    except BaseException as err:
      if self.trying < self.maxTrying:
        self.trying += 1
        return self.read(type_value)

    raise Exception(f'InputReader error: bat type converter {type_value}')

  def readList(self, type_value, length = 0):
    values = []

    for x in range(0, length):
      values.append(self.read(type_value, f'{self.text}{x + 1}: '))
    return values