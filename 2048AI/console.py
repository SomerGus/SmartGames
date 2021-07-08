from lib.Grid import Grid, Moves
from lib.AI import AI
from time import time

game = Grid()
Ai = AI(multi_core=True)
N_GAMES = 1

def main():
    start = time()
    while True:
        if not game.move(Ai.next_move(game, N_GAMES)):
            print(game)
            print(f"Finished with a score of: {game.score()} in {round((time() - start)/60, 2)} minutes!")
            break
        print(game)


if __name__ == '__main__':
    main()