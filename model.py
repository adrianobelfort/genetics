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
	def __init__(self, vectorFiller, startLine=0, startColumn=0):
		self.vectorFiller = vectorFiller
		self.startLine = startLine
		self.startColumn = startColumn

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

class FlipFiller(object):
	def __init__(self, linearFiller, startLine=0, startColumn=0, direction='h', way=1):
		self.filler = linearFiller
		self.startLine = startLine
		self.startColumn = startColumn
		self.direction = direction
		self.way = way

	def flipDirection(self):
		if self.direction == 'h':
			self.direction = 'v'
		elif self.direction == 'v':
			self.direction = 'h'
			self.way = -self.way

	def updatePosition(self, offset):
		if self.direction == 'h':
			self.startColumn = self.startColumn + self.way * offset
		elif self.direction == 'v':
			self.startLine = self.startLine + self.way * offset

		self.flipDirection()

	def fillFlip(self, offset):
		self.filler.fillLine(self.startLine, self.startColumn, self.way * offset, self.direction)
		self.updatePosition(offset)
		return self

	def skipFlip(self, offset):
		self.updatePosition(offset)
		return self

class PathIterator(object):
	def __init__(self, path):
		self.path = path
		self.hop = 0

	def next(self):
		if self.hop < self.path.hops():
			point = (self.path.xpath[self.hop], self.path.ypath[self.hop])
			self.hop += 1
		else:
			point = None

		return point

	def previous(self):
		if self.hop >= 0:
			point = (self.path.xpath[self.hop], self.path.ypath[self.hop])
			self.hop -= 1
		else:
			point = None

		return point

	def reset(self):
		self.hop = 0

	def hasNext(self):
		return self.hop < self.path.hops()

class Path(object):
	def __init__(self, xpath=[], ypath=[]):
		self.xpath = xpath
		self.ypath = ypath

	def add(self, x, y):
		self.xpath.append(x)
		self.ypath.append(y)
		return self

	def getPoints(self):
		return (self.xpath, self.ypath)

	def hops(self):
		return len(self.xpath)

	def getIterator(self):
		return PathIterator(self)
