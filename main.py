import pygame
from text import Text
from Toss import Alien
from stone import Block


def intersect(r1, r2):
# This function returns true if two rectangles have intersected
    if (r1.x < r2.x + r2.width) and (
	r1.x + r1.width > r2.x) and (
	r1.y < r2.y + r2.height) and (
	r1.height + r1.y > r2.y):
	        return True
 
    return False


if __name__ == "__main__":
	# Initialize Pygame
	pygame.init()
	pygame.display.set_caption('CSC 284 Game')
	fpsclock = pygame.time.Clock()

	# Build the game surface
	gameSurfaceWidth, gameSurfaceHeight = 1000, 600
	gameSurfaceColor = (240, 240, 200)
	gameSurface = pygame.display.set_mode((gameSurfaceWidth, gameSurfaceHeight))

	# Initialize Ground Plane
	groundHeight = 500

	# Initialize Alien
	AliensSize = 5
	xPosition = 50
	yPosition = groundHeight-AliensSize
	xv = 0 # x---axis velocity
	yv = 0 # Axis velocity
	alien = Alien(xPosition, yPosition, AliensSize, (255, 0, 0))
	Alienismoving = False

	# Initialize blocks
	numBlocks = 9 # number of blocks
	blockCount = numBlocks
	blockColor = (20, 20, 255)
	blockSize = 45
	blocks = []

	for A in range(0, 3):
		for B in range(1, 4):
			blocks.append(Block(500 + A * blockSize, groundHeight - B * blockSize, blockSize, blockColor))

	# Initializing the  Score
	score = 0
	score_string = 'Score: {}'
	score_text = Text(0, 0, score_string.format(score))
	hiScore = 0
	hiScore_string = 'High Score: {}'
	hiScore_text = Text(350, 0, hiScore_string.format(hiScore))

	# the pysics component
	dt = .1
	g = 6.41
	R = .7
	eta = .5

	# initializing the game state
	gameOver = False
	waitingForNewGame = False

	while True:
		print(blockCount)
		for event in pygame.event.get():
			if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
				pygame.quit()
				exit()

			gameOver = blockCount <= 0

			if not gameOver:
				
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouseDownPos = pygame.mouse.get_pos()
				else:
				  mouseDownPos = [0, 0]

				if event.type == pygame.MOUSEBUTTONUP:
				  mouseUpPos = pygame.mouse.get_pos()
				else:
				  mouseUpPos = [0, 0]  

				xv = mouseUpPos[0] - mouseDownPos[0]
				yv = mouseUpPos[1] - mouseDownPos[1]
				Alienismoving = True
				# gameOver = True


			elif waitingForNewGame:
				
				if (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_y):
					# Reset the score
					score = 0

					# Reset the game state
					gameOver = False
					waitingForNewGame = False

					# Reset the alien
					Alienismoving = False
					alien.set_position((30, groundHeight - AliensSize))
					xPosition, yPosition = alien.get_position()
					# Reset the blocks
					for block in blocks:
						block.set_visible(True)
					blockCount = numBlocks

				if event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_n:
					pygame.quit()
					exit()

		# if the aleins goes outof the bound, the game stops
		if (not (int(AliensSize/2) < xPosition < gameSurfaceWidth - int(AliensSize/2))) or \
		(not (int(AliensSize/2) < yPosition < gameSurfaceHeight - int(AliensSize/2))):
			Alienismoving = False
			alien.set_position((30, groundHeight - AliensSize))
			xPosition, yPosition = alien.get_position()

		# If the aliens has slowed down, stop it completely
		if yv < 0.0001 and xv < 0.0001:
			Alienismoving = False

		if Alienismoving:
			if yPosition > groundHeight-(AliensSize): # The aliens has bounced
				yv = -R * yv
				xv = eta * xv
				yPosition = groundHeight-(AliensSize) # ensure the aliens never goes below the ground
				xPosition += dt * xv

			else:
				yv = yv + g * dt
				yPosition += dt * yv
				xPosition += dt * xv

		# If the aliens has slowed down, stop it completely
		if yv < 0.0001 and xv < 0.0001:
			Alienismoving = False


		# Move the aliens to its new position
		alien.set_position((int(xPosition), int(yPosition)))

		# Remove blocks that have been hit and update the score
		for block in blocks:
			if intersect(block.get_rect(), alien.get_rect()):
				if block.get_visible():
					block.set_visible(False)
					blockCount -= 1
					score += 1
					if score >= hiScore:
						hiScore = score


		# Reset the background
		gameSurface.fill(gameSurfaceColor)

		# Draw ground plane
		ground_Line = pygame.draw.line(gameSurface, (0, 0, 0), (0, groundHeight), (gameSurfaceWidth, groundHeight), 3)

		# Draw the aleins
		alien.draw(gameSurface)

		# Draw blocks
		for block in blocks:
			block.draw(gameSurface)

		# Drawing the score
		# score_text = Text(0, 0, score_string.format(score))
		score_text.set_message(score_string.format(score))
		score_text.draw(gameSurface)

		hiScore_text.set_message(hiScore_string.format(hiScore))
		hiScore_text.draw(gameSurface)

		pygame.display.flip()

		# Prompt for new game
		if not Alienismoving and gameOver:
			new_game_string = 'New Game? Press [Y] or [N]'
			new_game_text = Text(90, 150, new_game_string)
			new_game_text.draw(gameSurface)
			waitingForNewGame = True

			pygame.display.update()
			fpsclock.tick(30)