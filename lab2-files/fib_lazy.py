# explanations for member functions are provided in requirements.py
from __future__ import annotations

class FibNodeLazy:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNodeLazy):
        return self.val == other.val

class FibHeapLazy:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min_node = None

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNodeLazy:
        node = FibNodeLazy(val)
        self.roots.append(node)
        self.find_min_lazy()
        return node
        
    def delete_min_lazy(self) -> None:
        if self.min_node is None or self.min_node not in self.roots:
            return
        if self.min_node.val != float('-inf'):
            self.mark_deleted()
        else:
            #if the min node is already deleted, find the new min node
            self.find_min_lazy()
            self.mark_deleted()
    
    def mark_deleted(self) -> None: 
        for root in self.roots:
            if root.val == self.min_node.val:
                root.val = float('-inf')
                self.min_node.val = float('-inf')
                break

    def find_min_lazy(self) -> FibNodeLazy:
        self.remove_vacant(self.min_node)
        self.consolidate()
        min_node = self.find_min_root()
        return min_node
    
    def remove_vacant(self,node:FibNodeLazy) -> None:
        if node is not None and node.val != float('-inf'):
            self.roots.append(node)
            node.flag = False
            return
        
        roots_copy = self.roots.copy()
        for root in roots_copy:
            if root.val == float('-inf'):
                if node in self.roots:
                    self.roots.remove(node)
                for child in root.get_children():
                    self.remove_vacant(child)
    
    def consolidate(self) -> None:
        #make sure that the root list is unchanged
        root_list = self.roots.copy()
        #store the degree of each node
        degree_dict = {}

        while root_list:
            root = root_list.pop()
            degree = len(root.get_children())
            if degree not in degree_dict:
                degree_dict[degree] = root
            else:
                combine_root = degree_dict[degree]
                del degree_dict[degree]
                #choose the min node as the parent
                if root.val < combine_root.val:
                    root.children.append(combine_root)
                    combine_root.parent = root
                    root.flag = False
                    root_list.append(root)
                    self.roots.remove(combine_root)
                else:
                    combine_root.children.append(root)
                    root.parent = combine_root
                    combine_root.flag = False
                    root_list.append(combine_root)
                    self.roots.remove(root)

    def find_min_root(self) -> FibNodeLazy:
        if len(self.roots)==0:
            self.min_node = None
            return
        min_node = FibNodeLazy(float('inf'))
        for root in self.roots:
            if root.val<min_node.val:
                min_node = root
                self.min_node = min_node
        return min_node  
    
    def promote(self, node: FibNodeLazy) -> None:
        if node.parent is not None:
            p = node.parent
            p.children.remove(node)
            self.roots.append(node)
            node.flag = False
            node.parent = None
            if p.parent is not None:
                if p.flag:
                    self.promote(p)
                elif p not in self.roots:
                    p.flag = True
                    
    def decrease_priority(self, node: FibNodeLazy, new_val: int) -> None:
        node.val = new_val
        if node.parent is not None:
            self.promote(node)
        self.find_min_lazy()

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define