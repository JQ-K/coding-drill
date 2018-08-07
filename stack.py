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


def is_matched(expr):
	""" Return True if all delimiters are properly match; False otherwise"""
	lefty = '({['
	righty = ')}]'
	S = ArrayStack()
	for c in expr:
		if c in lefty:
			S.push(c)
		elif c in righty:
			if S.is_empty():
				return False
			if righty.index(c) != lefty.index(S.pop()):
				return False
	return S.is_empty()
	

def is_matched_html(raw):
	""" 判断HTML 标签是否正确匹配"""
	S = ArrayStack() # 创建一个stack
	j = raw.find('<') # 是否存在，如果有返回第一个位置，没有的话返回-1
	while j != -1: # 使用while 语句，找完所有的‘<'标签
		k = raw.find('>', j+1) # k 是从 '<' 后 找到的第一个'>'的位置
		if k == -1:  # 如果k = -1 说明缺一个 '>'
			return False
		tag = raw[j+1,:k] # tag 是 < > 之间的内容 
		if not tag.sartswith('/'): # 如果非尾部标签，把 tag 压入栈
			S.push(tag)
		else:
			if S.is_empty():
				return False
			if tag[1:] != S.pop():
				return False
		j = raw.find('<', k+1)
	return S.is_empty()


if __name__ == '__main__':
	a = ArrayStack()
	a.push('123')
	print(a.top())
	reverse_file('kang.txt')