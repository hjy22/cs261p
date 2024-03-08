# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List, Optional

class CuckooHash24:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.bucket_size = 4
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.table = [None]*self.table_size

	def get_rand_bucket_index(self, bucket_idx: int) -> int:
		# you must use this function when you need to evict a random key from a bucket. this function
		# randomly chooses an index from a given cell index. this ensures that the random
		# index chosen by your code and our test script match.
		#
		# for example, if you need to remove a random element from the bucket at table index 5,
		# you will call get_rand_bucket_index(5) to determine which key from that bucket to evict, i.e. if get_random_bucket_index(5) returns 2, you
		# will evict the key at index 2 in that bucket.
		rand.seed(int(str(bucket_idx)))
		return rand.randint(0, self.bucket_size-1)

	def hash_func(self, key: int, func_id: int) -> int:
		# access h0 via func_id=0, access h1 via func_id=1
		key = int(str(key) + str(self.__num_rehashes) + str(func_id))
		rand.seed(key)
		result = rand.randint(0, self.table_size-1)
		return result

	def get_table_contents(self) -> List[Optional[List[int]]]:
		# the buckets should be implemented as lists. Table cells with no elements should still have None entries.
		return self.table

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

	def insert(self, key: int) -> bool:
		current_circle = 0
		while current_circle <= self.CYCLE_THRESHOLD:
			insert_zero = self.insertKey(key, 0)
			if(insert_zero is True):
				return True
			else:
				insert_one = self.insertKey(key, 1)
				if(insert_one is True):
					return True
				else:
					key = insert_one
					current_circle += 1
		return False
	
	def insertKey(self, key: int,ID:int) -> bool:
		hash_value = self.hash_func(key, ID)
		row_array = self.table[hash_value]
		if row_array is None:
			self.table[hash_value] = [key]
			return True
		elif len(row_array) < self.bucket_size:
			self.table[hash_value].append(key)
			return True
		else:
			if ID==0:
				return False
			else:
				hash_value0 = self.hash_func(key, 0)
				rand_idx = self.get_rand_bucket_index(hash_value0)
				current_value = self.table[hash_value0][rand_idx]
				self.table[hash_value0][rand_idx] = key
				return current_value
	
	def lookup(self, key: int) -> bool:
		hash_value1 = self.hash_func(key, 0)
		hash_value2 = self.hash_func(key, 1)
		if (self.table[hash_value1] is not None and key in self.table[hash_value1]) or (self.table[hash_value2] is not None and key in self.table[hash_value2]):
			return True
		else:
			return False
		

	def delete(self, key: int) -> None:
		hash_values = [0, 1]
		for ID in hash_values:
			hash_value = self.hash_func(key, ID)
			if self.table[hash_value] != None and key in self.table[hash_value]:
				self.table[hash_value].remove(key)
				if not self.table[hash_value]:
					self.table[hash_value] = None

	def rehash(self, new_table_size: int) -> None:
		self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line
		old_table = self.table
		self.table = [None]*new_table_size
		for i in range(len(old_table)):
			if old_table[i] is not None:
				for j in old_table[i]:
					self.insert(j)

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define


