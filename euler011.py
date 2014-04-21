# Fill a grid with the values
# Declare grid as empty list
grid = []

# Open file with memory management
with open("euler011_data.txt") as data:
    for line in data:
		# Declare empty list
        row = []
        for number in line.split(" "):
            row.append( int(number) )
        grid.append(row)

# Rows are naturally obtained as a list
# now we need to get columns the same way:	
def getcolumn(index):
	col = []
	for row in grid:
		col.append( row[index] )
	return col
	
def highest_horizonta_value():
	max_product = 0
	tmp_product = 0
	for row in grid:
		for i in xrange( len(row) - 3 ):
			tmp_product = ( row[i] * row[i+1] * row[i+2] * row[i+3] )
			if tmp_product > max_product: max_product = tmp_product
	return max_product
	
def highest_vertical_value():
	max_product = 0
	tmp_product = 0
	for i in xrange( len(grid[0]) ):
		col = getcolumn(i)
		for j in xrange( len(col) - 3 ):
			tmp_product = ( col[j] * col[j+1] * col[j+2] * col[j+3] )
			if tmp_product > max_product: max_product = tmp_product
	return max_product

def highest_diagonal_value():
	max_product = 0
	tmp_product = 0
	for row in xrange( len(grid) - 3 ):
		for col in xrange( len(grid[row]) - 3 ):
			tmp_product = ( grid[row][col] * grid[row+1][col+1] 
						  * grid[row+2][col+2] * grid[row+3][col+3] )
			if tmp_product > max_product: max_product = tmp_product
	return max_product
	
def highest_diagonal_value_inverted():
	max_product = 0
	tmp_product = 0
	for row in xrange( len(grid) - 3 ):
		for col in xrange( len(grid[row]) - 3 ):
			tmp_product = ( grid[row][col+3] * grid[row+1][col+2] 
							* grid[row+2][col+1] * grid[row+3][col] )
			if tmp_product > max_product: max_product = tmp_product
	return max_product
	
print highest_horizonta_value()	
print highest_vertical_value()
print highest_diagonal_value()
print highest_diagonal_value_inverted()