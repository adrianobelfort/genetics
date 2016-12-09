from view import *

###############################################################################
############################### TEST FUNCTIONS ################################
###############################################################################

###############################################################################
################################ MAIN FUNCTION ################################
###############################################################################

def testSimpleShow():
	grid = GridMap(10, 10)
	grid.setObstacle(3,5).setObstacle(6,4)

	choreographer = Choreographer(grid)

	choreographer.show()

def testPathShow():
	grid = GridMap(20,20)
	choreographer = Choreographer(grid)

	gridPlanner = PathFiller(VectorFiller(LinearFiller(grid)))

	gridPlanner.fillPath((4,5)).skipPath((2,2)).fillPath((0,7)).fillPath((6,1))

	choreographer.show()

def testPathWithAnimation():
	grid = GridMap(20,20)
	path = Path()

	gridPlanner = PathFiller(VectorFiller(LinearFiller(grid)))
	gridPlanner.fillPath((4,5)).skipPath((2,2)).fillPath((0,7)).fillPath((6,1))

	choreographer = Choreographer(grid, path)

	path.add(0,0).add(1,1).add(2,2).add(3,3).add(4,4).add(5,5)

	choreographer.show()

def testPresentation():
	grid = GridMap(20,20)
	path = Path()

	path.add(18,1).add(15,5).add(12,5).add(10,6).add(9,7).add(7,6).add(4,5).add(3,6).add(3,13).add(5,13).add(7,15).add(13,18)

	gridPlanner = FlipFiller(LinearFiller(grid))
	gridPlanner.fillFlip(19).fillFlip(9).fillFlip(11).flipOrientation().fillFlip(3).flipOrientation().fillFlip(11).fillFlip(7).fillFlip(19).fillFlip(19)

	choreographer = Choreographer(grid, path)
	choreographer.show()

def main():
	#testPathShow()
	#testPathWithAnimation()
	testPresentation()

if __name__ == '__main__':
	main()
