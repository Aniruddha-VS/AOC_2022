# Genral tree , paent an have many children

class TreeNode:
    def __init__(self,data, parent=None):
        self.data = data
        self.children = []
        self.files = {}
        self.parent = parent
    
    def add_files(self, files):
        self.files = files
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def print_tree(self):
        print(self.data)
        
        for child in self.children:
            print(child.data)
            
        
def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("laptop")
    
    root.add_child(laptop)
    
    return root
    
if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass