from data_prod import data

# A -> X (2+6 = 8)
# B -> Y (1+0 = 1)
# C -> Z (3+3 = 6)

rows = data.split('\n')

# print(len(rows))

hands_played = [ hand.split(" ") for hand in rows]

# print(hand_played)

def score_calculator(hand_played):
    score_array =[]
    
    for hand in hand_played:
        score_on_hand = 0
        if hand[1] == "X":
            score_on_hand += 1
        elif hand[1] == "Y":
            score_on_hand += 2
        elif hand[1] == "Z":
            score_on_hand += 3
        #Draws
        if (hand[0] == "A" and hand[1] == "X") or (hand[0] == "B" and hand[1] == "Y") or (hand[0] == "C" and hand[1] == "Z"):
            score_on_hand += 3
        #Wins
        elif (hand[1] == "X" and hand[0]== "C") or (hand[1] == "Y" and hand[0]== "A") or (hand[1] == "Z" and hand[0]== "B"):
            score_on_hand += 6
        else:
            score_on_hand += 0
        score_array.append(score_on_hand)
    return sum(score_array)

print(score_calculator(hands_played))
