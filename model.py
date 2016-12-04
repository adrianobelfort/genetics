import json

class GridMap(object):
	def __init__(self, xLength, yLength, obstacles = None):
		self.xLength = xLength
		self.yLength = yLength

		self.map = [[False for j in range(yLength)] for i in range(xLength)]

		if obstacles is not None:
			for x, y in obstacles:
				self.map[x][y] = True

	def at(self, x, y):
		return self.map[x][y]

	def setPosition(self, x, y, occupied):
		self.map[x][y] = occupied
		return self

	def setObstacle(self, x, y):
		return self.setPosition(x, y, True)

	def setFree(self, x, y):
		return self.setPosition(x, y, False)

	def serialForm(self):
		mappings = []

		for i in range(0, self.xLength):
			for j in range(0, self.yLength):
				if self.map[i][j]:
					mappings.append((i,j))

		return mappings

	def toList(self):
		gridlist = []

		for i in range(0, self.xLength):
			sublist = []
			for j in range(0, self.yLength):
				sublist.append(self.map[i][j])
			gridlist.append(sublist)

		return gridlist

	def show(self):
		for i in range(0, self.xLength):
			for j in range(0, self.yLength):
				if self.map[self.xLength-1 - i][j]:
					print 'o',
				else:
					print '.',
			if j == self.yLength - 1:
				print ''

class GridManager(object):
	limitsKey = 'limits'
	gridKey = 'grid'

	def exportGrid(grid, filename):
		with open(filename, 'w') as outfile:
			serialGrid = grid.serialForm()
			dictionary = {GridManager.limitsKey: [grid.xLength, grid.yLength], GridManager.gridKey: serialGrid}
			json.dump(dictionary, outfile)

	def importGrid(filename):
		with open(filename, 'r') as infile:
			loadedGrid = json.load(infile)

		x, y = loadedGrid[GridManager.limitsKey]
		obstacles = loadedGrid[GridManager.gridKey]

		return GridMap(x, y, obstacles)

	exportGrid = staticmethod(exportGrid)
	importGrid = staticmethod(importGrid)

class LinearFiller(object):
	def __init__(self, gridMap):
		self.grid = gridMap

	def fillLine(self, startLine, startColumn, offset, direction='h'):
		linearRange = range(0, offset+1) if offset >= 0 else range(0, offset-1, -1)

		for i in linearRange:
			if direction == 'h':
				self.grid.setObstacle(startLine, startColumn + i)
			elif direction == 'v':
				self.grid.setObstacle(startLine + i, startColumn)

class VectorFiller(object):
	def __init__(self, linearFiller):
		self.linearFiller = linearFiller

	def fillVector(self, startLine, startColumn, direction, startingDirection='h'):
		columnDirection, lineDirection = direction

		if startingDirection == 'h':
			self.linearFiller.fillLine(startLine, startColumn, columnDirection, 'h')
			self.linearFiller.fillLine(startLine, startColumn + columnDirection, lineDirection, 'v')
		elif startingDirection == 'v':
			self.linearFiller.fillLine(startLine, startColumn, lineDirection, 'v')
			self.linearFiller.fillLine(startLine + lineDirection, startColumn, columnDirection, 'h')

class PathFiller(object):
	def __init__(self, vectorFiller):
		self.vectorFiller = vectorFiller
		self.startLine = 0
		self.startColumn = 0

	def fillPath(self, direction, startingDirection='h', startLine=None, startColumn=None):
		columnDirection, lineDirection = direction

		if startLine is None or startColumn is None:
			startLine = self.startLine
			startColumn = self.startColumn

		self.vectorFiller.fillVector(startLine, startColumn, (columnDirection, lineDirection), startingDirection)

		self.startLine = startLine + lineDirection
		self.startColumn = startColumn + columnDirection

		return self

	def skipPath(self, direction):
		columnDirection, lineDirection = direction

		self.startLine = self.startLine + lineDirection
		self.startColumn = self.startColumn + columnDirection

		return self

###############################################################################
############################### TEST FUNCTIONS ################################
###############################################################################

def sampleMap():
	return GridMap(20,20)

def testCreateAndSetGrid():
	grid = GridMap(20,20)
	grid.setObstacle(0,0).setObstacle(0,1).setObstacle(15,10).setObstacle(4,5)
	return grid

def testImportGrid():
	grid = GridManager.importGrid('grid.json')
	grid.show()

def testExportGrid():
	grid = testCreateAndSetGrid()
	GridManager.exportGrid(grid, 'grid.json')

def testLinearFiller():
	grid = GridMap(20,20)
	gridFiller = LinearFiller(grid)

	gridFiller.fillLine(0,0, 4, 'h')
	grid.show()

def testVectorFiller():
	grid = sampleMap()

	gridFiller = VectorFiller(LinearFiller(grid))
	gridFiller.fillVector(0,0,(4,5), 'h')

	grid.show()

def testPathFiller():
	grid = sampleMap()

	gridFiller = PathFiller(VectorFiller(LinearFiller(grid)))
	gridFiller.fillPath((3,3)).fillPath((2,5)).skipPath((2,0)).fillPath((4,0))

	grid.show()

###############################################################################
################################ MAIN FUNCTION ################################
###############################################################################

def main():
	#testExportGrid()
	#testImportGrid()
	#testLinearFiller()
	#testVectorFiller()
	testPathFiller()

if __name__ == '__main__':
	main()
