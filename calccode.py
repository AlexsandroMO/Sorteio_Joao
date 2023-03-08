import random
import pandas as pd
import numpy as np

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
    df_base = pd.read_excel('static/media/carga_jogo.xlsx')
    df_base = df_base.drop(columns=['Unnamed: 0'])

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
# def generation_num_table(qt_col):
    
#     df_base = pd.read_excel('static/media/carga_jogo.xlsx')
#     df_base = df_base.drop(columns=['Unnamed: 0'])
#     #df_base = df_base.drop(columns=[0])

#     list_table = []
#     for a in range(0, len(df_base)):
#         list_read = []
#         for b in range(0, len(df_base.columns)):
#             list_read.append(df_base[b][a])
#         list_table.append(list_read)

#     cont = 0
#     while cont != qt_col:
#         for a in range(0, len(list_table)):
#             test = True
#             while test == True:
#                 x = int(round(random.random()*100,0))
#                 if x in list_table[a]:
#                     test = True
#                 else:
#                     list_table[a].append(x)
#                     test = False
#         cont += 1

#     for a in range(0, len(list_table)):
#         list_table[a].remove(0)

#     df = pd.DataFrame(data=list_table)
#     df.to_excel('static/media/df_prov.xlsx', sheet_name='Jogos Gerados')
#     df = pd.read_excel('static/media/df_prov.xlsx')
#     df = df.drop(columns=['Unnamed: 0'])
    
#     title_read = df.columns
#     read = [list_table, title_read[1::]]

#     df = pd.DataFrame(data=list_table)
#     df.to_excel('static/media/df_prov.xlsx', sheet_name='Jogos Gerados')

#     return read


# def generation_num(qt_col, qt_lin, dez):

#     list_table = []
#     zeros = np.zeros((qt_lin,), dtype=int)
#     for a in zeros:
#         list_table.append([a])

#     cont = 0
#     while cont != qt_col +1:
#         for a in range(0, len(list_table)):
#             test = True
#             while test == True:
#                 x = int(round(random.random()*100,0))
#                 if x in list_table[a]:
#                     test = True
#                 else:
#                     list_table[a].append(x)
#                     test = False
#         cont += 1
#         print(cont)

#     for a in range(0, len(list_table)):
#         list_table[a].remove(0)

#     df = pd.DataFrame(data=list_table)
#     df.to_excel('static/media/df_prov.xlsx', sheet_name='Jogos Gerados')
#     df = pd.read_excel('static/media/df_prov.xlsx')
#     df = df.drop(columns=['Unnamed: 0'])

#     title_read = df.columns
#     read = [list_table, title_read[1::]]

#     return read


def generation_num_col(qt_lin, dez):

    list_table = []
    zeros = np.zeros((qt_lin,), dtype=int)
    for a in zeros:
        list_table.append([a])

    for a in range(0, len(list_table)):
        test = True
        while test == True:
            x = int(dez[random.randint(0,len(dez)-1)])
            if x in list_table[a]:
                test = True
            else:
                list_table[a].append(x)
                test = False

    for a in range(0, len(list_table)):
        list_table[a].remove(0)

    df = pd.DataFrame(data=list_table)
    df.to_excel('static/media/df_prov.xlsx', sheet_name='Jogos Gerados')
    df = pd.read_excel('static/media/df_prov.xlsx')
    df = df.drop(columns=['Unnamed: 0'])

    title_read = df.columns
    read = [list_table, title_read]
    
    return read


def generation_num_colx(dez, qt_col_del, qt_col):

    df_prov = pd.read_excel('static/media/df_prov.xlsx')
    df_prov = df_prov.drop(columns=['Unnamed: 0'])

    if qt_col_del == 'S':
        df_prov.drop(columns=[len(df_prov.columns)-1], inplace=True)
        df_prov.to_excel('static/media/df_prov.xlsx')
        df = pd.read_excel('static/media/df_prov.xlsx')
        df = df.drop(columns=['Unnamed: 0'])

        list_table = []
        for a in range(0, len(df_prov)):
            list_read = []
            for b in range(0, len(df_prov.columns)):
                list_read.append(df_prov[b][a])
            list_table.append(list_read)

        title_read = df.columns
        read = [list_table, title_read]
        
        return read

    else:

        list_table = []
        for a in range(0, len(df_prov)):
            list_read = []
            for b in range(0, len(df_prov.columns)):
                list_read.append(df_prov[b][a])
            list_table.append(list_read)

        for cont in range(0, qt_col):
            for a in range(0, len(list_table)):
                test = True
                while test == True:
                    x = int(dez[random.randint(0,len(dez)-1)])
                    if x in list_table[a]:
                        test = True
                    else:
                        list_table[a].append(x)
                        test = False   

        df = pd.DataFrame(data=list_table)
        df = df.replace(100,0)
        df.to_excel('static/media/df_prov.xlsx')
        df = pd.read_excel('static/media/df_prov.xlsx')
        df = df.drop(columns=['Unnamed: 0'])

        title_read = df.columns
        read = [list_table, title_read]
        
        return read


def gera_game():

    df_base = pd.read_excel('static/media/df_prov.xlsx')
    df_base = df_base.drop(columns=['Unnamed: 0'])

    df_base.to_excel('static/media/JOGO_GERADO.xlsx', sheet_name='Jogos Gerados')

    return 'feito!'


#------
def generation_change_dez(qt_lin, dez1, dez2, extra_dez):

    print('>>>>>>>>>>>>>>>>>>> Aqui foi!!!!')

    #----
    join_table = []
    for a in dez1:
        join_table.append(a)

    for a in dez2:
        join_table.append(a)
    
    #----
    list_table = []
    zeros = np.zeros((qt_lin,), dtype=int)
    for a in zeros:
        list_table.append([a])

    test_extra = 0
    for a in range(0, len(list_table)):
        test = True
        while test == True:
            if test_extra <= extra_dez:
                x = int(join_table[random.randint(0,len(join_table)-1)])
            else:
                x = int(dez1[random.randint(0,len(dez1)-1)])

            if x in list_table[a]:
                test = True
            else:
                list_table[a].append(x)
                #testa se as dezenas escolhidas já saíram
                if x in dez2:
                    test_extra += 1

                test = False

    for a in range(0, len(list_table)):
        list_table[a].remove(0)

    df = pd.DataFrame(data=list_table)
    df.to_excel('static/media/df_prov.xlsx', sheet_name='Jogos Gerados')
    df = pd.read_excel('static/media/df_prov.xlsx')
    df = df.drop(columns=['Unnamed: 0'])

    title_read = df.columns
    read = [list_table, title_read]
    
    return read
