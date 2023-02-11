import random
import pandas as pd
from random import sample

#----------------------------------
def number(qt_lin, random_option):

    if random_option == 'sim':
        list_number = []
        for a in range(0, qt_lin):
            sorteados = sample(range(1, 101), qt_lin)
            list_number.append(sorteados)
        
        return sorteados
    
    else:
        list_number = []
        for a in range(0, qt_lin):
            list_number.append(int(round(random.random()*100,0)))

        return list_number
        

#---------------------------------- ler tabela carregada
def read_df():
    df_base = pd.read_excel('static/media/caraga_jogo.xlsx')
    df_base = df_base.drop(columns=['Unnamed: 0'])
    #df_base = df_base.drop(columns=[0])

    title_read = df_base.columns

    list_table =[]
    for a in range(0, len(df_base)):
        list_read = []
        for b in range(1, len(df_base.columns)):
            list_read.append(df_base[b][a])
        list_table.append(list_read)

    read = [list_table, title_read[1::]]

    return read



#---------------------------------- ler tabela gerada
def generation_num(random_option, qt_col, qt_lin):
    
    df_base = pd.read_excel('static/media/caraga_jogo.xlsx')
    df_base = df_base.drop(columns=['Unnamed: 0'])
    #df_base = df_base.drop(columns=[0])

    for a in range(0, qt_col):
        game_x = number(qt_lin, random_option)
        #-----
        for a in range(0, len(game_x)):
            for b in range(0, len(df_base.columns)):
                y = df_base[df_base.index == a][b][a]
                if y == game_x[a]:
                    x = int(round(random.random()*101,0))
                    game_x[a] = x
        #-----
        df_base[len(df_base.columns)] = pd.DataFrame(data=game_x)

    df_base = df_base.replace(100, 0)

    list_table =[]
    for a in range(0, len(df_base)):
        list_read = []
        for b in range(1, len(df_base.columns)):
            list_read.append(df_base[b][a])
        list_table.append(list_read)

    title_read = df_base.columns

    read = [list_table, title_read[1::]]

    return read
