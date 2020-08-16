import pygame
import os
from time import sleep
import random
pygame.init()

class Object:
	def __init__(self,x,y,w,h,name):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.name=name
		self.image=None
		objects.append(self)
	
	def load(self):
		
		cur_path = os.path.dirname(__file__)
		new_path = os.path.relpath('./images', cur_path)
	
		self.image=pygame.image.load(new_path+"/"+"{}.png".format(self.name))
		self.image = pygame.transform.scale(self.image, (self.w, self.h))

	def show(self,screen):
		screen.blit(self.image,(int(self.x),int(self.y)))
		
class Button(Object):
	def checkForClick(self,event,function):
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.button==1:
				if pygame.Rect(int(self.x),int(self.y),self.w,self.h).collidepoint(pygame.mouse.get_pos()):
					print("you left kicked me!")
					function(self.name)


def setupScreen(screen,width,height):
	#Line in the middle to split the screen
	pygame.draw.line(screen,(153,77,0),(int(width/2),0),(int(width/2),height),7)
	#Box around player1 
	pygame.draw.rect(screen,(80,170,60),(45,95,305,305))
	pygame.draw.rect(screen,(65,153,47),(45,95,305,305),10)
	#Box around player2
	pygame.draw.rect(screen,(80,170,60),(int(45+width/2),95,305,305))
	pygame.draw.rect(screen,(65,153,47),(int(45+width/2),95,305,305),10)
	#Little squares for choices to go
def loadImages(objects):
	for i in objects:
		i.load()


def setChoice(name):
	global choice,madeChoice
	choice=name
	print(choice)
def displayMessage(message,x,y,font,screen):
	textsurface = font.render(message, False, (27,68,140))
	screen.blit(textsurface,(x,y))
def game(choice,screen):
	global message
	if choice =="Rock":#prob showing for just a split second
		objects[3].show(screen)
	elif choice=="Paper":
		objects[4].show(screen)
	elif choice=="Scissors":
		objects[5].show(screen)
	pygame.display.flip()
	sleep(0.4)
	enemyChoice=random.randint(0,2)
	print(f"enemyChoice: {enemyChoice}")

	objects[enemyChoice].show(screen)
	pygame.display.flip()
	sleep(0.4)


	if choice=="Rock":
		if enemyChoice==0:
			print("Draw!")
			message="Draw!"

		elif enemyChoice==1:
			print("You lost!")
			message="You lost!"

		elif enemyChoice==2:
			print("You won!")
			message="You won!"

	elif choice=="Paper":
		if enemyChoice==0:
			print("You won")
			message="You won"

		elif enemyChoice==1:
			print("Draw")
			message="Draw!"

		elif enemyChoice==2:
			print("You lost!")
			message="You lost!"

	elif choice=="Scissors":
		if enemyChoice==0:
			print("You lost")
			message="You lost!"

		elif enemyChoice==1:
			print("You win")
			message="You win"

		elif enemyChoice==2:
			print("Draw")
			message="Draw!"
	if message!="Draw":
		displayMessage(message,220,100,font,screen)
	else:
		displayMessage(message,600,100,font,screen)
	pygame.display.flip()
	sleep(0.4)


	
def main():
	global objects,choice,font,screen
	objects=[]
	
	choice=None
	message=""
	width=800
	height=600

	gameRunning=True

	font = pygame.font.SysFont('Arial', 100)
	clock=pygame.time.Clock()
	FPS=60
	screen=pygame.display.set_mode((width,height))
	pygame.display.set_caption("RPS-Remastered")

	pygame.display.flip()

	Rock=Object(int(50+width/2),100,300,300,"Rock")
	Paper=Object(int(50+width/2),100,300,300,"Paper")
	Paper=Object(int(50+width/2),100,300,300,"Scissors")

	rock1=Object(50,100,300,300,"Rock")
	paper1=Object(50,100,300,300,"Paper")
	scissor1=Object(50,100,300,300,"Scissors")

	rockChoice=Button(width/2/3*1-(width/6),500,130,130,"Rock")
	paperChoice=Button(width/2/3*2-(width/6),500,130,130,"Paper")
	scissorsChoice=Button(width/2/3*3-(width/6),500,130,130,"Scissors")


	loadImages(objects)
	rockChoice.load()
	paperChoice.load()
	scissorsChoice.load()




	while gameRunning:
		clock.tick(FPS)

		screen.fill((145,214,107))
		
		setupScreen(screen,width,height)
		

		rockChoice.show(screen)
		paperChoice.show(screen)
		scissorsChoice.show(screen)
		if message!="":
			print(f"Message: {message}")
		pygame.display.flip()
		
	
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameRunning=False
			rockChoice.checkForClick(event,setChoice)
			paperChoice.checkForClick(event,setChoice)
			scissorsChoice.checkForClick(event,setChoice)
			
		if choice !=None:
			game(choice,screen)
		choice =None
		displayMessage(message,300,200,font,screen)

if __name__=="__main__":
	main()
