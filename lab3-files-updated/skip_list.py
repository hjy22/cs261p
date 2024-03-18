# explanations for member functions are provided in requirements.py
# each file that uses a skip list should import it from this file.

from typing import TypeVar
import random
from zip_tree import ZipTree
from collections import OrderedDict


KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')
        
class SkipList:
	def __init__(self):
		self.lists = {}
		self.max_level =0

	def get_random_level(self, key: KeyType) -> int:
	  	# Do not change this function. Use this function to determine what level each key should be at. Assume levels start at 0 (i.e. the bottom-most list is at level 0)
		# e.g. for some key x, if get_random_level(x) = 5, then x should be in the lists on levels 0, 1, 2, 3, 4 and 5 in the skip list.
		random.seed(str(key))
		level = 0
		while random.random() < 0.5 and level < 20:
			level += 1
		return level

	def insert(self, key: KeyType, val: ValType):
		level = self.get_random_level(key)
		
		while level>=self.max_level:
			self.lists[self.max_level] = OrderedDict()
			self.max_level += 1
		for i in range(level+1):
			self.lists[i][str(key)]= val
			self.lists[i] = OrderedDict(sorted(self.lists[i].items(), key=lambda x: (x[0], x[1])))


	def remove(self, key: KeyType):
		level = self.max_level-1
		while level>=0:
			if str(key) in self.lists[level]:
				del self.lists[level][str(key)]
			level -= 1

	def find(self, key: KeyType) -> ValType:
		level = self.max_level-1
		while level>=0:
			if str(key) in self.lists[level]:
				return self.lists[level][str(key)]
			level -= 1
		return None

	def get_list_size_at_level(self, level: int):
		if level>=self.max_level:
			return 0
		return len(self.lists[level])
		
	def from_zip_tree(self, zip_tree: ZipTree) -> None:
		for node in zip_tree.traverse_inorder():
			self.insert_with_rank(node.key, node.value, node.rank)
   
	def insert_with_rank(self, key: KeyType, val: ValType,level: int):		
		while level>=self.max_level:
			self.lists[self.max_level] = OrderedDict()
			self.max_level += 1
		for i in range(level+1):
			self.lists[i][str(key)]= val
			self.lists[i] = OrderedDict(sorted(self.lists[i].items(), key=lambda x: (x[0], x[1])))

# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
