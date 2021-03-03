import dice


def has_straight(roll_from_dice):
    roll_from_dice.sort()
    for num in range(1, 7):
        if num != roll_from_dice[num - 1]:
            return False
    return True


def has_three_pair(pairs_dict):
    dict_values = list(pairs_dict.values())
    if len(dict_values) != 3:
        return False
    for value in dict_values:
        if value != 2:
            return False
    return True


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
        self.dice = [1, 4, 6, 6, 1, 4]
        self.score_for_turn = 0
    
    def take_turn(self):
        print("dice", self.dice)
        moves = self.score_three_pair()
        print("moves", moves)
    
    def score_ones(self):
        return self.score_single_number(1, 100)
    
    def score_fives(self):
        return self.score_single_number(5, 50)
    
    def score_single_number(self, number, score_value):
        indices_with_number = []
        for i, die in enumerate(self.dice):
            if die == number:
                indices_with_number.append(i)
        
        if not indices_with_number:
            return []
        
        score = 0
        moves = []
        remaining_dice = self.dice
        for idx in indices_with_number:
            remaining_dice[idx] = self.REMOVED_DIE
            score += score_value
            moves.append(self.build_move(remaining_dice, score))
        return moves
    
    def score_three_of_a_kind(self):
        moves = []
        score = 0
        order = [1, 6, 5, 4, 3, 2]
        remaining_dice = self.dice
        for num in order:
            matches = filter(lambda die: die == num, remaining_dice)
            if len(list(matches)) >= 3:
                remaining_dice = self.remove_first_three(num)
                score += self.THREE_OF_A_KIND_SCORES[num]
                moves.append(self.build_move(remaining_dice, score))
                if remaining_dice == 0:
                    break
        return moves
    
    def score_straight(self):
        if has_straight(self.dice):
            return [{
                "score": 3000,
                "remaining": []
            }]
        return []
    
    def score_three_pair(self):
        pairs_dict = {}
        for die in self.dice:
            if die in pairs_dict:
                pairs_dict[die] = pairs_dict[die] + 1
            else:
                pairs_dict[die] = 1
        if has_three_pair(pairs_dict):
            return [{
                "score": 1500,
                "remaining": []
            }]
        return []
    
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
    
    def build_move(self, dice_from_move, score):
        filtered_dice = filter(lambda die: die != self.REMOVED_DIE, dice_from_move)
        return {
            "score": score,
            "remaining": list(filtered_dice)
        }
