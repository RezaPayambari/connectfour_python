#!/usr/bin/env python3

class Connectfour(object):
	"""Connectfour Game on CLI Basis"""
	def __init__(self):
		super(Connectfour, self).__init__()

	fieldsize = [6,7] # rows, columns
	aienemy = False

	field = []


	def setup(self):
		self.field = [[0 for x in range(self.fieldsize[1])] for x in range(self.fieldsize[0])]

	def getTranslation(self, content):
		if content == 0:
			return "   "
		elif content == 1:
			return " X "
		elif content == 2:
			return " O "

	def _printNewLine(self):
		line = "+";
		for i in range(0, self.fieldsize[0]+1):
			line += '-----+'
		print(line)

	def printField(self):
		self._printNewLine()
		for row in self.field:
			print('| ', end='')
			for column in row:
				print(self.getTranslation(column) + ' | ', end='')
			print()
			self._printNewLine()


	def feed(self, where, what):
		self.field[where[0]][where[1]] = what

c4 = Connectfour()

c4.setup();

c4.feed([5,6], 1)
c4.feed([5,5], 1)
c4.feed([5,4], 2)
c4.feed([4,6], 2)
c4.feed([4,4], 1)

c4.printField()