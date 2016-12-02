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

	def show(self):
		for i in range(0, self.xLength):
			for j in range(0, self.yLength):
				if self.map[i][j]:
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

###############################################################################
############################### TEST FUNCTIONS ################################
###############################################################################

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

###############################################################################
################################ MAIN FUNCTION ################################
###############################################################################

def main():
	testExportGrid()
	testImportGrid()

if __name__ == '__main__':
	main()
