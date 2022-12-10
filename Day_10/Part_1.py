with open("data_prod.txt") as data:
    ##Read data
    input_text = data.readlines()
    instructions = [ line.replace("\n", "") for line in input_text]
 


# Initial State, Cycle Number and Register State
X = 1
cycle = 1

#sate tracker [cycle :  signal strength]
state_tracker = {}


#during matters
for instruction in instructions:
    
    if instruction[:4] == "noop":
        
        state_tracker[cycle] = X*cycle
        cycle+=1
    
    else:
        
        state_tracker[cycle] = X*cycle
        cycle += 1
        state_tracker[cycle] = X*cycle
        cycle += 1
        delta = int(instruction.split()[1])
        X += delta
    
# get state for cycle 20+40X

sum = 0
for cycle in range(20, 221, 40):
  
    print(f"Cycle: {cycle}, Signal Strenght: {state_tracker[cycle]}")
    sum += state_tracker[cycle]

print(f"Part 1 answer is : {sum}")
