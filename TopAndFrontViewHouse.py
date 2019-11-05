import pygame


black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)

# rect = (marginLeft , marginTop , breadth , length)

rect = [(300,300,500,200),(304,304,492,192),(400,150,380,150),(730,110,30,40),(720,100,50,10),(510,430,80,70)]

rectx = [(360,380,100,50),(640,380,100,50),(358,378,104,54),(638,378,105,54)]

topView = [(300,520,500,250),(400,600,380,150),(720,680,50,50),(730,690,30,30)]

dk1 = (570,465) #DoorKnob

wl1 = (360,405) #WindowPanes1
wl2 = (460,405) #WindowPanes1


wl3 = (410,380) #WindowPanes1
wl4 = (410,430) #WindowPanes1


wl5 = (640,405) #WindowPanes2
wl6 = (740,405) #WindoePanes2


wl7 = (690,380) #WindowPanes2
wl8 = (690,430) #WindoePanes2

pt1 = (400,150) #Initial Point for left side
pt2 = (380,180) #End Point for left side

pt3 = (780,150) #Initial Point for right side
pt4 =  (800,180) #End Point for right side

joinPt1 = (380,180) #Joining line
joinPt2 = (800,180) #Joining line

cp1 = (440,225)
cp2 = (740,225)

cpx1 = (740,205) #Circular Window Pane 2
cpx2 = (740,245) #Circular Window Pane 2

cpx3 = (720,225) #Circular Window Pane 2
cpx4 = (760,225) #Circular Window Pane 2

cpy1 = (440,205) #Circular Window Pane 2
cpy2 = (440,245) #Circular Window Pane 2

cpy3 = (420,225) #Circular Window Pane 2
cpy4 = (460,225) #Circular Window Pane 2

size = [1000, 1000]
screen = pygame.display.set_mode(size)

screen.fill(black)

def house():
	for i in range(0,6):
		pygame.draw.rect(screen,red,rect[i],2)
	for i in range(0,4):
		pygame.draw.rect(screen,white,rectx[i],1)
	pygame.draw.line(screen,red,pt1,pt2,2)
	pygame.draw.line(screen,red,pt3,pt4,2)
	pygame.draw.line(screen,red,joinPt1,joinPt2,2)
	pygame.draw.line(screen,white,wl1,wl2,2) #WindowPane
	pygame.draw.line(screen,white,wl3,wl4,2) #WindowPane
	pygame.draw.line(screen,white,wl5,wl6,2) #WindowPane
	pygame.draw.line(screen,white,wl7,wl8,2) #WindowPane
	pygame.draw.circle(screen,white,cp1,20) #Circular Window1
	pygame.draw.circle(screen,white,cp2,20) #Circular Window2
	pygame.draw.line(screen,black,cpx1,cpx2,2) #Circular Window Pane
	pygame.draw.line(screen,black,cpx3,cpx4,2) #Circular Window Pane
	pygame.draw.line(screen,black,cpy1,cpy2,2) #Circular Window Pane
	pygame.draw.line(screen,black,cpy3,cpy4,2) #Circular Window Pane
	pygame.draw.circle(screen,white,dk1,3) #Circular Window2
	for i in range(0,4):
		pygame.draw.rect(screen,red,topView[i],2)

pygame.init()
house()

done = False

while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()

	pygame.display.update()