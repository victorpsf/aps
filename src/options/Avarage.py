from src.lib.InputReader import InputReader
from src.lib.Log import Log
from src.lib.Util import text_concat

class AvarageOption:
  def __init__(self):
    self.name    = ''
    self.notes   = []
    self.total   = 0
    self.avarage = 0

  def Name(self, value = None):
    if value is None:
      return self.name
    else:
      self.name = value

  def Notes(self, value = None):
    if value is None:
      return self.notes
    else:
      self.notes = value

  def Total(self, value = None):
    if value is None:
      return self.total
    else:
      self.total = value

  def Avarage(self, value = None):
    if value is None:
      return self.avarage
    else:
      self.avarage = value



  def run(self):
    self.Name(InputReader('Informe o Nome: ').read('str'))
    self.Notes(InputReader('Nota ').readList('float', 4))
    self.Total(sum(self.Notes()))
    self.Avarage(self.Total / len(self.Notes()))

