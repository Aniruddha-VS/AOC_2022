from data_prod import data


rows = data.split('\n')

# print(len(rows))

hands_played = [ hand.split(" ") for hand in rows]

# print(hand_played)

def score_calculator(hand_played):
    
    score_array =[]
    
    for hand in hand_played:
        score_on_hand = 0
        #Win
        if hand[1] == "Z":
            score_on_hand += 6
            if hand[0] == "A":
                score_on_hand += 2
            elif hand[0] == "B":
                score_on_hand += 3
            else:
                score_on_hand += 1
        #Draw
        elif hand[1] == "Y":
            score_on_hand += 3
            if hand[0] == "A":
                score_on_hand += 1
            elif hand[0] == "B":
                score_on_hand += 2
            else:
                score_on_hand += 3
        #Loose
        else:
            if hand[0] == "A":
                score_on_hand += 3
            elif hand[0] == "B":
                score_on_hand += 1
            else:
                score_on_hand += 2
        score_array.append(score_on_hand)
        print(score_array)
    return sum(score_array)

print(score_calculator(hands_played))    
        
        