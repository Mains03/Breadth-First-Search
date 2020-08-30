import pygame

backgroundColour = (0,0,0)
screen = None
screenWidth = 500
screenHeight = 500

def createWindow(grid):
	global screen, screenWidth, screenHeight

	screen = pygame.display.set_mode((screenWidth,screenHeight))
	pygame.display.set_caption("Breadth First Search")
	
	cellWidth = (screenWidth-50)//len(grid[0])
	cellHeight = (screenHeight-50)//len(grid)

	for row in range(len(grid)):
		for column in range(len(grid[row])):
			cell = grid[row][column]
			x = 25+column*cellWidth
			y = 25+row*cellHeight
			if cell == 'A':
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(x,y,cellWidth,cellHeight))
			elif cell == 'B':
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,cellWidth,cellHeight))
			elif cell == '#':
				pygame.draw.rect(screen, (255,255,255), pygame.Rect(x,y,cellWidth,cellHeight))

	pygame.display.flip()

def drawPath(grid,path):
	global screen, screenWidth, screenHeight

	cellWidth = (screenWidth-50)//len(grid[0])
	cellHeight = (screenHeight-50)//len(grid)

	for position in path[1:len(path)-1]:
		x = 25+position[1]*cellWidth
		y = 25+position[0]*cellHeight
		pygame.draw.rect(screen, (0,0,255), pygame.Rect(x,y,cellWidth,cellHeight))

	pygame.display.flip()

def closeWindow():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			return True
	return False
