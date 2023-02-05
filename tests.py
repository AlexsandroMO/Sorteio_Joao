import random
import pandas as pd

def number(qt_dez):
  if qt_dez == 10:
    x = int(round(random.random()*100,0))
    return x

  elif qt_dez == 6:
    test_random = False
    while test_random == False:
      x = int(round(random.random()*100,0))
      
      if x > 0 and x < 61:
        return x
        test_random = True
      else:
        test_random = False

def sorted_number(list_read):
  list_number = sorted(list_read)

  for b in range(0, len(list_number)):
    test = list_number[b]
    for a in range(0, len(list_number)):
      if a != b:
        if list_number[a] == test:
          x = number(qt_dez)
          if x != test:
            list_number[a] = x

  list_number = sorted(list_number)
  return list_number


def action_random(qt_dez, qt_col, list_table):
  for a in range(0, qt_col):
    list_number = []
    for a in range(0, qt_dez):
      list_number.append(number(qt_dez))

    list_number = sorted_number(list_number)

    list_table.append(list_number)

  name_col = []
  for a in range(1, len(list_number)+1):
    name_col.append('DEZ_{}'.format(a))

  df = pd.DataFrame(data=list_table, columns=name_col)
  return df

#---------
create_status = input('Deseja Criar um Jogo? (S/N): ').upper()

if create_status == 'n'.upper():
  qt_dez = int(input('(6 ou 10) Digite e quantidade de Dezenas: '))
  qt_col = int(input('Digite e quantidade de Colunas: '))
  print('\n')

  list_table = []
  print('\n')
  print(action_random(qt_dez, qt_col,list_table))

else:
  qt_dez = int(input('(6 ou 10) Digite e quantidade de Dezenas: '))

  list_table = []
  test_while = False
  
  while test_while == False:
    list_number = []
    for a in range(0, qt_dez):
      num = int(input('Digite o Número desejado: '))
      list_number.append(num)

    list_table.append(sorted(list_number))

    test_continue = input('Deseja continuar criando jogos? ').upper()

    if test_continue == 's'.upper():
      test_while = False

    else:
      test_while = True
      test_random = input('Deseja que o rograma preencha as apostas? ').upper()
      if test_random == 's'.upper():
        qt_col = int(input('Defina a quantidade de colunas '))
        print('\n')
        print(action_random(qt_dez, qt_col-len(list_table), list_table))

      else:
        name_col = []
        for a in range(1, len(list_number)+1):
          name_col.append('DEZ_{}'.format(a))

        df = pd.DataFrame(data=list_table, columns=name_col)
        print('\n')
        print(df)
    