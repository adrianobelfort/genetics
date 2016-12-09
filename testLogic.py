from logic import *
from view import *
from model import *
from dijkstra import *

def main():
	grid = GridMap(20,20)

	gridPlanner = FlipFiller(LinearFiller(grid))
	gridPlanner.fillFlip(19).fillFlip(9).fillFlip(11).flipOrientation().fillFlip(3).flipOrientation().fillFlip(11).fillFlip(7).fillFlip(19).fillFlip(19)

	chromossome = ChromossomeFactory.build(50, grid.getLimits())
	evaluator = Evaluator()

	individual = Individual(chromossome, evaluator, 0.5, 0.05)

	# Acao do ambiente
	individual.computeAllDistances(grid)

	# Testa Dijkstra
	paths = individual.getPaths()

	#print 'Paths', paths

	spath = shortestPath(paths, chromossome[0], chromossome[-1])

	print 'Shortest path', spath

	path = Path()
	path.setPath(spath)

	choreographer = Choreographer(grid, path)
	choreographer.show()

if __name__ == '__main__':
	main()
