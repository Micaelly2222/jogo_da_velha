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


def start_board():
    """Inicia o tabuleiro"""
    return [""] * 9


def is_not_full(turn):
    return turn <= 8


def random_player():
    return random.choice(("x", "\u25EF"))


def print_board(board):
    """Função para exibir o tabuleiro"""
    print(f"{board[0]:^3s}|{board[1]:^3s}|{board[2]:^3s}  |   0 | 1 | 2 \n"
          f"{board[3]:^3s}|{board[4]:^3s}|{board[5]:^3s}  |   3 | 4 | 5 \n"
          f"{board[6]:^3s}|{board[7]:^3s}|{board[8]:^3s}  |   6 | 7 | 8 \n")


def select_movement(player, board):
    print_board(board)
    str_movement = input(f'(Jogador {player}) Selecione o movimento (Selecione um número de 0 até 8 inclusive):  ')
    try:
        int_movement = int(str_movement)
    except ValueError:
        print(f'{str_movement!r} não é um valor inteiro')
        return None
    if int_movement in range(9):
        return int_movement
    else:
        print(f'{str_movement!r} não está no intervalo')
        return None


def movement_is_valid(movement, board):
    # é jogada valida se espaco nao tiver ocupado
    movement_element = board[movement]
    return movement_element == ""


# marca a jogada
def do_movement(movement, board):
    pass


def player_won(player, board, turn, movement):
    # Ignorou completamente a nossa estratégia 👀
    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]):
        player_won = True
    elif (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]):
        player_won = True
    elif (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
        player_won = True
    else:
        player_won = False
    return player_won


board = start_board()  # Inicia o tabuleiro
winner = None
player = random_player()
turn = 0
while winner is None or is_not_full(turn):  # Enquanto ninguém ganhar ou ainda tiver espaço no tabuleiro:
    movement = select_movement(player, board)  # Jogador escolhe uma jogada
    if not movement_is_valid(movement, board):  # Se a jogada for inválida
        print("Jogada inválida, tente novamente")  # printa na tela mensagem de erro
        continue  # Reinicia o loop para o mesmo jogador
    do_movement(movement, board)  # Marca a jogada
    winner = player_won(player, board, turn, movement)  # Verifica se o jogador ganhou
    player = "X" if player == "\u25EF" else "\u25EF"  # Troca o jogador
    turn += 1
