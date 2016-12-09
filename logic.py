from model import *
import math
import numpy as np

# Defines the genes of each individual
class Chromossome(object):
	# @points: list of points (x,y)
	def __init__(self, points):
		self.points = points

	def getPoints(self):
		return points

	def getNumberOfPoints(self):
		return len(points)

class ChromossomeFactory(object):
	@staticmethod
	def createRandomPoint(limits):
		limitX, limitY = limits
		point = (np.random.randint(0, limitX), np.random.randint(0, limitY))
		return point

	@staticmethod
	def build(npoints, limits):
		limitX, limitY = limits
		pointList = []

		for i in range(0, npoints):
			point = ChromossomeFactory.createRandomPoint(limits)
			pointList.append(point)

		# Aqui tenho a lista de pontos completa
		return pointList

# Converts genes into phenotypes
class Individual(object):
	def __init__(self, genes, evaluator, aconnection, bstop):
		self.genes = genes
		self.evaluator = evaluator
		self.createPaths(aconnection, bstop)

	def createPaths(self, aconnection, bstop):
		self.pointGraph = {}
		pointList = self.genes

		for point in pointList:
			self.pointGraph[point] = {}

			for targetPoint in pointList:
				if point == targetPoint:
					continue

				if np.random.rand() < aconnection:
					# TODO: Mudar aqui para None depois
					self.pointGraph[point][targetPoint] = None #math.sqrt((targetPoint[0] - point[0])**2 + (targetPoint[1] - point[1])**2)

				if np.random.rand() < bstop:
					break

	def fitness(self, grid):
		pass

	def reproduce(self):
		pass

	def getPaths(self):
		return self.pointGraph

	def computeAllDistances(self, grid):
		self.evaluator.computeAllDistances(self.getPaths(), grid.obstacles())

	#def evaluate(self):
	#	self.evaluator.computeDistance()

# Abordagem polimorfica onde os individuos sabem obter seus proprios resultados
# com base nos genes e repassam os dados para quem chama (avalia)

class LineSegment(object):
	def __init__(self, pointA, pointB):
		self.xa, self.ya = pointA
		self.xb, self.yb = pointB

		deltaY = self.yb - self.ya
		deltaX = self.xb - self.xa

		if deltaX == 0:
			self.m = None
		else:
			self.m = deltaY/deltaX

	def evaluate(self, x, y):
		if self.xa <= x and x <= self.xb:
			if self.m is None:
				if x == self.xa:
					return y
				else:
					return float('inf')
			else:
				return self.ya + self.m * (x - self.xa)
		else:
			return float('inf')	# Nao pertence ao segmento

	def distance(self):
		return math.sqrt((self.xb - self.xa)**2 + (self.yb-self.ya)**2)

class Evaluator(object):
	def detectCollision(self, point, lineSegment):
		x, y = point
		segmentY = lineSegment.evaluate(x,y)

		if y <= segmentY and segmentY <= y+1:
			return True
		else:
			return False

	def computeDistance(self, pointA, pointB, obstacles):
		segment = LineSegment(pointA, pointB)

		# Comecei a mudar aqui
		for obstacle in obstacles:
			if not self.detectCollision(obstacle, segment):
				continue
			else:
				return float('inf')

		return segment.distance()

	def computeAllDistances(self, pointGraph, obstacles):
		for v in pointGraph:
			for w in pointGraph[v]:
				pointGraph[v][w] = self.computeDistance(v, w, obstacles)

######################################################################
def main():
	pass

if __name__ == '__main__':
	main()
