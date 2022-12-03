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
# print(clean_data)
for line in clean_data:
    
    mid_point = int(len(line)/2)
    
    # print(mid_point)
    
    first_half = set(list(line[:mid_point]))
    second_half = set(list(line[mid_point:]))
    
    # print(first_half, "   ", second_half)
    
    common_char = set.intersection(first_half, second_half)
    
    score_array.append(priority_dict[common_char.pop()])
                    
print(sum(score_array))
    
