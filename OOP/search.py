class Node():
    def __init__(self, key):
        self.key = key
        self.values = []
        self.left = None
        self.right = None
        
    def __len__(self):
        size = len(self.values)
        if self.left != None:
            size += len(self.left)
        if self.right != None:
            size += len(self.right)
        return size
    
    def lookup(self, key):
        if key == self.key: #return my values
            return self.values
        if key < self.key and self.left != None:
            return self.left.lookup(key)
        elif key > self.key and self.right != None:
            return self.right.lookup(key)
        else:
            return []
        
    def tree_height(self):
        if self.right != None and self.left != None:
            return 1 + max(self.right.tree_height(), self.left.tree_height())
        elif self.right != None:
            return 1 + self.right.tree_height()
        elif self.left != None:
            return 1 + self.left.tree_height()
        else:
            return 1
        
    def tree_size(self):
        if self.right != None and self.left != None:
            return 1 + self.right.tree_size() + self.left.tree_size()
        elif self.right != None:
            return 1 + self.right.tree_size()
        elif self.left != None:
            return 1 + self.left.tree_size()
        else:
            return 1

class BST():
    def __init__(self):
        self.root = None

    def add(self, key, val):
        if self.root == None:
            self.root = Node(key)

        curr = self.root
        while True:
            if key < curr.key:
                # go left
                if curr.left == None:
                    curr.left = Node(key)
                curr = curr.left
            elif key > curr.key:
                 # go right
                if curr.right == None:
                    curr.right = Node(key)
                curr = curr.right
            else:
                # found it!
                assert curr.key == key
                break

        curr.values.append(val)
        
    def __dump(self, node):
        if node == None:
            return
        self.__dump(node.left)             # 1
        print(node.key, ":", node.values)  # 2
        self.__dump(node.right)            # 3

    def dump(self):
        self.__dump(self.root)
        
    def __getitem__(self, item):
        return self.root.lookup(item)
    
    def tree_height(self):
        if self.root != None:
            return self.root.tree_height()
        else: 
            return 0
    def tree_size(self):
        if self.root != None:
            return self.root.tree_size()
        else:
            return 0
        
      