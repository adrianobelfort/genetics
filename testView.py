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

def main():
	testPathShow()

if __name__ == '__main__':
	main()
