from flask import Flask, render_template, redirect, url_for, request,send_from_directory
import os
import calccode as CalcCode
import numpy as np


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/game_station')
def game_station():
  return render_template('game-station.html')


# @app.route('/fileform')
# def fileform():
#     return render_template('fileform.html')

#------------------------------
# @app.route('/list_doc')
# def list_doc():
#   read_table = CalcCode.read_df()
#   title_read = read_table[1]
#   read = read_table[0]

#   qt_lin = len(read_table[0])
#   qt_lin_ex = len(title_read)
#   list_cont = np.arange(1, 101)
  
#   return render_template('list-doc.html', qt_lin=qt_lin, read=read, list_cont=list_cont, title_read=title_read, qt_lin_ex=qt_lin_ex)

# @app.route('/filltable', methods=['POST'])
# def filltable():
#   if request.method == 'POST':
#     result = request.form
#     qt_col_exist = int(result['colunas_exist'])
#     qt_col = int(result['colunas'])
    
#     read_table = CalcCode.generation_num_table((qt_col + 1)-qt_col_exist)
#     title_read = read_table[1]
#     read = read_table[0]

#   return render_template('list-read.html', read=read, title_read=title_read)

#------------------------------
@app.route('/list_gen')
def list_gen():

  list_cont = np.arange(1, 101)

  table_listnum = []
  baseA, baseB = 1, 11
  for cont in range(0,10):
    table_listnum.append(list(np.arange(baseA,baseB)))
    baseA, baseB  = baseA + 10, baseB + 10

  return render_template('list-gen.html', list_cont=list_cont, table_listnum=table_listnum)


@app.route('/fillgen', methods=['POST'])
def fillgen():
  if request.method == 'POST':
    result = request.form

    dez_A = result['dez']
    dez = []

    if bool(dez_A):
      dez = dez_A.split(';')

    else:
      test = ''
      for a in result:
        if 'lotom' in a:
          test = 'lotom'
          break

        elif 'mega' in a:
          test = 'mega'
          break

        elif 'loto' in a:
          test = 'lotof'
          break

        elif 'milho-dupla' in a:
          test = 'milho-dupla'
          break

        elif 'quin-time' in a:
          test = 'quin-time'
          break

        elif 'dia' in a:
          test = 'dia'
          break


      if test == 'lotom':
        table_listnum2 = list(np.arange(1,101))
        for a in table_listnum2:
          dez.append(a)

      if test == 'mega':
        table_listnum2 = list(np.arange(1,61))
        for a in table_listnum2:
          dez.append(a)

      if test == 'lotof':
        table_listnum2 = list(np.arange(1,26))
        for a in table_listnum2:
          dez.append(a)

      if test == 'milho-dupla':
        table_listnum2 = list(np.arange(1,51))
        for a in table_listnum2:
          dez.append(a)

      if test == 'quin-time':
        table_listnum2 = list(np.arange(1,81))
        for a in table_listnum2:
          dez.append(a)

      if test == 'dia':
        table_listnum2 = list(np.arange(1,32))
        for a in table_listnum2:
          dez.append(a)
      
    qt_lin = int(result['numero-linha'])

    list_cont = np.arange(1, 101)

    print('--------------- ')
    print(dez)
 
    read_table = CalcCode.generation_num_col(qt_lin, dez)
    title_read = read_table[1]
    read = read_table[0]
    
  return render_template('list-read-num-col.html', read=read, title_read=title_read, list_cont=list_cont)


@app.route('/fillgen_num', methods=['POST'])
def fillgen_num():
  if request.method == 'POST':
    result = request.form

    dez_A = result['dez']
    dez = []

    if bool(dez_A):
      dez = dez_A.split(';')

    else:
      test = ''
      for a in result:
        if 'lotom' in a:
          test = 'lotom'
          break

        elif 'mega' in a:
          test = 'mega'
          break

        elif 'loto' in a:
          test = 'lotof'
          break

        elif 'milho-dupla' in a:
          test = 'milho-dupla'
          break

        elif 'quin-time' in a:
          test = 'quin-time'
          break

        elif 'dia' in a:
          test = 'dia'
          break


      if test == 'lotom':
        table_listnum2 = list(np.arange(1,101))
        for a in table_listnum2:
          dez.append(a)

      if test == 'mega':
        table_listnum2 = list(np.arange(1,61))
        for a in table_listnum2:
          dez.append(a)

      if test == 'lotof':
        table_listnum2 = list(np.arange(1,26))
        for a in table_listnum2:
          dez.append(a)

      if test == 'milho-dupla':
        table_listnum2 = list(np.arange(1,51))
        for a in table_listnum2:
          dez.append(a)

      if test == 'quin-time':
        table_listnum2 = list(np.arange(1,81))
        for a in table_listnum2:
          dez.append(a)

      if test == 'dia':
        table_listnum2 = list(np.arange(1,32))
        for a in table_listnum2:
          dez.append(a)

    qt_col = int(result['coluna'])
    qt_col_del = result['coluna-del']
    
    list_cont = np.arange(1, 101)

    read_table = CalcCode.generation_num_colx(dez, qt_col_del, qt_col)
    title_read = read_table[1]
    read = read_table[0]

  return render_template('list-read-num-col.html', read=read, title_read=title_read, list_cont=list_cont)



#-----
@app.route('/list_gen_change')
def list_gen_change():

  list_cont = np.arange(1, 101)

  table_listnum = []
  baseA, baseB = 1, 11
  for cont in range(0,10):
    table_listnum.append(list(np.arange(baseA,baseB)))
    baseA, baseB  = baseA + 10, baseB + 10

  return render_template('list-gen-change.html', list_cont=list_cont, table_listnum=table_listnum)


@app.route('/fillgen_change', methods=['POST'])
def fillgen_change():
  if request.method == 'POST':
    result = request.form

    dez_A = result['dez']
    dez = []

    if bool(dez_A):
      dez = dez_A.split(';')

    else:
      test = ''
      for a in result:
        if 'lotom' in a:
          test = 'lotom'
          break

        elif 'mega' in a:
          test = 'mega'
          break

        elif 'loto' in a:
          test = 'lotof'
          break

        elif 'milho-dupla' in a:
          test = 'milho-dupla'
          break

        elif 'quin-time' in a:
          test = 'quin-time'
          break

        elif 'dia' in a:
          test = 'dia'
          break

        # else:
        #   test = 'dia'
        #   break


      if test == 'lotom':
        table_listnum2 = list(np.arange(1,101))
        for a in table_listnum2:
          dez.append(a)

      if test == 'mega':
        table_listnum2 = list(np.arange(1,61))
        for a in table_listnum2:
          dez.append(a)

      if test == 'lotof':
        table_listnum2 = list(np.arange(1,26))
        for a in table_listnum2:
          dez.append(a)

      if test == 'milho-dupla':
        table_listnum2 = list(np.arange(1,51))
        for a in table_listnum2:
          dez.append(a)

      if test == 'quin-time':
        table_listnum2 = list(np.arange(1,81))
        for a in table_listnum2:
          dez.append(a)

      if test == 'dia':
        table_listnum2 = list(np.arange(1,32))
        for a in table_listnum2:
          dez.append(a)
      
    #----
    qt_lin = int(result['numero-linha'])
    dez2_read = result['dez2']

    dez2 = dez2_read.split(';')
    extra_dez = len(dez2)
    #----

    list_cont = np.arange(1, 101)
 
    read_table = CalcCode.generation_change_dez(qt_lin, dez, dez2, extra_dez)
    title_read = read_table[1]
    read = read_table[0]
    
  return render_template('list-read-change-dez.html', read=read, title_read=title_read, list_cont=list_cont,dez2_read=dez2_read)


@app.route('/fillgen_change_num', methods=['POST'])
def fillgen_change_num():
  if request.method == 'POST':
    result = request.form

    table_listnum = []
    baseA, baseB = 1, 11
    for cont in range(0,10):
      table_listnum.append(list(np.arange(baseA,baseB)))
      baseA, baseB  = baseA + 10, baseB + 10

    #----
    qt_col = int(result['coluna'])
    qt_col_del = result['coluna-del']
   
    dez1_read = result['dez1']
    dez1 = dez1_read.split(';')
    
    dez2_read = result['dez2']
    dez2 = dez2_read.split(';')
    extra_dez = len(dez2)

    #----

    list_cont = np.arange(1, 101)

    read_table = CalcCode.generation_num_change(dez1, dez2, qt_col_del, qt_col, extra_dez)
    title_read = read_table[1]
    read = read_table[0]

  return render_template('list-read-change-dez.html', read=read, title_read=title_read, table_listnum=table_listnum, list_cont=list_cont, dez2_read=dez2_read, dez1_read=dez1_read, qt_col=qt_col)


@app.route('/list_gen_change_2')
def list_gen_change_2():

  list_cont = np.arange(1, 101)

  table_listnum = []
  baseA, baseB = 1, 11
  for cont in range(0,10):
    table_listnum.append(list(np.arange(baseA,baseB)))
    baseA, baseB  = baseA + 10, baseB + 10

  return render_template('list-gen-change-2.html', list_cont=list_cont, table_listnum=table_listnum)


@app.route('/fillgen_change_2', methods=['POST'])
def fillgen_change_2():
  if request.method == 'POST':
    result = request.form

    dez_A = result['dez']
    dez = []

    if bool(dez_A):
      dez = dez_A.split(';')

    else:
      test = ''
      for a in result:
        if 'lotom' in a:
          test = 'lotom'
          break

        elif 'mega' in a:
          test = 'mega'
          break

        elif 'loto' in a:
          test = 'lotof'
          break

        elif 'milho-dupla' in a:
          test = 'milho-dupla'
          break

        elif 'quin-time' in a:
          test = 'quin-time'
          break

        elif 'dia' in a:
          test = 'dia'
          break

        # else:
        #   test = 'dia'
        #   break


      if test == 'lotom':
        table_listnum2 = list(np.arange(1,101))
        for a in table_listnum2:
          dez.append(a)

      if test == 'mega':
        table_listnum2 = list(np.arange(1,61))
        for a in table_listnum2:
          dez.append(a)

      if test == 'lotof':
        table_listnum2 = list(np.arange(1,26))
        for a in table_listnum2:
          dez.append(a)

      if test == 'milho-dupla':
        table_listnum2 = list(np.arange(1,51))
        for a in table_listnum2:
          dez.append(a)

      if test == 'quin-time':
        table_listnum2 = list(np.arange(1,81))
        for a in table_listnum2:
          dez.append(a)

      if test == 'dia':
        table_listnum2 = list(np.arange(1,32))
        for a in table_listnum2:
          dez.append(a)
    
  qt_lin = int(result['numero-linha'])
  col_A = int(result['numero-coluna-dez'])
  qt_col_ex =  int(result['numero-coluna-extra'])

  dez_ex = result['dez-extra']
  dez_extra = dez_ex.split(';')

  qt_col = col_A + qt_col_ex

  list_cont = np.arange(1, 101)

  read_table = CalcCode.generation_change_dez_2(qt_col, col_A, qt_col_ex, qt_lin, dez, dez_extra)
  title_read = read_table[0]
  read = read_table[1]
    
  return render_template('list-read-change-dez-2.html', read=read, title_read=title_read, list_cont=list_cont)


#-----
@app.route('/handleUpload', methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.save(os.path.join('static/media/', photo.filename))
    return redirect(url_for('list_doc'))


@app.route("/download")
def download():
    CalcCode.gera_game()
    return redirect(url_for('static', filename='media/JOGO_GERADO.xlsx'))


@app.route('/construction')
def construction():
  return render_template('construction.html')



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
#app.run(host='0.0.0.0', port=8080)