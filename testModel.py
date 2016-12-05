from model import *

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

def testFlipFiller():
	grid = sampleMap()

	gridFiller = FlipFiller(LinearFiller(grid))
	gridFiller.fillFlip(19).fillFlip(19).fillFlip(19)

	grid.show()

###############################################################################
################################ MAIN FUNCTION ################################
###############################################################################

def main():
	#testExportGrid()
	#testImportGrid()
	#testLinearFiller()
	#testVectorFiller()
	#testPathFiller()
	testFlipFiller()

if __name__ == '__main__':
	main()
