# coding:utf-8

class Empty(Exception):
	pass

class ArrayStack:
	"""LIFO Stack implementation using a Python list as underlying storage"""


	def __init__(self):
		""" Create an empty stack """
		self._data = []  # noplublic list instance


	def __len__(self):
		""" Return the number of elements in the stack """
		return len(self._data)


	def is_empty(self):
		""" Return True if the stack is empty """
		return len(self._data) == 0


	def push(self, e):
		""" Add element e to the top of the stack """
		self._data.append(e)  # new item stored at end of the list


	def top(self):
		"""
		Return (but do't remove) the element at the top of the stack
        
        Raise Empty exception if the stack is empty   
		"""
		if self.is_empty():
		    raise Empty('Stack is empty')
		return self._data[-1]


	def pop(self):
		""" Remove and return the element from the top of the stack

		Rasie Empty exception if the stack is empty """

		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data.pop()  # remove last item from list


def reverse_file(filename):
	"""Overwrite given file with its contents line-byline reversed"""
	S = ArrayStack()
	with open(filename, 'r') as outfile:
		for line in outfile:
			S.push(line.rstrip('\n'))

	with open(filename,'w') as infile:
		while not S.is_empty():
			infile.write(S.pop() + '\n')


if __name__ == '__main__':
	a = ArrayStack()
	a.push('123')
	print(a.top())
	reverse_file('kang.txt')