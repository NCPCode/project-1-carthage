import pygame

print(1)

WINDOW_SIZE = [500, 500]

class Player:
	def __init__(self, color, coords):
		self.color = color
		self.initial_coords = list(coords)
		self.coords = coords
		self.speed = 10
		self.size = [10, 75]

	def move(self, direction):
		if direction == "up":
			if (self.coords[1] > 0):
				self.coords[1] -= self.speed
		elif direction == "down":
			if (self.coords[1] < WINDOW_SIZE[1]-self.size[1]):
				self.coords[1] += self.speed

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.coords, self.size))

class Ball:
	def __init__(self, color, coords):
		self.color = color
		self.initial_coords = list(coords)
		self.coords = coords
		self.speed = 2
		self.size = [15, 15]
		self.direction = [0.5, -1]

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.coords, self.size))

	def move(self):
		if (self.coords[1] < 0):
			self.direction[1] = 1
		if (self.coords[1] >= WINDOW_SIZE[1] - self.size[1]):
			self.direction[1] = -1

		self.coords[0] += self.direction[0] * self.speed
		self.coords[1] += self.direction[1] * self.speed

	def has_collided(self, player):
		return ((self.coords[0] < player.coords[0] + player.size[0]) and
			(player.coords[0] < self.coords[0] + self.size[0]) and
			(self.coords[1] < player.coords[1] + player.size[1]) and
			(player.coords[1] < self.coords[1] + self.size[1]))

player1 = Player(
  pygame.Color('white'),
  [490, 250],
)

player2 = Player(
  pygame.Color('white'),
  [0, 250],
)

ball = Ball(
  pygame.Color('white'),
  [WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2]
)


window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


while True: 
	# collect events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

  # do some processing
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		player1.move('up')
	elif keys[pygame.K_DOWN]:
		player1.move('down')

	if keys[pygame.K_w]:
		player2.move('up')
	elif keys[pygame.K_s]:
		player2.move('down')

	ball.move()

	if ball.has_collided(player1):
		ball.direction[0] = -1
		
	if ball.has_collided(player2):
		ball.direction[0] = 1

	window.fill(pygame.Color("black"))


	player1.draw(window)
	player2.draw(window)
	ball.draw(window)

	# display
	pygame.display.update()
	clock.tick(60)

