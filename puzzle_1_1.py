from Data_1 import data

data_1_array = data.split("\n")[1:]

data_1_array.append("")


calorie_sum_array = []
sum_ = 0


for item in data_1_array:
    if item =="":
        calorie_sum_array.append(sum_)
        sum_ = 0
    else: 
        sum_+=int(item)
        
calorie_sum_array.sort(reverse=True)
top_3_elves = calorie_sum_array[:3]
print(sum(top_3_elves))
        

