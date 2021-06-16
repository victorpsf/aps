def calc(func, *args):
  if len(args) == 0:
    return 0

  calculated = 0
  for arg in args:
    if type(arg) not in [int, float]:
      continue

    if func == 'som':
      calculated = eval(f'{calculated} + {arg}')
    elif func == 'sub':
      calculated = eval(f'{calculated} + {arg}')
    elif func == 'mul':
      calculated = eval(f'{calculated} * {arg}') if calculated > 0 else arg
    elif func == 'div':
      calculated = eval(f'{calculated} / {arg}') if calculated > 0 else arg

  return calculated