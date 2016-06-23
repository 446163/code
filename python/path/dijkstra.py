'''
points_input = int(input("number of points: "))
points_input = points_input + 2
distance_input = ""
grid = []
gridtemp = []
for i in range(points_input):
	for j in range(points_input):
		gridtemp.append("'")
	grid.append(gridtemp)
	gridtemp=[]
	grid[0][0] = "x" 
#creating grid
for i in range(points_input):
	grid[i][1] = "¦"
	grid[1][i] = "―"
	grid[1][1] = "+"
#adding lines

'''
grid = [["x","¦"],["―","+"]]
gridtemp = []
grid_size = 2
def print_grid():
	for item in grid:
		print(' '.join(map(str, item)))
print_grid()

distance_input = "0"

while distance_input != "":
	gridtemp = []
	grid_count = 2
	point_taken = 0
	point_taken2 = 0
	distance_input = input("Distance: ")
	distance_input = distance_input.split()
	print(distance_input)
	for i in range(1,grid_size):
		#print(grid[0][i])
		#print(distance_input[0])
		if grid[0][i] == distance_input[0]:
			point_taken = 1
			point_taken_ref = i
		if grid[0][i] == distance_input[1]:
			point_taken2 = 1
			point_taken_ref2 = i
	if point_taken == 0:
		#add grid +1 in x & y
		for item in grid:
			item.append("'")
		for i in range(grid_size+1):
			gridtemp.append("'")
		grid.append(gridtemp)
		grid_size = grid_size + 1
		for i in range(grid_size):
			grid[i][1] = "¦"
			grid[1][i] = "―"
			grid[1][1] = "+"
		#print_grid()
		print_grid()











'''
		while grid[0][grid_count] != "'":
				grid_count = grid_count + 1
				print_grid
				for x in range(grid_size):
					grid[0].append("'")
					print_grid()
					for j in range(grid_size):
						gridtemp.append("'")
					grid.append(gridtemp)
			grid_size = grid_size + 1		
			for i in range(grid_size):
				grid[i][1] = "¦"
				grid[1][i] = "―"

			grid[0][i] = distance_input[0]
			print_grid()
			print("test")
'''