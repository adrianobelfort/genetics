from model import *
import math

# Defines the genes of each individual
class Gene(object):
	# @points: list of points (x,y)
	def __init__(self, points):
		self.points = points

	def getPoints(self):
		return points

	def getNumberOfPoints(self):
		return len(points)

# Converts genes into phenotypes
class Individual(object):
	def __init__(self, gene, evaluator):
		self.gene = gene
		self.evaluator = evaluator

	def fitness(self, grid):
		pass

	def reproduce(self):
		pass

# Move to controller
class Environment(object):
	pass

# Abordagem polimórfica onde os indivíduos sabem obter seus próprios resultados
# com base nos genes e repassam os dados para quem chama (avalia)

class LineSegment(object):
	def __init__(self, pointA, pointB):
		self.xa, self.ya = pointA
		self.xb, self.yb = pointB
		self.m = (self.yb - self.ya)/(self.xb - self.xa)

	def evaluate(self, x):
		if self.xa <= x and x <= self.xb:
			return self.ya + self.m * (x - self.xa)
		else:
			return float('inf')	# Nao pertence ao segmento

	def distance(self):
		return math.sqrt((self.xb - self.xa)**2 + (self.yb-self.ya)**2)

class Evaluator(object):
	def __init__(self):
		pass

	def detectCollision(self, point, lineSegment):
		x, y = point
		segmentY = lineSegment.evaluate(x)

		if y <= segmentY and segmentY <= y+1:
			return True
		else
			return False

	def computeDistance(self, pointA, pointB, obstacle):
		segment = LineSegment(pointA, pointB)

		if self.detectCollision(obstacle, segment):
			return segment.distance()
		else:
			return float('inf')

######################################################################
def main():
	pass

if __name__ == '__main__':
	main()
