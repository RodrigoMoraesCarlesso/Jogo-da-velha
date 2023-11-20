from funções import escolhap, pos, check
terminar = True
while terminar:
       n1 = 1 
       n2 = 2
       n3 = 3
       n4 = 4
       n5 = 5
       n6 = 6
       n7 = 7
       n8 = 8
       n9 = 9
       lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

       print('=-' * 20)
       print('--- Jogo da Velha ---'.center(40))
       print('=-' * 20)

       p1 = escolhap(1)
       p2 = escolhap(2)
       while True:
              if p2['time'] == p1['time']:
                     print(f'Você digitou o mesmo time do {p1['nome']}, tente novamente ', end='')
                     p2 = escolhap(2)
              if p2['time'] != p1['time']:
                     break
       t1 = p1['time']
       t2 = p2['time']
  
       c = 0
       primeiro = True
       game = True
       while game:
              #Jogador1
              if primeiro == True:
                     print(f'''
            |           | 
            |           |
     {lista[0]}      |     {lista[1]}     |      {lista[2]}
            |           |
____________|___________|_____________
            |           | 
            |           |
     {lista[3]}      |     {lista[4]}     |      {lista[5]}
            |           |     
____________|___________|____________
            |           | 
            |           |
     {lista[6]}      |     {lista[7]}     |      {lista[8]}
            |           |   
            |           |               ''')
              primeiro = False 
              print(f'Jogador {p1['nome']}: ', end='')
              jogada1 = pos(lista, t1) #returna time e posição ['x', '2']
              lista[jogada1[1]-1] = f'\033[37;41m{jogada1[0]}\033[m'
              print(f'''
            |           | 
            |           |
     {lista[0]}      |     {lista[1]}     |      {lista[2]}
            |           |
____________|___________|_____________
            |           | 
            |           |
     {lista[3]}      |     {lista[4]}     |      {lista[5]}
            |           |     
____________|___________|____________
            |           | 
            |           |
     {lista[6]}      |     {lista[7]}     |      {lista[8]}
            |           |   
            |           |               ''')
    
              c += 1
              game = check(lista, t1)
              if game == False:
                     break
              if game == True:
                     if c >= 9:
                            print('Deu velha :(')
                            break

              #Jogador2
              print(f'Jogador {p2['nome']}: ', end='')
              jogada2 = pos(lista, t2)
              lista[jogada2[1]-1] = f'\033[37;44m{jogada2[0]}\033[m'
              print(f'''
            |           | 
            |           |
     {lista[0]}      |     {lista[1]}     |      {lista[2]}
            |           |
____________|___________|_____________
            |           | 
            |           |
     {lista[3]}      |     {lista[4]}     |      {lista[5]}
            |           |     
____________|___________|____________
            |           | 
            |           |
     {lista[6]}      |     {lista[7]}     |      {lista[8]}
            |           |   
            |           |               ''')
              c += 1
              game = check(lista, t2)
              if game == False:
                     break
       esc = 0
       while True:
              esc = int(input('Gostaria de jogar mais uma partida? 1 = SIM, 2 = NÃO: '))
              if esc == 1:
                     print('Certo, vamos novamente...')
                     break
              elif esc == 2:
                     print('Obrigado por jogar')
                     terminar = False
                     break

