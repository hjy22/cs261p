# explanations for member functions are provided in requirements.py
from __future__ import annotations
from typing import List

class FibNode:
    def __init__(self, val: int):
        self.val: int = val
        self.parent: FibNode = None
        self.children: List[FibNode] = []
        self.flag: bool = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min_node = None

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNode:
        node = FibNode(val)
        self.roots.append(node)
        if self.min_node is None or val < self.min_node.get_value_in_node():
            self.min_node = node
        return node
        
    def delete_min(self) -> None:
        #deleting the min node and promoting its children to the root list
        if self.min_node not in self.roots:
            return
        
        #promote the children of the min node to the root list
        if self.min_node is not None:
            for child in self.min_node.get_children():
                child.parent = None
                child.flag = False
                self.roots.append(child)

        #removing the min node from the root list
        self.roots.remove(self.min_node)

        #consolidating the root list
        self.consolidate()
        # Finding the new min root
        self.find_min_root()

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

    def find_min_root(self) -> FibNode:
        if len(self.roots)==0:
            self.min_node = None
            return
        min_node = FibNode(float('inf'))
        for root in self.roots:
            if root.val<min_node.val:
                min_node = root
                self.min_node = min_node  

    def find_min(self) -> FibNode:
        return self.min_node

    def promote(self, node: FibNode) -> None:
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
        
    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        node.val = new_val
        if node.parent is not None:
            self.promote(node)
        if new_val < self.min_node.get_value_in_node():
            self.min_node = node

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define