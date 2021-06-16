import re

class RegGroups:
  def __init__(self, clousure, value):
    self.clousure = clousure
    self.value    = value

  def __exec__(self):
    reg = re.compile(self.clousure)
    reg = reg.search(self.value)

    if reg is None: return None
    return list(reg.groups())

class Converter:
  def __init__(self, value):
    self.value = value
    self.closures = {
      'interger': '^(\d+)$',
      'float': '^((\d+)|(\d+\,\d+)|(\d+\.\d+))$'
    }

  def interger(self):
    value = RegGroups(self.closures['interger'], self.value).__exec__()

    if value is None or len(value) == 0:
      raise Exception('Converter: Invalid value, convert to interger failed')

    return int(value[0])

  def float(self):
    value = RegGroups(self.closures['float'], self.value).__exec__()

    if value is None or len(value) == 0:
      raise Exception('Converter: Invalid value, convert to float failed')

    return float(value[0].replace(',', '.'))

  def string(self):
    return str(self.value)