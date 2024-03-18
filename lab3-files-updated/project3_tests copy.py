import requirements

from typing import TypeVar, NamedTuple
from copy import deepcopy

# Some test cases for the ZipTree and SkipList classes can be found below.
#
# Note that passing the test cases here does not necessarily mean that your zip tree/skip list
# is correctly implemented / will pass other cases. It is a good idea to try and create different
# test cases for both.

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class InsertType(NamedTuple):
	key: KeyType
	val: ValType
	rank: int

def create_tree_with_data(data: [InsertType]) -> requirements.ZipTree:
	tree = requirements.ZipTree()
	for item in data:
		tree.insert(item.key, item.val, item.rank)

	return tree

def zip_tree_tests():
	print('testing ZipTree')

	# data = [InsertType(4, 'a', 0),
    #      InsertType(5, 'b', 0),
    #      InsertType(2, 'c', 2),
    #      InsertType(1, 'd', 1)]
	# tree = create_tree_with_data(data)

	# print(f'find(4): {tree.find(4)}, Expected: a')
	# print(f'get_size(): {tree.get_size()}, Expected: 4')
	# print(f'get_height(): {tree.get_height()}, Expected: 2')
	# print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	# print(f'get_depth(1): {tree.get_depth(1)}, Expected: 1')
	# tree.insert(0, 'e', 1)
	# print(f'get_size(): {tree.get_size()}, Expected: 5')
	# print(f'get_height(): {tree.get_height()}, Expected: 2')
	# print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	# print(f'get_depth(1): {tree.get_depth(1)}, Expected: 2\n')

 
 
 
	datat = [
	InsertType(0, 'a', -1),
	InsertType(1, 'b', -1),
	InsertType(2, 'c', -1),
	InsertType(3, 'd', -1),
	InsertType(4, 'e', -1),
	InsertType(5, 'f', -1),
	InsertType(6, 'g', -1),
	InsertType(7, 'h', -1),
	InsertType(8, 'i', -1),
	InsertType(9, 'j', -1),
	InsertType(10, 'k', -1),
	InsertType(11, 'l', -1),
	InsertType(12, 'm', -1),
	InsertType(13, 'n', -1),
	InsertType(14, 'o', -1),
	InsertType(15, 'p', -1),
	InsertType(16, 'q', -1),
	InsertType(17, 'r', -1),
	InsertType(18, 's', -1),
	InsertType(19, 't', -1),
	InsertType(20, 'u', -1),
	InsertType(21, 'v', -1),
	InsertType(22, 'w', -1),
	InsertType(23, 'x', -1),
	InsertType(24, 'y', -1),
	InsertType(25, 'z', -1),
	]
	tree = create_tree_with_data(datat)
	tree.remove(0)
	tree.remove(3)
	tree.remove(6)
	tree.remove(9)
	tree.remove(12)
	tree.remove(15)
	tree.remove(18)
	tree.remove(21)
	tree.remove(24)
	print(tree.find(1))
	print(tree.find(2))
	print(tree.find(4))
	print(tree.find(5))
	print(tree.find(7))
	print(tree.find(8))
	print(tree.find(10))
	print(tree.find(11))
	print(tree.find(13))
	print(tree.find(14))
	print(tree.find(16))
	print(tree.find(17))
	print(tree.find(19))
	print(tree.find(20))
	print(tree.find(22))
	print(tree.find(23))
	print(tree.find(25))
 
 
 
# 	data2 = [InsertType(4, 'a', 2), InsertType(5, 'b', 3), InsertType(2, 'c', 1), InsertType(1, 'd', 0), InsertType(0, 'e', 1)]
# 	tree2 = create_tree_with_data(data2)

# 	print(f'find(4): {tree2.find(4)}, Expected: a')
# 	print(f'get_size(): {tree2.get_size()}, Expected: 5')
# 	print(f'get_height(): {tree2.get_height()}, Expected: 4')
# 	print(f'get_depth(2): {tree2.get_depth(2)}, Expected: 3')
# 	print(f'get_depth(1): {tree2.get_depth(1)}, Expected: 4')

# 	print('\ntesting random rank generation')
# 	rank_sum = 0
# 	num_ranks = 10000
# 	for _ in range(num_ranks):
# 		try:
# 			rank_sum += requirements.ZipTree.get_random_rank()
# 		except:
# 			break

# 	rank_mean = rank_sum / num_ranks

# 	print(f'random rank mean: {rank_mean}, Expected: ~1\n\n')

# 	# add new tests...

# def skip_list_tests():
# 	print("testing skip list")
# 	skip_list = requirements.SkipList()
# 	skip_list.insert(2.4, 'a')
# 	skip_list.insert(2.5, 'b')
# 	skip_list.insert(2.2, 'c')
# 	skip_list.insert(2.1, 'd')
# 	skip_list.insert(2.6, 'e')
# 	# skip list levels should look like 
# 	# -> 2.1 -> 		 2.4 -> 	   2.6
# 	# -> 2.1 -> 		 2.4 -> 	   2.6
# 	# -> 2.1 -> 2.2 -> 2.4 -> 2.5 -> 2.6
# 	print(f'find(2.4): {skip_list.find(2.4)}, Expected: a')
# 	print(f'get_list_size_at_level(0): {skip_list.get_list_size_at_level(0)}, Expected: 5')
# 	print(f'get_list_size_at_level(1): {skip_list.get_list_size_at_level(1)}, Expected: 3')
# 	print(f'get_list_size_at_level(2): {skip_list.get_list_size_at_level(2)}, Expected: 3\n')
# 	skip_list.remove(2.6)
# 	# skip list levels should look like 
# 	# -> 2.1 -> 		 2.4
# 	# -> 2.1 -> 		 2.4
# 	# -> 2.1 -> 2.2 -> 2.4 -> 2.5
# 	print(f'get_list_size_at_level(0): {skip_list.get_list_size_at_level(0)}, Expected: 4')
# 	print(f'get_list_size_at_level(1): {skip_list.get_list_size_at_level(1)}, Expected: 2')
# 	print(f'get_list_size_at_level(2): {skip_list.get_list_size_at_level(2)}, Expected: 2\n')



# 	print("testing skip list construction from a zip tree")
# 	data = [InsertType(4, 'a', 0), InsertType(5, 'b', 0), InsertType(2, 'c', 2), InsertType(1, 'd', 1)]
# 	tree = create_tree_with_data(data)

# 	skip_list = requirements.SkipList()
# 	skip_list.from_zip_tree(tree)
# 	# skip list levels should look like 
# 	# ->		2
# 	# -> 1 -> 2
# 	# -> 1 -> 2 -> 4 -> 5
# 	skip_list.printList()
# 	print(f'find(4): {skip_list.find(4)}, Expected: a')
# 	print(f'get_list_size_at_level(0): {skip_list.get_list_size_at_level(0)}, Expected: 4')
# 	print(f'get_list_size_at_level(1): {skip_list.get_list_size_at_level(1)}, Expected: 2')
# 	print(f'get_list_size_at_level(2): {skip_list.get_list_size_at_level(2)}, Expected: 1\n')
# 	skip_list.remove(2)
# 	# skip list levels should look like 
# 	#														 				-> 1
# 	#															 			-> 1 -> 4 -> 5
# 	print(f'get_list_size_at_level(0): {skip_list.get_list_size_at_level(0)}, Expected: 3')
# 	print(f'get_list_size_at_level(2): {skip_list.get_list_size_at_level(2)}, Expected: 0')

	# add new tests...
	
if __name__ == '__main__':
	zip_tree_tests()
	# skip_list_tests()
