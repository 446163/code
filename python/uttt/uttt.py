board = [[[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],[[" "],[" 
"],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],[[" "],[" "],[" "],[" "],[" 
"],[" "],[" "],[" "],[" "]],[[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" 
"],[" "]],[[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],[[" "],[" 
"],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],[[" "],[" "],[" "],[" "],[" 
"],[" "],[" "],[" "],[" "]],[[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" 
"],[" "]],[[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]]] grid = 
["|","|","-","-","-","|","|","-","-","-","|","|"]
#pri = ["","","","","","","","",""] hGrid = 
#[["‖"],["‖"],["="],["="],["="],["‖"],["‖"],["="],["="],["="],["‖"],["‖"]] 
#hData = 
#[[0,2],[0,1,3],[1,4],[2,5,7],[3,5,6,8],[4,6,9],[7,10],[8,10,11],[9,11]]
""" print(' '.join() 012 | 012 | 012 345 | 345 | 345 678 | 678 | 678 
--------------- 012 | 012 | 012 345 | 345 | 345 678 | 678 | 678 
--------------- 012 | 012 | 012 345 | 345 | 345 678 | 678 | 678 def 
selection(d):
    print("selection loaded...")
    grid = ["|","|","-","-","-","|","|","-","-","-","|","|"]
    hGrid = ["‖","‖","=","=","=","‖","‖","=","=","=","‖","‖"]
    hData = 
[[0,2],[0,1,3],[1,4],[2,5,7],[3,5,6,8],[4,6,9],[7,10],[8,10,11],[9,11]]
    print(hData[d])
    #for item in hData[d]:
    #    for each thing in hData[item] grid[item] = hGrid[item]
    for item in hData[d]:
        print("item :"+str(item))
        for i in range(len(hData[d])):
            grid[i] = hGrid[i]
    
  """ def printBoard(s):
    print("selection loaded...")
    grid = ["|","|","-","-","-","|","|","-","-","-","|","|"]
    hGrid = ["I","I","=","=","=","I","I","=","=","=","I","I"]
    hData = 
[[0,2],[0,1,3],[1,4],[2,5,7],[3,5,6,8],[4,6,9],[7,10],[8,10,11],[9,11]]
    for item in hData[s]:
        grid[item] = hGrid[item]
    print(str(' '.join(board[0][0]))+str(' '.join(board[0][1]))+str(' 
'.join(board[0][2]))+str(grid[0])+str(' '.join(board[1][0]))+str(' 
'.join(board[1][1]))+str(' '.join(board[1][2]))+str(grid[1])+str(' 
'.join(board[2][0]))+str(' '.join(board[2][1]))+str(' '.join(board[2][2])))
    print(str(' '.join(board[0][3]))+str(' '.join(board[0][4]))+str(' 
'.join(board[0][5]))+str(grid[0])+str(' '.join(board[1][3]))+str(' 
'.join(board[1][4]))+str(' '.join(board[1][5]))+str(grid[1])+str(' 
'.join(board[2][3]))+str(' '.join(board[2][4]))+str(' '.join(board[2][5])))
    print(str(' '.join(board[0][6]))+str(' '.join(board[0][7]))+str(' 
'.join(board[0][8]))+str(grid[0])+str(' '.join(board[1][6]))+str(' 
'.join(board[1][7]))+str(' '.join(board[1][8]))+str(grid[1])+str(' 
'.join(board[2][6]))+str(' '.join(board[2][7]))+str(' '.join(board[2][8])))
    print(str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[2])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[3])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4])+str(grid[4]))
    print(str(' '.join(board[3][0]))+str(' '.join(board[3][1]))+str(' 
'.join(board[3][2]))+str(grid[5])+str(' '.join(board[4][0]))+str(' 
'.join(board[4][1]))+str(' '.join(board[4][2]))+str(grid[6])+str(' 
'.join(board[5][0]))+str(' '.join(board[5][1]))+str(' '.join(board[5][2])))
    print(str(' '.join(board[3][3]))+str(' '.join(board[3][4]))+str(' 
'.join(board[3][5]))+str(grid[5])+str(' '.join(board[4][3]))+str(' 
'.join(board[4][4]))+str(' '.join(board[4][5]))+str(grid[6])+str(' 
'.join(board[5][3]))+str(' '.join(board[5][4]))+str(' '.join(board[5][5])))
    print(str(' '.join(board[3][6]))+str(' '.join(board[3][7]))+str(' 
'.join(board[3][8]))+str(grid[5])+str(' '.join(board[4][6]))+str(' 
'.join(board[4][7]))+str(' '.join(board[4][8]))+str(grid[6])+str(' 
'.join(board[5][6]))+str(' '.join(board[5][7]))+str(' '.join(board[5][8])))
    print(str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[7])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[8])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9])+str(grid[9]))
    print(str(' '.join(board[6][0]))+str(' '.join(board[6][1]))+str(' 
'.join(board[6][2]))+str(grid[10])+str(' '.join(board[7][0]))+str(' 
'.join(board[7][1]))+str(' '.join(board[7][2]))+str(grid[11])+str(' 
'.join(board[8][0]))+str(' '.join(board[8][1]))+str(' '.join(board[8][2])))
    print(str(' '.join(board[6][3]))+str(' '.join(board[6][4]))+str(' 
'.join(board[6][5]))+str(grid[10])+str(' '.join(board[7][3]))+str(' 
'.join(board[7][4]))+str(' '.join(board[7][5]))+str(grid[11])+str(' 
'.join(board[8][3]))+str(' '.join(board[8][4]))+str(' '.join(board[8][5])))
    print(str(' '.join(board[6][6]))+str(' '.join(board[6][7]))+str(' 
'.join(board[6][8]))+str(grid[10])+str(' '.join(board[7][6]))+str(' 
'.join(board[7][7]))+str(' '.join(board[7][8]))+str(grid[11])+str(' 
'.join(board[8][6]))+str(' '.join(board[8][7]))+str(' '.join(board[8][8])))
    grid = ["|","|","-","-","-","|","|","-","-","-","|","|"]
    
for i in range(0, 9):
    printBoard(i)
