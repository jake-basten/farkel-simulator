import dice

class Turn:

  REMOVED_DIE = -1
  THREE_OF_A_KIND_SCORES = {
      1: 1000,
      2: 200,
      3: 300,
      4: 400,
      5: 500,
      6: 600
    }

  def __init__(self):
    self.dice = [1, 1, 1, 2, 2, 2]
    self.score_for_turn = 0


  def take_turn(self):
    print("dice", self.dice)
    moves = self.score_three_of_a_kind()
    print("moves", moves)
  
  def score_ones(self):
    return self.score_single_number(1, 100)

  
  def score_fives(self):
    return self.score_single_number(5, 50)


  def score_three_of_a_kind(self):
    moves = []
    score = 0
    order = [1, 6, 5, 4, 3, 2]
    remaining_dice = self.dice
    for num in order:
      matches = filter(lambda die: die == num, self.dice)
      if len(list(matches)) >= 3:
        remaining_dice = self.remove_first_three(num)
        score += self.THREE_OF_A_KIND_SCORES[num]
        moves.append(self.build_move(remaining_dice, score))
        if remaining_dice == 0:
          break
    return moves

  
  def remove_first_three(self, num):
    count = 0
    remaining_dice = self.dice
    for idx, die in enumerate(remaining_dice):
      if count == 3:
        break
      elif die == num:
        remaining_dice[idx] = self.REMOVED_DIE
        count += 1
    return remaining_dice

  def score_single_number(self, number, score_value):
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