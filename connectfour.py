#!/usr/bin/env python3

class Connectfour(object):
	"""Connectfour Game on CLI Basis"""
	def __init__(self):
		super(Connectfour, self).__init__()

	fieldsize = [6,30] # rows, columns
	aienemy = False

	field = []

	identifier = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	whosTurn = 1;

	def setup(self):
		self.field = [[0 for x in range(self.fieldsize[1])] for x in range(self.fieldsize[0])]

		# Check if column-count is bigger than identifier-list -> generate permutations..
		if self.fieldsize[1] > len(self.identifier):
			ident = []
			import itertools
			for p in itertools.permutations(self.identifier, 2):
			    ident.append(''.join(p))
			self.identifier = self.identifier + ident

		self.identifier = self.identifier[0:self.fieldsize[1]+1]

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
		for row in reversed(self.field):
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


	def feed(self, where):
		if (where not in self.identifier):
			return False

		# Find out if slot can be used
		columnNumber = self.identifier.index(where)
		rowNumber = 0
		i = 0
		for row in self.field:
			if (row[columnNumber] == 0):
				rowNumber = i
				break
			i += 1


		# Save selection to field
		self.field[rowNumber][columnNumber] = self.whosTurn

		# Next player is on turn
		self.whosTurn = 1 if self.whosTurn == 2 else 2

c4 = Connectfour()
c4.setup();

for x in range(1,10):
	c4.feed(input(">> "))
	c4.printField()

