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

  def mkdirs(self, path):
    os.makedirs(self.path)

  def read(self):
    if self.path_exists(self.path) is False:
      self.mkdirs(self.path)
    lines = []
    with open(self.join_path(self.path, self.file), 'r') as file:
      lines = file.readlines()
    file.close()

    return lines

  def write(self, value):
    if (self.path_exists(self.path)) is False:
      self.mkdirs(self.path)

    with open(self.join_path(self.path, self.file), 'a') as file:
      file.write(value)
    file.close()