import os

class Storage:
  def __init__(self, path, file = ''):
    self.path = path
    self.file = file

  def file_name(self, name):
    self.name = name
    return self

  @classmethod
  def join_path(cls, *argv):
    path = ''

    for arg in argv:
      path = os.path.join(path, arg)
    return path

  @classmethod
  def path_exists(cls, path):
    return os.path.exists(path)

  # def read():
    
    
  # def write():