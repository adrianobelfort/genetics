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

def main():
	#testPathShow()
	testPathWithAnimation()

if __name__ == '__main__':
	main()
