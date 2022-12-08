with open("data_prod.txt") as data:
    ##Read data
    input_text = data.readlines()
    input_lines = [ line.replace("\n", "") for line in input_text]
 
import numpy as np


# Create two array
for line in input_lines:
    tree_height_array = [int(ch) for ch in line]
    
    if line == input_lines[0]:
        
        tree_height_2d_array = np.array(tree_height_array)
        
    else:
        tree_height_2d_array = np.vstack( (tree_height_2d_array, np.array(tree_height_array)))
    
print(tree_height_2d_array.shape)



def check_grid(arr):
    answer_array = np.empty(shape=arr.shape)
    m, n  = arr.shape
    count = 0
    for i in range(m):
        for j in range(n):
            
            if j == 0 or i == 0 or j==n-1 or i==m-1:
                count +=1
                answer_array[i,j] = True
            #check from left or right or top or bottom avoid empty array
            elif  arr[i,j] > max(arr[i, :j]) or arr[i,j] > max(arr[i,j+1:]) or arr[i,j] > max(arr[:i, j]) or arr[i,j] > max(arr[i+1:, j]):
                count+=1
                answer_array[i,j] = True
            else:
                answer_array[i,j] = False
            
    return (count, answer_array)

count, boolean_arr  =  check_grid(tree_height_2d_array)

print("Part 1 answer: ",count)

def part_2_answer(arr):
    answer_array = np.empty(shape=arr.shape)
    m, n  = arr.shape
    
    
    for i in range(m):
        for j in range(n):
            top = 0
            bottom = 0
            left = 0
            right = 0
            #edge_Cases
            if  j == 0 or i == 0 or j==n-1 or i==m-1:
                if i==0:
                    top=0
                if j==0:
                    left=0
                if i==m-1:
                    bottom=0
                if j==n-1:
                    right=0
            else:
                #left
                for tree in np.flip(arr[i,:j]):
                    if arr[i,j] > tree: 
                        left+=1
                    else: 
                        left+=1
                        break
                    
                #right
                for tree in arr[i,j+1:]:
                    if arr[i,j] > tree: 
                        right+=1
                    else:
                        right+=1
                        break
                   
                #up
                for tree in np.flip(arr[:i,j]):
                    if arr[i,j] > tree: 
                        top+=1
                    else: 
                        top+=1
                        break
                    
                #down
                for tree in arr[i+1:,j]:
                    if arr[i,j] > tree: 
                        bottom+=1
                    else: 
                        bottom+=1
                        break
        
                    
            scenic_score = left*right*top*bottom
            
            answer_array[i,j] = scenic_score
    return int(np.amax(answer_array))

print("Part 2 answer:",part_2_answer(tree_height_2d_array))