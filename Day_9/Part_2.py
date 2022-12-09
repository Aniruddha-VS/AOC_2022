with open("data_prod.txt") as data:
    ##Read data
    input_text = data.readlines()
    input_lines = [ line.replace("\n", "") for line in input_text]
 

instructions = []
# Create two array
for line in input_lines:
    direction, number_of_steps = line.split(" ")
    number_of_steps = int(number_of_steps)
    instructions.append((direction, number_of_steps))
    
def get_final_state(head, tail):
    
    head_x_coor, head_y_coor = head
    tail_x_coor, tail_y_coor = tail
    
    # we do not need to update anything is they are still touching
    if abs(head_x_coor - tail_x_coor) < 2 and abs(head_y_coor - tail_y_coor) < 2:
        return (head, tail)
    
    #top moving diagonally
    dx, dy = head_x_coor - tail_x_coor, head_y_coor - tail_y_coor
    if dx == 2 and dy == 2:
        tail_x_coor += 1
        tail_y_coor += 1
        tail = (tail_x_coor, tail_y_coor)
        return(head, tail)
    elif dx == -2 and dy ==2:
        tail_x_coor += -1
        tail_y_coor += 1
        tail = (tail_x_coor, tail_y_coor)
        return(head, tail)
    elif dx == 2 and dy == -2:
        tail_x_coor += 1
        tail_y_coor += -1
        tail = (tail_x_coor, tail_y_coor)
        return(head, tail)
    elif dx == -2 and dy == -2:
        tail_x_coor += -1
        tail_y_coor += -1
        tail = (tail_x_coor, tail_y_coor)
        return(head, tail)
        
    
    # straight movement of head
    # right
    if head_x_coor - tail_x_coor == 2:
        tail_x_coor += 1
        if head_y_coor != tail_y_coor:
             tail_y_coor = head_y_coor
    # left
    elif head_x_coor - tail_x_coor == -2:
        tail_x_coor +=-1
        if head_y_coor != tail_y_coor:
             tail_y_coor = head_y_coor
    # up
    elif head_y_coor - tail_y_coor == 2:
        tail_y_coor += 1
        if head_x_coor != tail_x_coor:
            tail_x_coor = head_x_coor
    #down
    elif head_y_coor - tail_y_coor == -2:
        tail_y_coor +=-1
        if head_x_coor != tail_x_coor:
            tail_x_coor = head_x_coor
                
    head = (head_x_coor, head_y_coor)
    tail = (tail_x_coor, tail_y_coor)
    
    return(head, tail)

def give_tail_history(instructions):
        
    #initial start position of all knots is 0,0
    knots = [(0,0) for i in range(10)] #starting positions of each knot
    
    #track tail position on each instructions each step
    tail_positions = []
    
    #add initial position right away
    tail_positions.append(knots[-1])
    
    # For each intruction
    for instruction in instructions:
            
        direction, steps = instruction
        
        # For each step we have to update every knot
        for _ in range(steps):
            
            #lets start moving
            for i in range(len(knots)-1):
                
                #Start from head couple going in downward direction
                head = knots[i]
                tail = knots[i+1]
            
                head_x_coor, head_y_coor = head                
                # direction of head will be determined by instructions, other will follow head
                if i==0:
                    
                    if direction == "R":
                        head_x_coor += 1
                    elif direction == "L":
                        head_x_coor -= 1
                    elif direction == "U":
                        head_y_coor += 1
                    elif direction == "D":
                        head_y_coor -= 1
                    #updated head position
                    head = (head_x_coor, head_y_coor)
                if direction == "U" and steps == 4:
                    print(f"\nBe : i : {i} Head : {head} Tail : {tail}")  
                #get final position by passing the couples initial position to 
                knots[i], knots[i+1] = get_final_state(head, tail)
                
                if direction == "U" and steps == 4:
                    print(f"Af : i : {i} Head : {knots[i]} Tail : {knots[i+1]}")
                
                # on the last couple append tail position
                if i == len(knots)-2:
                    tail_positions.append(knots[i+1])
            if direction == "U" and steps == 4:
                print("\n")
        print(f"{instruction}\n")
        disply_str = ""
        for knot in knots:
            disply_str += f" {knot} "
        print(disply_str, "\n")
                            
    return set(tail_positions)

arr = give_tail_history(instructions=instructions)


arr = sorted(list(arr))

print(len(arr))