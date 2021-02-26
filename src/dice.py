import random

def roll(num_dice):
  if num_dice < 1 or num_dice > 6:
    raise Exception(f"Must roll betwen 1 and 6 dice - attempted to roll {num_dice} dice")

  rolls = []
  for roll in range(num_dice):
    rolls.append(random.randint(0, 6))
    
  return rolls

