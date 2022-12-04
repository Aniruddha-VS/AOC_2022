with open("data_prod.txt") as data:
    ##Read data
    lines = data.readlines()
    
##Get rid of "\n" 
data_array = [line.replace("\n","") for line in lines]


def beautify_my_data(arr):
    # seperating pairs
    separate_pairs = [data_point.split(",") for data_point in arr]
    
    # extracting individual section assignments
    section_assignments = [[ item.split("-") for item in pair] for pair in separate_pairs]
    
    section_assignment_sets = []
    for pair in section_assignments:
        section_assignment_sets.append(list(map(lambda elve: set(range(int(elve[0]), int(elve[1])+1)), pair)))
    
    return section_assignment_sets

final_format = beautify_my_data(data_array)


# Part 1
count = 0
for data in final_format:
    if data[0].issuperset(data[1]) or data[1].issuperset(data[0]):
        count+=1

# Part 1 solution      
print(count)

# Part 2
is_overlap = list(map(lambda element:not(element[1].isdisjoint(element[0])), final_format))

# Part 2 Solution
print(sum(is_overlap))
