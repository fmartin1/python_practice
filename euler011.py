# Fill a grid with the values
grid = []
with open("euler011_data.txt") as fp:
    for line in fp:
        row = []
        for number in line.split(" "):
            row.append( int(number) )
        grid.append(row)

def hor_value():
	max_product = 0
	tmp_product = 0
	for row in grid:
		for i in xrange( len(row) - 3 ):
			tmp_product = ( row[i] * row[i+1] * row[i+2] * row[i+3] )
			if tmp_product > max_product: max_product = tmp_product
	return max_product
	
def getcol(index):
	col = []
	for row in grid:
		col.append( row[index] )
	return col

def ver_value():
	max_product = 0
	tmp_product = 0
	for i in xrange( len(grid[0]) ):
		col = getcol(i)
		for j in xrange( len(col) - 3 ):
			tmp_product = ( col[j] * col[j+1] * col[j+2] * col[j+3] )
			if tmp_product > max_product: max_product = tmp_product
	return max_product

def dia_value1():
	max_product = 0
	tmp_product = 0
	for row in xrange( len(grid) - 3 ):
		for col in xrange( len(grid[row]) - 3 ):
			tmp_product = ( grid[row][col] * grid[row+1][col+1] * grid[row+2][col+2] * grid[row+3][col+3] )
			if tmp_product > max_product: max_product = tmp_product
	return max_product
	
def dia_value2():
	max_product = 0
	tmp_product = 0
	for row in xrange( len(grid) - 3 ):
		for col in xrange( len(grid[row]) - 3 ):
			tmp_product = ( grid[row][col+3] * grid[row+1][col+2] * grid[row+2][col+1] * grid[row+3][col] )
			if tmp_product > max_product: max_product = tmp_product
	return max_product
	
print hor_value()	
print ver_value()
print dia_value1()
print dia_value2()