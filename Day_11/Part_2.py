class Monekey:
    
    #Initializing monkey
    def __init__(self, id, items, operation, operation_with, test_divisibility,if_true_throw_to, if_false_throw_to):
        self.id = id
        self.items = items
        self.operation = operation
        self.operation_with = operation_with
        self.test_divisibility = test_divisibility
        self.if_true_throw_to = if_true_throw_to #[if_true, If False]
        self.if_false_throw_to = if_false_throw_to
        self.items_handled = 0
    
    def do_operation(self, current_worry):
        
        operand = self.operation_with
        if operand == "self":
            operand = current_worry
        if self.operation == "+":
            new_worry = current_worry + operand
        elif self.operation == "*":
            new_worry = current_worry * operand
        
        #getting borred
        # new_worry = int(new_worry /3)
        return  new_worry
    
    #void function does not return anything
    def catch_item(self, item):
        self.items.append(item)
    
    #void function does not return anything
    def empty_items(self):
        self.items = []
    
    def throw_tos(self):
        
        throw_to = []
        
        
        for item in self.items:
            self.items_handled += 1
            new_worry = self.do_operation(item)
            
            if new_worry % self.test_divisibility == 0:
                # print("divisibility true")
                throw_to.append((new_worry, self.if_true_throw_to))
                
            else:
                # print("divisibility false")
                throw_to.append((new_worry, self.if_false_throw_to))
            
        # print(throw_to)
        self.empty_items()
        
        return throw_to
        

with open("data_prod.txt") as data:
    ##Read data
    input_text = data.read()
    monkey_collection = input_text.split("\n\n")
        
        
monkey_objects = []
for monkey in monkey_collection:
    
    instructions = monkey.splitlines()
    
    for i in range(len(instructions)):
        
        if i == 0:
            id = int(instructions[i].split(" ")[1][:-1])
        elif i == 1:
            string_with_items = instructions[i].split(": ")[1].split(", ")
            items = [int(item) for item in string_with_items]
        elif i == 2:
            operation_string = instructions[i].split(" = old ")[1]
            operand = operation_string.split(" ")[0]
            if operation_string.split(" ")[1] != "old":
                operation_with = int(operation_string.split(" ")[1])
            else:
                operation_with = "self"
        elif i == 3:
            divisibility_check = int(instructions[i].split("by ")[1])
        elif i == 4:
            if_true = int(instructions[i].split("monkey ")[1])
        else:
            if_false = int(instructions[i].split("monkey ")[1])
    
    
    # print(f"{id}, {items}, {operand}, {operation_with}, {divisibility_check} {if_true} {if_false}")
    monkey_objects.append(Monekey(id=id, items=items,operation=operand, operation_with=operation_with, test_divisibility = divisibility_check, if_true_throw_to=if_true,if_false_throw_to=if_false))

mod = 1
for monkey in monkey_objects:
    mod *= monkey.test_divisibility

# Go 20 rounds
for curr_round in range(1,10001):
    for i in range(len(monkey_objects)):
        
        monkey_objects[i].items = [ item % mod for item in monkey_objects[i].items]
        throw_to = monkey_objects[i].throw_tos()
        
        for item, to in throw_to:
            monkey_objects[to].catch_item(item)
    
    # print(f"Round {curr_round}")
    # for monkey in monkey_objects:
    #     print(f"Monkey {monkey.id}: {monkey.items}")
    # print("\n")
    
handled_count = []
for monkey in monkey_objects:
    handled_count.append(monkey.items_handled)
    print(f"Monkey {monkey.id} inspected items {monkey.items_handled} times")
    
handled_count.sort(reverse=True)

print(f"Monkey Business = {handled_count[0]*handled_count[1]}")

        
        
            
    