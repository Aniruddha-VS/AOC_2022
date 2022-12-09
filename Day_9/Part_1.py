with open("data_prod.txt") as data:
    ##Read data
    input_text = data.readlines()
    input_lines = [ line.replace("\n", "") for line in input_text]
 
import numpy as np

instructions = []
# Create two array
for line in input_lines:
    direction, number_of_steps = line.split(" ")
    number_of_steps = int(number_of_steps)
    instructions.append([direction, number_of_steps])

def give_tail_history(instructions):
    
    #set initial position as 0,0
    head_x_coor = 0
    head_y_coor = 0
    
    tail_x_coor = 0
    tail_y_coor = 0
    
    tail_position_history = []
    tail_position_history.append((tail_x_coor,tail_y_coor))
    #let start moving
    
    for instrction in instructions:
        
        direction, steps = instrction[0], instrction[1]
        
        
        for _ in range(steps):
            
            if direction == "R":
                head_x_coor += 1
            elif direction == "L":
                head_x_coor -= 1
            elif direction == "U":
                head_y_coor += 1
            else:
                head_y_coor -= 1
            
            #Get latest tail position
            if head_x_coor - tail_x_coor == 2:
                tail_x_coor += 1
                if head_y_coor != tail_y_coor:
                    tail_y_coor = head_y_coor
            elif head_x_coor - tail_x_coor == -2:
                tail_x_coor +=-1
                if head_y_coor != tail_y_coor:
                    tail_y_coor = head_y_coor
            elif head_y_coor - tail_y_coor == 2:
                tail_y_coor += 1
                if head_x_coor != tail_x_coor:
                    tail_x_coor = head_x_coor
            elif head_y_coor - tail_y_coor == -2:
                tail_y_coor +=-1
                if head_x_coor != tail_x_coor:
                    tail_x_coor = head_x_coor
            
            tail_position_history.append((tail_x_coor,tail_y_coor))
            
    unique_positions = len(set(tail_position_history)) #for the starting position
    
    return set(tail_position_history)

arr = give_tail_history(instructions=instructions)

x_max, x_min, y_max, y_min = -9999999999,9999999999,-9999999999,9999999999
for x,y in arr:
    if x > x_max:
        x_max = x
    if x < x_min:
        x_min = x
    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y
        
print(x_max," ",x_min)
print(y_max," ",y_min)

final = []
arr = sorted(list(arr))

    
print(len(arr))
