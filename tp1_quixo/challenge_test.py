import random

from tp1_quixo.quixo_wyry import QuixoPlayerWyry, h_potentially_improving_lines, Quixo, PLAYER1, PLAYER2, \
    valid_moves_player, Move, print_board, NEUTRAL, h_potentially_improving_lines_overdosed as h_dan


class IdiotPlayer(QuixoPlayerWyry):
    def __init__(self):
        super().__init__(None, None)

    def playerPlay(self) -> Move:
        move = random.choice(
            valid_moves_player(self.board,PLAYER1)
        )
        self._play(PLAYER1,move)
        return move

player1 = QuixoPlayerWyry(h_dan,3)
# player2 = QuixoPlayerWyry(h_dan,3)
player2 = IdiotPlayer()
game = Quixo()
player = PLAYER1
i = 0
while game.game_over() == NEUTRAL:
    i +=1
    print("Player %s turn.." % (1 if player == PLAYER1 else 2))
    if player == PLAYER1:
        move = player1.playerPlay()
        print(move)
        player2.oponentPlay(move)
        game._play(PLAYER1, move)
    else:
        move = player2.playerPlay()
        # print(move)
        player1.oponentPlay(move)
        game._play(PLAYER2, move)

    player = player * -1
    # print("Player1 board")
    # print_board(player1.board)
    # print("Player2 board")
    # print_board(player2.board)

    print("Game board")
    print_board(game.board)

print("Winner is player %s." % (1 if game.game_over() == PLAYER1 else 2))
print("In %s moves." % i)
