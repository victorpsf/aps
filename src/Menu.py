from src.lib.InputReader import InputReader 
from src.lib.Util import clear_terminal

class Menu:
  def __init__(self):
    self.error = 0
    self.maxError = 3
    self.errorMessage = "error: opção invalida 3x"

    self.message = f"""
    Welcome, Bem Vindo.
    Este aplicativo visa resolver o exercicio da APS
    Segue abaixo opções do app.
    
      (1) Médias de um aluno.
      (2) 
      (0) fechar o app

    obs: {self.maxError} tentativas erradas o app é fechado.
    """
    self.exitMessage = """
      acabamos por aqui, good bye, the end.
    """

  def run(self):
    try:
      while True:
        option = InputReader(self.message).read('int')
        clear_terminal()

        if option == 0:
          break

        if self.error == self.maxError:
          print(self.errorMessage)
          break

        if    option == 1:
          teste = []
        else:
          self.error += 1

      print(self.exitMessage)
    except BaseException as error:
      print(f'error: erro não mapeado ocorrido.\n\n\nlog: {error}')
