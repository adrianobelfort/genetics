from model import *
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.animation as animation

# this function gives the path to the choreographer!!
# encapsulate it into another class!
def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

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
		fig1 = plt.figure()

		# Make a color map of fixed colors
		cmap = mpl.colors.ListedColormap(['white', 'blue'])
		bounds = [Choreographer.lowerBoundary, Choreographer.turningPoint, Choreographer.upperBoundary]
		norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

		# Get the points from model
		gridpoints = self.prepare()

		# animation

		data = np.random.randint(0, 20, (2,50))
		data[0].sort()
		data[1].sort()

		print data

		l, = plt.plot([], [], 'r-')
		line_ani = animation.FuncAnimation(fig1, update_line, 50, fargs=(data, l),
		                                   interval=100, blit=True)

		# end of animation

		# Tell imshow about color map so that only set colors are used
		img = plt.imshow(gridpoints,interpolation='nearest', cmap = cmap,norm=norm, origin='lower')

		# Set labels
		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title('Region grid')

		# Make a color bar
		plt.colorbar(img,cmap=cmap,norm=norm,boundaries=bounds,ticks=[Choreographer.lowerBoundary,Choreographer.upperBoundary], format=ticker.FuncFormatter(self.formatColorbarLabel))

		plt.show()
