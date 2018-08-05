# coding:utf-8

class GameEntry:
	""" 展示一组高分成绩"""
	def __init__(self, name, score):
		self._name = name
		self._score = score

	def get_name(self):
		return self._name

	def get_score(self):
		return self._score

	def __str__(self):
		return '({0}, {1})'.format(self._name, self._score)



class Scoreboard:
	''' 展示成绩'''
	def __init__(self, capacity=10):
		self._board = [None] * capacity #创建大小为capacity的空列表
		self._n = 0 #列表元素个数

	def __getitem__(self, k):
		"""Return entry at index k"""
		return self._board[k]

	def __str__(self):
		return '\n'.join(str(self._board[j]) for j in range(self._n))

	def add(self, entry):
		"""
		主要是要理解腾笼换鸟的操作，和list 中insert 的原理类似
		1.如果列表元素没有满或者 有添加的score 大于列表最后一个，进入条件判断
		如果列表没有满，n+1， 接下来进入循环语句，也是最重要的部分
		其原理就是依次 把前面的元素和要添加的score进行比较，如果比其小就向右移一位，腾笼换鸟，
		直到遇到比其大或者相等的，循环结束，此时的j就是score 要添加的位置

		"""
		score = entry.get_score()
		good = self._n < len(self._board) or score > self._board[-1].get_score

		if good:
			if self._n < len(self._board):
				self._n += 1

			j = self._n - 1
			while j > 0 and self._board[j-1].get_score() < score:
				self._board[j] = self._board[j-1]
				j -= 1
			self._board[j] = entry



