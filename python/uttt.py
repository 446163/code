board = [[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]],[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]],[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]],[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]],[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]],[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]],[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]],[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]],[["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "],["   "]]]
grid = ["|","|","-","-","-","|","|","-","-","-","|","|"]
win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
capture = ["   ","   ","   ","   ","   ","   ","   ","   ","   "]
  
def printBoard(s):
    grid = ["|","|","-","-","-","|","|","-","-","-","|","|"]
    hGrid = ["I","I","=","=","=","I","I","=","=","=","I","I"]
    hData = [[0,2],[0,1,3],[1,4],[2,5,7],[3,5,6,8],[4,6,9],[7,10],[8,10,11],[9,11],[]]
    for item in hData[s]:
        grid[item] = hGrid[item]
    print(str(''.join(board[0][0]))+str(''.join(board[0][1]))+str(''.join(board[0][2]))+str(grid[0])+str(''.join(board[1][0]))+str(''.join(board[1][1]))+str(''.join(board[1][2]))+str(grid[1])+str(''.join(board[2][0]))+str(''.join(board[2][1]))+str(''.join(board[2][2])))
    print(str(''.join(board[0][3]))+str(''.join(board[0][4]))+str(''.join(board[0][5]))+str(grid[0])+str(''.join(board[1][3]))+str(''.join(board[1][4]))+str(''.join(board[1][5]))+str(grid[1])+str(''.join(board[2][3]))+str(''.join(board[2][4]))+str(''.join(board[2][5])))
    print(str(''.join(board[0][6]))+str(''.join(board[0][7]))+str(''.join(board[0][8]))+str(grid[0])+str(''.join(board[1][6]))+str(''.join(board[1][7]))+str(''.join(board[1][8]))+str(grid[1])+str(''.join(board[2][6]))+str(''.join(board[2][7]))+str(''.join(board[2][8])))
    print(str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+"+"+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+"+"+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+"   "+str(''.join(capture[0]))+"|"+str(''.join(capture[1]))+"|"+str(''.join(capture[2])))                                                                            
    print(str(''.join(board[3][0]))+str(''.join(board[3][1]))+str(''.join(board[3][2]))+str(grid[5])+str(''.join(board[4][0]))+str(''.join(board[4][1]))+str(''.join(board[4][2]))+str(grid[6])+str(''.join(board[5][0]))+str(''.join(board[5][1]))+str(''.join(board[5][2]))+"   "+"-----------")
    print(str(''.join(board[3][3]))+str(''.join(board[3][4]))+str(''.join(board[3][5]))+str(grid[5])+str(''.join(board[4][3]))+str(''.join(board[4][4]))+str(''.join(board[4][5]))+str(grid[6])+str(''.join(board[5][3]))+str(''.join(board[5][4]))+str(''.join(board[5][5]))+"   "+str(''.join(capture[3]))+"|"+str(''.join(capture[4]))+"|"+str(''.join(capture[5])))
    print(str(''.join(board[3][6]))+str(''.join(board[3][7]))+str(''.join(board[3][8]))+str(grid[5])+str(''.join(board[4][6]))+str(''.join(board[4][7]))+str(''.join(board[4][8]))+str(grid[6])+str(''.join(board[5][6]))+str(''.join(board[5][7]))+str(''.join(board[5][8]))+"   "+"-----------")
    print(str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+"+"+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+"+"+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+"   "+str(''.join(capture[6]))+"|"+str(''.join(capture[7]))+"|"+str(''.join(capture[8])))
    print(str(''.join(board[6][0]))+str(''.join(board[6][1]))+str(''.join(board[6][2]))+str(grid[10])+str(''.join(board[7][0]))+str(''.join(board[7][1]))+str(''.join(board[7][2]))+str(grid[11])+str(''.join(board[8][0]))+str(''.join(board[8][1]))+str(''.join(board[8][2])))
    print(str(''.join(board[6][3]))+str(''.join(board[6][4]))+str(''.join(board[6][5]))+str(grid[10])+str(''.join(board[7][3]))+str(''.join(board[7][4]))+str(''.join(board[7][5]))+str(grid[11])+str(''.join(board[8][3]))+str(''.join(board[8][4]))+str(''.join(board[8][5])))
    print(str(''.join(board[6][6]))+str(''.join(board[6][7]))+str(''.join(board[6][8]))+str(grid[10])+str(''.join(board[7][6]))+str(''.join(board[7][7]))+str(''.join(board[7][8]))+str(grid[11])+str(''.join(board[8][6]))+str(''.join(board[8][7]))+str(''.join(board[8][8])))
    grid = ["|","|","-","-","-","|","|","-","-","-","|","|"]
    


mainLoop = 1
valid = ["1","2","3","4","5","6","7","8","9"]
def main():
	while mainLoop == 1:
		game=1
		print("welcome to ultimate Tic Tac Toe \n press [enter] to start a new game or [q] to quit")
		menu = input(": ")
		if menu == "q":
			quit()
		elif menu == "":
			print("game start")
			printBoard(9)
			player = " x "
			validLoop = 0
			while validLoop == 0:
				force = input("first initial selection? : ")
				for item in valid:
					if item == force:
						validLoop = 1
				if validLoop == 0:
					print("Input Error")
			printBoard(int(force)-1) 
			while game == 1:
				if player == " x ":
					player = " O "
				else:
					player = " x "
				validLoop = 0
				while validLoop == 0:
					newForce = 0
					selection = input(str(player)+" : ")
					for item in valid:
						if selection == item:
							if board[int(force)-1][int(selection)-1] == ['   ']:
                                                		validLoop = 1
							else:
								newForce = 0
								for item in board[int(force)-1]:
									if item == ['   ']:
										newForce = 1
								if newForce == 0:
									print("***Free force to square "+str(selection)+"***")
									force = int(selection)
									printBoard(int(force)-1)
							if validLoop == 0 and newForce == 1:
								print("Input Error")  
				board[int(force)-1][int(selection)-1] = str(player)
				printBoard(int(selection)-1)
				force = int(selection)
				for a in range(9):
					for item in win:
						if board[a][item[0]] == board[a][item[1]] == board[a][item[2]] and board[a][item[0]] != ["   "]:
							if capture[a] == "   ":
								capture[a] = player
								print("player"+str(player)+"has won square "+str(int(a+1)))
				for item in win:
					if capture[item[0]] == capture[item[1]] == capture[item[2]] and capture[item[0]] != "   ":
						print("player"+str(player)+"has won the game!")
						printBoard(9)
						game = 0
mainLoop = 1
main()
