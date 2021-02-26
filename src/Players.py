class Player:

  def __init__(self, name):
    self.name = name
    self.score = 0

  def __str__(self):
    return f"{self.name}: {self.score}"

  def add_to_score(self, points):
    self.score += points

  def has_score_to_win(self, score_to_win):
    return self.score >= score_to_win


players = []

def initialize():
  players.append(Player('Jake'))
  players.append(Player('Jeff'))
  return players

def print_scores():
  for player in players:
    print(str(player))