import dice

class Turn:

  REMOVED_DIE = -1

  def __init__(self):
    self.dice = dice.roll(6)

  def take_turn(self):
    moves = self.ones()
    print(moves)

  def ones(self):
    print("dice", self.dice)

    ones = []
    for i, die in enumerate(self.dice):
      if die == 1:
        ones.append(i)
    
    if not ones:
      return []

    print("ones", ones)

    score = 0
    moves = []
    remaining_dice = self.dice
    for one in ones:
      remaining_dice[one] = self.REMOVED_DIE
      score += 100
      moves.append(self.build_move(remaining_dice, score))
    return moves


  def build_move(self, dice, score):
    filtered_dice = filter(lambda die: die != self.REMOVED_DIE, dice)
    return {
      "score": score,
      "remaining": list(filtered_dice)
    }