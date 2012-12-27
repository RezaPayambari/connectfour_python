#!/usr/bin/env python3

from random import choice
from os import system
from time import sleep
import re

class Connectfour(object):
	"""Connectfour Game on CLI Basis"""
	def __init__(self):
		super(Connectfour, self).__init__()

	fieldsize = [6,7] # rows, columns
	aienemy = False

	field = []

	identifier = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']

	whosTurn = 1;

	def setup(self):
		# Helper
		self.columnCount = self.fieldsize[1]
		self.rowCount = self.fieldsize[0]

		self.field = [[0 for x in range(self.columnCount)] for x in range(self.rowCount)]

		# Check if column-count is bigger than identifier-list -> generate permutations..
		if self.columnCount > len(self.identifier):
			ident = []
			import itertools
			for p in itertools.permutations(self.identifier, 2):
			    ident.append(''.join(p))
			self.identifier = self.identifier + ident

		self.identifier = self.identifier[0:self.columnCount]


	def getTranslation(self, content):
		if content == 0:
			return "   "
		elif content == 1:
			return " X "
		elif content == 2:
			return " O "

	def _printNewLine(self):
		line = "+";
		for i in range(0, self.columnCount):
			line += '-----+'
		print(line)

	def printField(self):
		print("\nVIER GEWINNT\n")
		self._printNewLine()
		for row in reversed(self.field):
			print('| ', end='')
			for column in row:
				print(self.getTranslation(column) + ' | ', end='')
			print()
			self._printNewLine()
		line = " ";
		for i in range(0, self.columnCount):
			separator = '  ' if (len(self.identifier[i]) == 1) else ' '
			line += separator+self.identifier[i]+'   '
		print(line)

	def isNotFull(self):
		for i in range(0, self.columnCount):
			if (self.field[self.rowCount-1][i] == 0):
				return True
		return False


	def checkWin(self):
		# Check horizontally
		for col in range(self.columnCount-3):
			for row in range(self.rowCount):
				if (self.field[row][col] == self.field[row][col+1] == self.field[row][col+2] == self.field[row][col+3] != 0):
					return self.field[row][col]

		# Check vertically
		for row in range(self.rowCount-3):
			for col in range(self.columnCount):
				if (self.field[row][col] == self.field[row+1][col] == self.field[row+2][col] == self.field[row+3][col] != 0):
					return self.field[row][col]

		# Skip diagonal checks if column count is less than 4
		if (self.columnCount < 4):
			return False

		# Check up-diagonally
		for col in range(self.columnCount-3):
			for row in range(self.rowCount-3):
				if (self.field[row][col] == self.field[row+1][col+1] == self.field[row+2][col+2] == self.field[row+3][col+3] != 0):
					return self.field[row][col]

		# Check down-diagonally
		for col in range(3, self.columnCount):
			for row in range(self.rowCount-3):
				if (self.field[row][col] == self.field[row+1][col-1] == self.field[row+2][col-2] == self.field[row+3][col-3] != 0):
					return self.field[row][col]

		return False

	def error(self, message):
		if (self.whosTurn == 2 and self.aienemy == True):
			return True

		print("FEHLER: "+str(message));
		sleep(1)

	def feed(self, where):
		where = where.upper()
		if (where not in self.identifier):
			self.error("Ungültiger Slot!")
			return False

		# Find out if slot can be used
		columnNumber = self.identifier.index(where)
		rowNumber = 0
		for row in self.field:
			if (row[columnNumber] == 0):
				break
			rowNumber += 1

		if (rowNumber >= self.rowCount):
			self.error("Diese Reihe ist Voll - Wählen Sie bitte eine Andere!")
			return False


		# Save selection to field
		self.field[rowNumber][columnNumber] = self.whosTurn

		# Next player is on turn
		self.whosTurn = 1 if self.whosTurn == 2 else 2

		if (self.whosTurn == 2 and self.aienemy == True):
			# Make AI-Move
			print("Computergegner ist an der Reihe..");
			self._aiMakeMove()

		return True


	def _aiMakeMove(self):
		while True:
			selection = choice(self.identifier)
			if (self.feed(selection)):
				print("Computergegner wählt "+selection);
				sleep(1)
				break

def main():
	system("clear")
	Game = Connectfour()

	print ("""
 __      ___                                 _             _   
 \ \    / (_)                               (_)           | |  
  \ \  / / _  ___ _ __    __ _  _____      ___ _ __  _ __ | |_ 
   \ \/ / | |/ _ \ '__|  / _` |/ _ \ \ /\ / / | '_ \| '_ \| __|
    \  /  | |  __/ |    | (_| |  __/\ V  V /| | | | | | | | |_ 
     \/   |_|\___|_|     \__, |\___| \_/\_/ |_|_| |_|_| |_|\__|
                          __/ |                                
                         |___/                                 
	""")

	print("Copyright 2012 Fabian Golle, Veronika Schoepf. Alle Rechte vorbehalten\n\n");
	print("Sie können das Spiel jederzeit mit der Eingabe von Q beenden!")
	print("Herzlich Willkommen!\nWählen Sie einen Spielmodus!")
	while True:
		print("Computergegner (C) oder menschlicher Gegner (M)?");
		modus = input(">> ")
		if (modus.upper() == "Q"):
			print("Bye-Bye ;)");
			quit();
		elif (modus.upper() == "C"):
			Game.aienemy = True
			print("\nSie haben: X")
			print("Computergegner hat: O")
			break
		elif (modus.upper() == "M"):
			Game.aienemy = False
			print("\nSpieler 1 hat: X")
			print("Spieler 2 hat: O")
			break

	while True:
		print("\nWie groß soll das Spielfeld sein? Breite x Höhe (Leere Eingabe = Standardgröße 6x7)");
		sizeI = input(">> ")
		size = re.search("(\d)+( )?x( )?(\d)+", sizeI)
		if (sizeI == ""):
			break
		elif (size):
			Game.fieldsize = [int(size.group(1)), int(size.group(4))]
			break

	system("clear")

	Game.setup();
	Game.printField()

	while (Game.isNotFull()):
		whateverTheUserEntered = input("Spieler "+str(Game.whosTurn)+" >> ")
		if (whateverTheUserEntered.upper() == "Q"):
			print("Bye-Bye ;)");
			quit();
		Game.feed(whateverTheUserEntered)
		system("clear")
		win = Game.checkWin()
		Game.printField()
		if (win):
			if (win == 1 or (win == 2 and self.aienemy == False)):
				for x in range(4):
					system("clear")
					print("""
  /$$$$$$                       /$$               /$$             /$$     /$$                     /$$
 /$$__  $$                     | $$              | $$            | $$    |__/                    | $$
| $$  \__/  /$$$$$$  /$$$$$$  /$$$$$$   /$$   /$$| $$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$ | $$
| $$ /$$$$ /$$__  $$|____  $$|_  $$_/  | $$  | $$| $$ |____  $$|_  $$_/  | $$ /$$__  $$| $$__  $$| $$
| $$|_  $$| $$  \__/ /$$$$$$$  | $$    | $$  | $$| $$  /$$$$$$$  | $$    | $$| $$  \ $$| $$  \ $$|__/
| $$  \ $$| $$      /$$__  $$  | $$ /$$| $$  | $$| $$ /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$    
|  $$$$$$/| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$ /$$
 \______/ |__/      \_______/   \___/   \______/ |__/ \_______/   \___/  |__/ \______/ |__/  |__/|__/
                                                                                                     
""")
					print ("Spieler "+str(win)+" hat gewonnen!")
					sleep(1)
					system("clear")
					print("""
 $$$$$$\                      $$\               $$\            $$\     $$\                     $$\ 
$$  __$$\                     $$ |              $$ |           $$ |    \__|                    $$ |
$$ /  \__| $$$$$$\  $$$$$$\ $$$$$$\   $$\   $$\ $$ | $$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\  $$ |
$$ |$$$$\ $$  __$$\ \____$$\\_$$  _|  $$ |  $$ |$$ | \____$$\\_$$  _|  $$ |$$  __$$\ $$  __$$\ $$ |
$$ |\_$$ |$$ |  \__|$$$$$$$ | $$ |    $$ |  $$ |$$ | $$$$$$$ | $$ |    $$ |$$ /  $$ |$$ |  $$ |\__|
$$ |  $$ |$$ |     $$  __$$ | $$ |$$\ $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |    
\$$$$$$  |$$ |     \$$$$$$$ | \$$$$  |\$$$$$$  |$$ |\$$$$$$$ | \$$$$  |$$ |\$$$$$$  |$$ |  $$ |$$\ 
 \______/ \__|      \_______|  \____/  \______/ \__| \_______|  \____/ \__| \______/ \__|  \__|\__|
                                                                                                                                                                                               
""")
					print ("Spieler "+str(win)+" hat gewonnen!")
					sleep(1)
			break

	print("Spielende.")


if __name__ == "__main__":
    main()