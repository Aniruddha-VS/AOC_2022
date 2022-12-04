# Lengthy way...
with open("data_prod.txt") as data:
    ##Read data
    lines = data.readlines()
    
##Get rid of "\n" 
data_array = [line.replace("\n","") for line in lines]

separated_pair = list(map(lambda x: x.split(","), data_array))

section_assignments = [[ item.split("-") for item in pair] for pair in separated_pair]

        
# print(section_assignments)
fully_contain_list = []
fully_contain_count = 0
for pair in section_assignments:
    # first subset of second
    if (int(pair[0][0]) >= int(pair[1][0])) and (int(pair[0][1]) <= int(pair[1][1])):
        fully_contain_list.append(pair)
        fully_contain_count += 1
        # print(pair, "+")
    # second subset of first
    elif (int(pair[0][0]) <= int(pair[1][0])) and (int(pair[0][1]) >= int(pair[1][1])):
        fully_contain_list.append(pair)
        fully_contain_count += 1
        # print(pair)

print(fully_contain_count)
        
        
