import dice

def play_game():
  print('starting game')
  
  rolls = dice.roll(6)
  print(rolls)


if __name__ == "__main__":
  play_game()