


    dez = []    
    for a in result:
      if 'all' in a:
        test = 'all'
        for read in table_listnum:
          for a in read:
            dez.append(a)

      elif 'mega' in a:
        table_listnum = list(np.arange(1,61))
        print('>>>', table_listnum)
        for read in table_listnum:
          dez.append(a)

      elif 'loto' in a:
        table_listnum = list(np.arange(1,26))
        for read in table_listnum:
          dez.append(a)

      else:
        print('ops')
        if a != 'linha' and a != 'all' and a != 'mega' and a != 'loto':
          dez.append(a)