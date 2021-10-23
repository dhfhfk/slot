import pygame
import sys
import random
import logic
import sound

class SlotMachine:
	def __init__(self):	
		pygame.init()
		self.screen = pygame.display.set_mode((1366,768))
		self.clock = pygame.time.Clock()
		self.screen.fill((0,0,0))
		self.font0 = pygame.font.Font("fonts/DungGeunMo.ttf", 100)
		self.font1 = pygame.font.Font("fonts/DungGeunMo.ttf", 50)
		self.font2 = pygame.font.Font("fonts/DungGeunMo.ttf", 20)
		pygame.display.set_caption('룰렛 머신')
		pygame.display.update()

		self.icon0 = pygame.image.load("images/Bananas.png")
		self.icon1 = pygame.image.load("images/Watermelon.png")
		self.icon2 = pygame.image.load("images/Plum.png")
		self.icon3 = pygame.image.load("images/Lemon.png")
		self.icon4 = pygame.image.load("images/Seven.png")
		self.icon5 = pygame.image.load("images/Cherries.png")
		self.icon6 = pygame.image.load("images/Orange.png")
		self.icon7 = pygame.image.load("images/Bar.png")
		self.icon8 = pygame.image.load("images/Bigwin.png")

		self.icon0.convert()
		self.icon1.convert()
		self.icon2.convert()
		self.icon3.convert()
		self.icon4.convert()
		self.icon5.convert()
		self.icon6.convert()
		self.icon7.convert()
		self.icon8.convert()

		self.winnings_to_display = 0.0

		self.main()

	def main(self):

		self.set_Slot()
		main_loop = True
		count = 0
		while main_loop == True:
			
			self.clock.tick(5)			
			self.screen.fill((0,0,0))
			self.background()
			self.fruits()
			self.panel()
			
			pygame.display.update()

			
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q :
						pygame.quit()
						sys.exit()
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == pygame.K_SPACE:
							self.winnings_to_display = 0.0
							self.bet()

					if event.key == pygame.K_UP:
						self.bet_up()

					if event.key == pygame.K_DOWN:
						self.bet_down()


	def background(self):
		pass


	def fruits(self):

		for i in self.wheel0:
			if 576 > i[1] > -192:
				self.screen.blit(i[0], (345, i[1]))
		for i in self.wheel1:
			if 576 > i[1] > -192:
				self.screen.blit(i[0], (567, i[1]))
		for i in self.wheel2:
			if 576 > i[1] > -192:
				self.screen.blit(i[0], (789, i[1]))

	def panel(self):

		bottom_rect = pygame.draw.rect(self.screen, (0,0,0), [0,576,1366,768])

		# credit_label = self.font1.render("칩: %.f개" % game.player_money,1, (255,255,255))
		# self.screen.blit(credit_label, (150,630))

		bet_label = self.font1.render("베팅: %.f개" % game.denomination,1, (255,255,255))
		self.screen.blit(bet_label, (400,630))

		winningX_label = self.font1.render("수익: %.f개" % (self.winnings_to_display),1, (255,255,255))
		self.screen.blit(winningX_label, (690,630))

		help_string = "스페이스바로 돌리기 | 위 화살표로 베팅 올리기 | 아래 화살표로 베팅 내리기"
		help_label = self.font2.render(help_string, 1, (100,100,100))
		self.screen.blit(help_label, (300,715))

	def animation(self,t0,t1, w0_speed, w1_speed, w2_speed):
		while t0 <= self.t < t1:
			self.clock.tick(90)
			self.screen.fill((0,0,0))
			for i in self.wheel0:
				if i[1] < 576:
					i[1] += w0_speed
				else:
					i[1] = -960 + w0_speed
			for i in self.wheel1:
				if i[1] < 576:
					i[1] += w1_speed
				else:
					i[1] = -960  + w1_speed
			for i in self.wheel2:
				if i[1] < 576:
					i[1] += w2_speed
				else:
					i[1] = -960  + w2_speed
			self.fruits()
			self.panel()
			pygame.display.update()
			self.t += 1														

	def spin_Slot(self):	
		self.t = -50
		
		self.animation(-64,   12, 96, 96, 96)
		self.animation( 12,   24, 48, 96, 96)
		self.animation( 24,   40, 24, 96, 96)
		self.animation( 40,   52, 16, 96, 96)
		self.animation( 52,   64,  8, 96, 96)
		self.animation( 64,   82,  4, 48, 48)
		self.animation( 82,   94,  2, 24, 48)

		self.animation( 94,  106,  0, 16, 24)
		self.animation(106,  122,  0,  8, 24)
		self.animation(122,  134,  0,  4, 12)
		self.animation(134,  142,  0,  2,  8)
		
		self.animation(142,  162,  0,  0,  8)
		self.animation(162,  200,  0,  0,  4)
		self.animation(200,  228,  0,  0,  2)

		pygame.event.get()

	def set_Slot(self):
		y=0
		self.wheel0 = [[self.icon0, y], [self.icon1, y], [self.icon2, y], [self.icon3, y], [self.icon4, y], [self.icon5, y], [self.icon6, y], [self.icon7, y], [self.icon8, y]]
		self.wheel1 = [[self.icon6, y], [self.icon0, y], [self.icon2, y], [self.icon4, y], [self.icon8, y], [self.icon1, y], [self.icon3, y], [self.icon5, y], [self.icon7, y], ]
		self.wheel2 = [[self.icon4, y], [self.icon7, y], [self.icon3, y], [self.icon1, y], [self.icon0, y], [self.icon8, y], [self.icon5, y], [self.icon2, y], [self.icon6, y], ]

		for i in (self.wheel2, self.wheel1, self.wheel0):
			i[0][1] = 576
			i[1][1] = 384
			i[2][1] = 192
			i[3][1] = 0
			i[4][1] = -192
			i[5][1] = -384
			i[6][1] = -576
			i[7][1] = -768
			i[8][1] = -960

	def shift_Slot(self, sym):
		for i in range(sym[0]):
			self.wheel0.append(self.wheel0.pop(0))
		for i in range(sym[1]):
			self.wheel1.append(self.wheel1.pop(0))
		for i in range(sym[2]):
			self.wheel2.append(self.wheel2.pop(0))

		for i in (self.wheel2, self.wheel1, self.wheel0):
			i[0][1] = 576
			i[1][1] = 384
			i[2][1] = 192
			i[3][1] = 0
			i[4][1] = -192
			i[5][1] = -384
			i[6][1] = -576
			i[7][1] = -768
			i[8][1] = -960				
						
	def bet_up(self):
		
		if game.denomination < 5.0:
			game.denomination += 1

	def bet_down(self):
		
		if game.denomination > 1:
			game.denomination -= 1

	def bet(self):
		
		if game.denomination > game.player_money:
			return

		sound.roll_sound()
		winningX = game.make_bet()

		shiftcode = self.get_shiftcode(winningX)


		self.set_Slot()
		self.shift_Slot(shiftcode)
		self.spin_Slot()
		sound.play_sound(winningX)
		self.winnings_to_display = winningX * game.denomination
		game.update()
		winpoint = (winningX*game.denomination)
		if winpoint == 0:
			print("꽝")
		else:
			print(winpoint,"칩 당첨")

		self.panel()
		pygame.display.update()
		pygame.event.get()

	def get_shiftcode(self, winningX):

		symbol_codes = {
			'Bigwin':    (0,1,4),
			'Banana':    (1,7,3),
			'Watermelon':(2,2,2),
			'Plum':      (3,8,6),
			'Lemon':     (4,3,1),
			'Seven': 	 (5,0,8),
			'Cherries':  (6,4,5),
			'Orange':	 (7,6,7),
			'Bar':		 (8,5,0)

		}
		if winningX == 100:
			return symbol_codes['Bigwin']
		if winningX == 50:
			return symbol_codes['Bigwin']
		if winningX == 25:
			return symbol_codes['Plum']
		if winningX == 15:
			return symbol_codes['Banana']
		if winningX == 10:
			return symbol_codes['Watermelon']
		if winningX == 7:
			return symbol_codes['Seven']
		if winningX == 5:
			return symbol_codes['Plum']
		if winningX == 4:
			return symbol_codes['Bar']
		if winningX == 3:
			return symbol_codes['Cherries']
		if winningX == 2:
			return symbol_codes['Orange']
		if winningX == 1:
			return symbol_codes['Lemon']
		if winningX == 0:
			while True:
				code = (random.randrange(9), random.randrange(9),random.randrange(9),)
				if code not in symbol_codes.values():
					return code

if __name__ == '__main__':

	game = logic.Game()
	app = SlotMachine()






