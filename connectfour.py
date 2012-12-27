#!/usr/bin/env python3

class Connectfour(object):
	"""Connectfour Game on CLI Basis"""
	def __init__(self):
		super(Connectfour, self).__init__()

	fieldsize = [6,30] # rows, columns
	aienemy = False

	field = []

	identifier = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	def setup(self):
		self.field = [[0 for x in range(self.fieldsize[1])] for x in range(self.fieldsize[0])]

		# Check if column-count is bigger than identifier-list -> generate permutations..
		if self.fieldsize[1] > len(self.identifier):
			ident = []
			import itertools
			for p in itertools.permutations(self.identifier, 2):
			    ident.append(''.join(p))
			self.identifier = self.identifier + ident

	def getTranslation(self, content):
		if content == 0:
			return "   "
		elif content == 1:
			return " X "
		elif content == 2:
			return " O "

	def _printNewLine(self):
		line = "+";
		for i in range(0, self.fieldsize[1]+1):
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
		line = " ";
		for i in range(0, self.fieldsize[1]+1):
			separator = '  ' if (len(self.identifier[i]) == 1) else ' '
			line += separator+self.identifier[i]+'   '
		print(line)


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