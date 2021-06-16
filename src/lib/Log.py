from lib.Util import current_time

class Log:
  def __init__(self, log, file=None):
    self.log  = log
    self.file = self.default_name() if file is None else file

  def default_name(self):
    return f'{current_time()}.log'

  def log(self):
    print(self.log)

  # def save(self):
