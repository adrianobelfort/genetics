from model import *
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

class Choreographer(object):
	# Constants
	lowerBoundary = -5
	upperBoundary = 5
	turningPoint = 0

	def __init__(self, grid):
		self.grid = grid

	def formatColorbarLabel(x, position):
		if x > Choreographer.turningPoint:
			colorbarlabel = 'Obstacle'
		else:
			colorbarlabel = 'Free'

		return colorbarlabel

	formatColorbarLabel = staticmethod(formatColorbarLabel)

	def prepare(self):
		gridlist = self.grid.toList()

		gridpoints = [[Choreographer.upperBoundary if obstacle else Choreographer.lowerBoundary for obstacle in obstacles] for obstacles in gridlist]
		gridpoints = np.array(gridpoints)

		return gridpoints

	def show(self):
		# Make a color map of fixed colors
		cmap = mpl.colors.ListedColormap(['white', 'blue'])
		bounds = [Choreographer.lowerBoundary, Choreographer.turningPoint, Choreographer.upperBoundary]
		norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

		# Get the points from model
		gridpoints = self.prepare()

		# Tell imshow about color map so that only set colors are used
		img = plt.imshow(gridpoints,interpolation='nearest', cmap = cmap,norm=norm)

		# Set labels
		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title('Region grid')

		# Make a color bar
		plt.colorbar(img,cmap=cmap,norm=norm,boundaries=bounds,ticks=[Choreographer.lowerBoundary,Choreographer.upperBoundary], format=ticker.FuncFormatter(self.formatColorbarLabel))

		plt.show()
