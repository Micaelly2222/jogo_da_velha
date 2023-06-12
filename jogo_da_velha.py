"""
Pseudo-Algoritmo do código
```
Inicia o tabuleiro
Enquanto ninguém ganhar ou ainda tiver espaço no tabuleiro:
    Jogador escolhe uma jogada
    Se a jogada for inválida
        printa na tela mensagem de erro
        Reinicia o loop para o mesmo jogador
    Marca a jogada
    Verifica se o jogador ganhou
    Troca o jogador
```
"""

import random
# módulo que gera números aleatorios

CRITICAL_GROUPS = [
  {0, 1, 2},
  {3, 4, 5},
  {6, 7, 8},
  {0, 3, 6},
  {1, 4, 7},
  {2, 5, 8},
  {0, 4, 8},
  {2, 4, 6},
]




def start_board():
    """Inicia o tabuleiro"""
    return [""] * 9
# retorna uma lista com 9 strings vazias

def is_not_full(turn):
   """verifica se tem espaço no tabuleiro """
    return turn <= 8


def random_player():
  """seleciona jogador aleatorio, sendo o x ou 0 """
    return random.choice(("X", "\u25EF"))


def print_board(board):
    """Função para exibir o tabuleiro"""
    print(f"{board[0]:^3s}|{board[1]:^3s}|{board[2]:^3s}  |   0 | 1 | 2 \n"
          f"{board[3]:^3s}|{board[4]:^3s}|{board[5]:^3s}  |   3 | 4 | 5 \n"
          f"{board[6]:^3s}|{board[7]:^3s}|{board[8]:^3s}  |   6 | 7 | 8 \n")


def select_movement(player, board):
   """recebe a jogada e exibe o tabuleiro e qual é o jogador"""
    print_board(board)
    str_movement = input(f'(Jogador {player}) Selecione o movimento (Selecione um número de 0 até 8 inclusive):  ')
    try: # tratando o erro caso o jogador escolha algum numero que nao seja inteiro
        # >>>> o tratamento de erro é só se for inserido um float?
        int_movement = int(str_movement) # verifica e converte a entrada para um inteiro  
    except ValueError:  # vai exibir essa mensagem se houver a exceção(se nao for o inteiro)
        print(f'{str_movement!r} não é um valor inteiro')
        return None
    if int_movement in range(9): #  retorna o numero se estiver no intervalo selecionado, se não estiver no intervalo exibe uma mensagem de erro
        return int_movement
    else:
        print(f'{str_movement!r} não está no intervalo')
        return None


def movement_is_valid(movement, board):
   """verifica se a jogada é valida"""
    # é jogada valida se espaco nao tiver ocupado
    movement_element = board[movement]
    return movement_element == ""


# marca a jogada
def do_movement(movement, board, player):
    board[movement] = player


def player_won_old(player, board, turn, movement):
    if (board[0] == board[1] == board[2] != '') or (board[3] == board[4] == board[5] != '') or (board[6] == board[7] == board[8] != ''):
        winner = player
    elif (board[0] == board[3] == board[6] != '') or (board[1] == board[4] == board[7] != '') or (board[2] == board[5] == board[8] != ''):
        winner = player
    elif (board[0] == board[4] == board[8] != '') or (board[2] == board[4] == board[6] != ''):
        winner = player
    else:
        winner = None
    return winner
  
  
def player_won(player, board, turn, movement):
    if turn < 4:
        return None
    for group in CRITICAL_GROUPS:
        if movement in group:
           if all([board[x] == player for x in group]):
                return player
    return None

  
board = start_board()  # Inicia o tabuleiro
winner = None
player = random_player() # jogador aleatorio
turn = 0
while winner is None and is_not_full(turn):  # Enquanto ninguém ganhar ou ainda tiver espaço no tabuleiro:
    movement = select_movement(player, board)  # Jogador escolhe uma jogada
    #número de 0 a 8
    if not movement_is_valid(movement, board):  # Se a jogada for inválida
        print("Jogada inválida, tente novamente")  # printa na tela mensagem de erro
        continue  # Reinicia o loop para o mesmo jogador
    do_movement(movement, board, player)  # Marca a jogada
    winner = player_won(player, board, turn, movement)  # Verifica se o jogador ganhou
    player = "X" if player == "\u25EF" else "\u25EF"  # Troca o jogador
    turn += 1
    # Acabou
if winner is None:
    print("velha")
else:
    print(f"{winner} é o vencedor")
