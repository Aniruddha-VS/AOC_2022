with open("data_prod.txt") as data:
    ##Read data
    input_text = data.readlines()
    instructions = [ line.replace("\n", "") for line in input_text]
 


# Initial State, Cycle Number and Register State
X = 1
cycle = 1

#sate tracker [cycle :  signal strength]
register_state_tracker = {}


#during matters
for instruction in instructions:
    
    if instruction[:4] == "noop":
        
        register_state_tracker[cycle] = X
        cycle+=1
    
    else:
        
        register_state_tracker[cycle] = X
        cycle += 1
        register_state_tracker[cycle] = X
        cycle += 1
        delta = int(instruction.split()[1])
        X += delta
    

CRT_dictionary = {}

#make list of 4 dictoiornaries
rows = []
register_values = list(register_state_tracker.values())
print(len(register_values))
for i in range(int(len(register_values)/40)):
    
    start_idx = i *40
    end_idx = start_idx + 40
    rows.append(register_values[start_idx:end_idx])

display_str = ""
for row in rows:
    
    for crt_position in range(len(row)):   # crt_position = 0,1,2,....,39
        
        
        
        register_value = row[crt_position]       # row contains 40 register values
        
        spirte_locations = [ register_value -1, register_value, register_value+1 ]
        
        if crt_position in spirte_locations:
            display_str += "#"
        else:
            display_str += "."
        
    print(display_str)
    display_str = ""
    
