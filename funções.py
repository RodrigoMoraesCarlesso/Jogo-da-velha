def escolhap(p):
    #Escolha do player e qual time ele escolhe X ou O
    while True:
        x = str(input(f'Player {p}: ')).strip()
        if x.isalpha():
            break
        else: print('Digite um nome válido (apenas letras)')
    while True:
        y = str(input('X ou O: ')).upper().strip()[0]
        if y not in 'XO':
            print('Digite um valor valido')
        else: break
    return {'nome' : x, 'time' : y}


def pos(list, time):
    #posição(Lista das posição, o que vai em cada posição X ou O)
    while True:
        x = int(input('Qual posição você quer jogar? '))
        if x in range(1, 10):
            for n in list:
                if x == n:
                    return [time, x]
        else: print('Digite um número valido')


def check(l, player):
    #Check(Lista das posições, time X ou O)
    if l[0] == l[1] == l[2]:
        print('-='*20)
        print(f'O jogador {player} ganhou!!!')
        print('-='*20)
        return False
    elif l[0] == l[4] == l[8]:
        print('-='*20)
        print(f'O jogador {player} ganhou!!!')
        print('-='*20)
        return False
    elif l[0] == l[3] == l[6]:
        print('-='*20)
        print(f'O jogador {player} ganhou!!!')
        print('-='*20)
        return False
    elif l[1] == l[4] == l[7]:
        print('-='*20)
        print(f'O jogador {player} ganhou!!!')
        print('-='*20)
        return False
    elif l[2] == l[4] == l[6]:
        print('-='*20)
        print(f'O jogador {player} ganhou!!!')
        print('-='*20)
        return False
    elif l[2] == l[5] == l[8]:
        print('-='*20)
        print(f'O jogador {player} ganhou!!!')
        print('-='*20)
        return False
    elif l[3] == l[4] == l[5]:
        print('-='*20)
        print(f'O jogador {player} ganhou!!!')
        print('-='*20)
        return False
    elif l[6] == l[7] == l[8]:
        print('-='*20)
        print(f'O jogador {player} ganhou!!!')
        print('-='*20)
        return False
    return True