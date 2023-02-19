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

@app.route('/fileform')
def fileform():
    return render_template('fileform.html')

#------------------------------
@app.route('/list_doc')
def list_doc():
  read_table = CalcCode.read_df()
  title_read = read_table[1]
  read = read_table[0]

  qt_lin = len(read_table[0])
  qt_lin_ex = len(title_read)
  list_cont = np.arange(1, 100)
  
  return render_template('list-doc.html', qt_lin=qt_lin, read=read, list_cont=list_cont, title_read=title_read, qt_lin_ex=qt_lin_ex)


@app.route('/filltable', methods=['POST'])
def filltable():
  if request.method == 'POST':
    result = request.form
    qt_col_exist = int(result['colunas_exist'])
    qt_col = int(result['colunas'])
    #random_option = result['opt-rep']
    #qt_lin = int(result['hideen-num'])
    read_table = CalcCode.generation_num_table((qt_col + 1)-qt_col_exist)
    title_read = read_table[1]
    read = read_table[0]


  #return render_template('list-read.html', qt_lin=qt_lin, read=read, title_read=title_read)
  return render_template('list-read.html', read=read, title_read=title_read)

#------------------------------
@app.route('/list_gen')
def list_gen():
  list_cont = np.arange(1, 100)

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

    dez = []
    for a in result:
      if a != 'linha' and a != 'All':
        dez.append(a)

    table_listnum = []
    baseA, baseB = 1, 11
    for cont in range(0,10):
      table_listnum.append(list(np.arange(baseA,baseB)))
      baseA, baseB  = baseA + 10, baseB + 10

    qt_lin = int(result['linha'])
    # all_num = result['All']
    # dez_x = []
    # if all_num == 'All':
    #   for read in table_listnum:
    #     for a in read:
    #       dez_x.append(a)
    #   read_table = CalcCode.generation_num_col(qt_lin, dez_x)
    
    read_table = CalcCode.generation_num_col(qt_lin, dez)
    title_read = read_table[1]
    read = read_table[0]
    
  return render_template('list-read-num-col.html', read=read, title_read=title_read, table_listnum=table_listnum)


@app.route('/fillgen_num', methods=['POST'])
def fillgen_num():
  if request.method == 'POST':
    result = request.form

    table_listnum = []

    baseA, baseB = 1, 11
    for cont in range(0,10):
      table_listnum.append(list(np.arange(baseA,baseB)))
      baseA, baseB  = baseA + 10, baseB + 10

    dez = []
    for a in result:
      if a != 'linha' and a != 'All':
        dez.append(a)

    #qt_col = int(result['colunas'])
    #qt_lin = int(result['linha'])
    #qt_dez = int(result['dezena'])
    #dez = num_dez.split(';')

    read_table = CalcCode.generation_num_colx(dez)
    title_read = read_table[1]
    read = read_table[0]

  return render_template('list-read-num-col.html', read=read, title_read=title_read, table_listnum=table_listnum)


@app.route('/handleUpload', methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        #print('---------', photo)
        if photo.filename != '':
            #print('foi')
            photo.save(os.path.join('static/media/', photo.filename))
    return redirect(url_for('list_doc'))


@app.route("/download")
def download():
    CalcCode.gera_game()
    return redirect(url_for('static', filename='media/JOGO_GERADO.xlsx'))



if __name__ == '__main__':
  #app.run(host='0.0.0.0', port=8080, debug=True)
  app.run(host='127.0.0.1', port=5000, debug=True)
#app.run(host='0.0.0.0', port=8080)




'''
@app.route('/fileform', methods = ['POST', 'GET'])
def fileform():
  if request.method == 'POST':
    result = request.form
    print(result)

  return render_template('file-form.html')
'''

