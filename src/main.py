import dice
import players
from turn import Turn


def play_game():
    print('starting game')
    Turn().take_turn()


if __name__ == "__main__":
    play_game()
