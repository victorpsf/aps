import os as OsModule
import platform as PlatformModule
import time
from datetime import datetime

def uname():
  return PlatformModule.uname()

def platform():
  return uname().system.lower()

def clear_terminal():
  if platform() == 'linux':
    OsModule.system('clear')
  else:
    OsModule.system('cls')

def path():
  return OsModule.getcwd()

def current_time():
  return int(datetime.now().timestamp())

def sleep(sec):
  if type(sec) is not int:
    sec = 1
  time.sleep(sec)


def text_concat(*args):
  text = ''

  for arg in args:
    if type(arg) in [str, int, float]:
      text += f' {arg}'
    else:
      continue