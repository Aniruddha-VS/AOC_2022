class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.files = []
        self.parent = None

    def add_file(self, name, size):
        self.files.append((name, size))
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level +=1
        return level
    
    def add_child(self, child):
        if child not in self.children:
            child.parent = self
            self.children.append(child)
        
    def print_tree(self):
        print(self.get_level()*" "*3 + self.data + "  (dir)")
        if len(self.files):
            for name, size in self.files:
                print("   "+ self.get_level()*" "*3 + name + f"  (file): {size}")
        # if len(self.files):
        #     for file in self.files:
        #         print(" "+ self.get_level()*" "*3 +file + f"  (file): {type(file)}")
        if self.children:
            for child in self.children:
                child.print_tree()
            
    def dir_sizes(self):    
        sum = 0
        for child in self.children:
            directory_sum = child.dir_sizes()
            sum += directory_sum
            dir_sizes_dict(child.data, directory_sum)
            
            print(f"For dir {child.data} size = {directory_sum}")
        for _, size in self.files:
            sum += size
        return sum
    
def dir_sizes_dict(directory, size):
    global DIRECTORY_ARR
    
    DIRECTORY_ARR.append((directory, size))
                       
with open("data_prod.txt") as data:
    ##Read data
    input_text = data.readlines()
    
commands = [cmd.replace("\n","") for cmd in input_text]


for command in commands:
    
    command = command.split(" ")
    
    if command[0] == "$":
        #check which command
        
        if command[1] == "cd":
            if command[2] == "/":
                rootNode = TreeNode(command[2])
                current_node = rootNode
            elif command[2] == "..":
                current_node = current_node.parent
            else:
                new_node = TreeNode(command[2])
                current_node.add_child(new_node)
                current_node = new_node
        else:
            continue
    else:
        if command[0] == "dir":
            pass
        else:
            current_node.add_file(name = command[1], size= int(command[0]))        
DIRECTORY_ARR = []
rootNode.print_tree()
occupied =rootNode.dir_sizes()
print(DIRECTORY_ARR)
sum = 0 
count = 0
for name, size in DIRECTORY_ARR:
    if size <= 100000:
        sum += size
        count+=1
    else:
        print(f"DIR: {name}, SUM = {size}")

print(f"answer is = {sum}, Number of such directries {count}")

DIRECTORY_ARR.sort(key = lambda x: x[1])

how_much_to_free = 30000000 - (70000000 - occupied)

#Part 2
for _, value in DIRECTORY_ARR:
    if value > how_much_to_free:
        print(value)
        break;