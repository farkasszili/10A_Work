board = [' ' for _ in range(10)]


def draw():
    row1 = '| {} | {} | {} |'.format(board[1], board[2], board[3])
    row2 = '| {} | {} | {} |'.format(board[4], board[5], board[6])
    row3 = '| {} | {} | {} |'.format(board[7], board[8], board[9])

    print(row1)
    print(row2)
    print(row3)


def check_win():
    nyeresi_lehetosegek = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

    for condition in nyeresi_lehetosegek:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]

    if ' ' not in board[1:10]:
        return 'T'

    return False


def start():
    current_player = 'x'
    while True:
        draw()
        move = input('\n{}-s Játékos: Kérlek add meg a következő lépést (1-9): '.format(current_player))
        if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move)] != ' ':
            print('Nem szabályos mozgás. Próbáld meg újra!')
            continue

        board[int(move)] = current_player
        result = check_win()
        if result:
            draw()
            if result == 'T':
                print('Döntetlen!')
            else:
                print('{} játékos nyert!'.format(current_player))
            break

        current_player = 'o' if current_player == 'x' else 'x'


def info():
    print("Üdvözöllek a TicTacToe világában!")
    print("A mozgási lehetőségeket az alábbi ábrán találod:\n")
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |\n')
    start()


info()
