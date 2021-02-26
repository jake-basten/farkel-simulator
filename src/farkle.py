import Dice
import Players

def play_game():
  print('starting game')
  
  rolls = Dice.roll(6)
  print(rolls)

  players = Players.initialize()
  Players.print_scores()

if __name__ == "__main__":
  play_game()