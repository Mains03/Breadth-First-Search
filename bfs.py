class Queue:
	def __init__(self):
		self.queue = []

	def push(self, value):
		self.queue.append(value)

	def pop(self):
		return self.queue.pop(0)

	def empty(self):
		return len(self.queue) == 0

class Node:
	def __init__(self, row, column, previous):
		self.row = row
		self.column = column
		self.previous = previous

def breadthFirstSearch(grid):
	""" Performs a breadth first search finding the shortest path
		from 'A' to 'B' along '.' (floors). '#' are walls. """

	start = getStartPosition(grid)
	if start == None:
		print("Start position not found")
		return None

	row = start[0]
	column = start[1]
	queue = Queue()
	queue.push(Node(row,column,None))

	visited = [[False for column in range(len(grid[0]))] for row in range(len(grid))]

	while not queue.empty():
		node = queue.pop()

		if node.row < 0 or node.column < 0:
			continue
		if node.row >= len(grid) or node.column >= len(grid[0]):
			continue
		if grid[node.row][node.column] == 'B':
			return generatePath(node)
		if visited[node.row][node.column]:
			continue
		if grid[node.row][node.column] == '#':
			continue

		queue.push(Node(node.row-1,node.column,node))
		queue.push(Node(node.row+1,node.column,node))
		queue.push(Node(node.row,node.column-1,node))
		queue.push(Node(node.row,node.column+1,node))

		visited[node.row][node.column] = True

	print("Destination not found")
	return None

def getStartPosition(grid):
	for row in range(len(grid)):
		for column in range(len(grid[row])):
			cell = grid[row][column]
			if cell == 'A':
				return (row,column)
	return None

def generatePath(node):
	path = []
	while node != None:
		path.insert(0,[node.row,node.column])
		node = node.previous
	return path
