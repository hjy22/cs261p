# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from typing import TypeVar
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class Node:
	def __init__(self, key: KeyType, value: ValType, rank: int):
		self.key = key
		self.value = value
		self.rank = rank
		self.left = None
		self.right = None
  
class ZipTree:
	def __init__(self):
		self.root = None
		self.num_nodes = 0

	@staticmethod
	def get_random_rank() -> int:
		rank = 0
		while random.randint(0, 1) == 0:
			rank += 1
		return rank

	def getInsertNode(self, node: Node)-> Node:
		current = self.root
		parent = None
		while current is not None:
			if current.rank < node.rank:
				return parent, current
			elif current.rank == node.rank and current.key > node.key:
				return parent, current
			else:
				parent = current
				if current.key > node.key:
					current = current.left
				else:
					current = current.right
		return parent, None
	
	def unzip(self, key: KeyType, node: Node):
		if node is None:
			return None, None
		if node.key<key:
			p,q = self.unzip(key, node.right)
			node.right = p
			return node, q
		else:
			p,q = self.unzip(key, node.left)
			node.left = q
			return p, node
 
	def insert(self, key: KeyType, val: ValType, rank: int = -1):
		print("InsertType({}, '{}', {}),".format(key, val, rank))
		self.num_nodes += 1
		if rank == -1:
			rank = ZipTree.get_random_rank()
		node = Node(key, val, rank)
  
		if self.root is None:
			self.root = node			
		else:
			parent,child = self.getInsertNode(node)
			if child is None:
				if parent.key > key:
					parent.left = node
				else:
					parent.right = node
				return
			if parent is None:
				p,q=self.unzip(node.key, child)
				node.left = p
				node.right = q
				self.root = node
				return 
			else:
				if node.key>parent.key:
					parent.right = node
				else:
					parent.left = node
			p,q=self.unzip(node.key, child)
			node.left = p
			node.right = q
   
	def zip(self, leftNode: Node, rightNode: Node):
		if leftNode is None:
			return rightNode
		if rightNode is None:
			return leftNode
		if rightNode.rank < leftNode.rank:
			rightNode.left = self.zip(leftNode, rightNode.left)
			return rightNode
		else:
			rightNode.right = self.zip(leftNode.right, rightNode)
			return leftNode

	def remove(self, key: KeyType):
		print("tree.remove({})".format(key))
		self.num_nodes -= 1
		current = self.root
		parent = None
		while current is not None:
			if key == current.key:
				break
			elif key >current.key:
				parent = current
				current = current.right
			else:
				parent = current
				current = current.left
		if current is not None:
			node = self.zip(current.left, current.right)
			if parent is None:
				self.root = node
				return
			if current.key < parent.key:
				parent.left = node
			else:
				parent.right = node

	def find(self, key: KeyType) -> ValType:
		print("tree.find({})".format(key))
		node = self.root
		while node is not None:
			if node.key > key:
				node = node.left
			elif node.key < key:
				node = node.right
			else:
				break
		if node is None:
			return None
		return node.value

	def get_size(self) -> int:
		return self.num_nodes

	def tree_height(self,node: Node) -> int:
		if node is None:
			return 0
		else:
			left_height = self.tree_height(node.left)
			right_height = self.tree_height(node.right)
			return max(left_height, right_height) + 1
     
	def get_height(self) -> int:
		return self.tree_height(self.root)-1

	def get_depth(self, key: KeyType):
		node = self.root
		depth = 0
		while node is not None:
			if node.key > key:
				node = node.left
			elif node.key < key:
				node = node.right
			else:
				break
			depth += 1	
		return depth

	def traverse_inorder(self):
		def inorder(node):
			if node is not None:
				yield from inorder(node.left)
				yield node
				yield from inorder(node.right)
		return inorder(self.root)