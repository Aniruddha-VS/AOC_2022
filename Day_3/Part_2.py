from string import ascii_letters

## create priority dictionary {"a": 1, ... "Z" : 52}
priority_dict = dict(zip(ascii_letters, range(1,53)))
# print(priority_dict)

with open("data_prod.txt") as data:
    ##Read data
    lines = data.readlines()
    
    ##Get rid of "\n" 
    clean_data = [line.replace("\n","") for line in lines]

score_array = []
for i in range(0,len(clean_data),3):
    member_1 = set(list(clean_data[i]))
    member_2 = set(list(clean_data[i+1]))
    member_3 = set(list(clean_data[i+2]))
    
    
    badge_item = set.intersection(member_1, member_2, member_3)
    
    score_array.append(priority_dict[badge_item.pop()])

print(sum(score_array))
    
    
