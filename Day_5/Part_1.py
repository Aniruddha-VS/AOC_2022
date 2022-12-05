with open("data_prod.txt") as data:
    ##Read data
    input_text = data.read()


# 1. Seperating stack_diagram and instructions
stack_diagram, instructions = input_text.split("\n\n")

stack_diagram_to_seperate_lines = stack_diagram.split("\n")

# calcuate number of stacks required
max_index = len(stack_diagram_to_seperate_lines[-1])
number_of_stacks = int(stack_diagram_to_seperate_lines.pop().strip().split(" ")[-1])

# calculate stack data location in lines
dictionary_of_stack_locations ={ k:v for (k,v) in zip(range(1,number_of_stacks+1), range(1,max_index,4))}
print(dictionary_of_stack_locations)


collection_of_stacks = []

for stack in range(number_of_stacks):
    collection_of_stacks.append([])


for line in stack_diagram_to_seperate_lines[::-1]:
    for key in dictionary_of_stack_locations:
        if line[dictionary_of_stack_locations[key]] != " ":
            collection_of_stacks[key-1].append(line[dictionary_of_stack_locations[key]])
        
    
    
print("Initial State")
for stack in collection_of_stacks:
    print(stack)

# get out information
instructions = instructions.splitlines()

for instruction in instructions:
    elements = instruction.split(" ")
    how_many = int(elements[1])
    from_where = int(elements[3]) - 1 #index starts from 0
    to_where = int(elements[5]) - 1 #index starts from 0
    
    for _ in range(how_many):
        collection_of_stacks[to_where].append(collection_of_stacks[from_where].pop())
        
print("Final State")

solution = []
for stack in collection_of_stacks:
    solution.append(stack[-1])
    
print("answer is: ", "".join(solution))



    