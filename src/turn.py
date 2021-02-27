import dice

class Turn:

  REMOVED_DIE = -1

  def __init__(self):
    self.dice = dice.roll(6)


  def take_turn(self):
    print("dice", self.dice)
    moves = self.score_for_number_of_dice(5, 50)
    print("moves", moves)


  def score_for_number_of_dice(self, number, score_value):
    indecies_with_number = []
    for i, die in enumerate(self.dice):
      if die == number:
        indecies_with_number.append(i)
    
    if not indecies_with_number:
      return []

    score = 0
    moves = []
    remaining_dice = self.dice
    for idx in indecies_with_number:
      remaining_dice[idx] = self.REMOVED_DIE
      score += score_value
      moves.append(self.build_move(remaining_dice, score))
    return moves


  def build_move(self, dice, score):
    filtered_dice = filter(lambda die: die != self.REMOVED_DIE, dice)
    return {
      "score": score,
      "remaining": list(filtered_dice)
    }