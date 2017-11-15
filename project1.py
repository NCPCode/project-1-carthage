import pygame


class Player:
	def __init__(self, color, coords):
		self.color = color
		self.initial_coords = list(coords)
		self.coords = coords
		self.speed = 10

	def move(self, direction):
		if direction == "up":
			self.coords[1] -= self.speed
		elif direction == "down":
			self.coords[1] += self.speed

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.coords, [10, 50])) 

player1 = Player(
  pygame.Color('white'),
  [0, 0],
)

player2 = Player(
  pygame.Color('white'),
  [490, 0],
)

window = pygame.display.set_mode((500, 500))
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

	player1.draw(window)
	player2.draw(window)

	# display
	window.fill(pygame.Color("black"))
	pygame.display.update()
	clock.tick(60)

