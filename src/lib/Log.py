from Util import current_time, path
from Storage import Storage

class Log:
  def __init__(self, log, file=None):
    self.log  = log
    self.file = self.default_name() if file is None else file

  def default_name(self):
    return f'{current_time()}.log'

  def append(self, text):
    if type(self.log) is str:
      self.log += text
    elif type(self.log) is list:
      self.log.append(text)

  def show(self):
    if type(self.log) is list:
      for log in self.log:
        print(log)
    elif type(self.log) is str:
      print(self.log)

  def save(self):
    string = ''
    storage = Storage(Storage.join_path(path(), 'log/'), self.file)

    if   type(self.log) is list:
      for line in self.log:
        string += f'{line}\n'
    elif type(self.log) is str:
      string = self.log

    storage.write(string)