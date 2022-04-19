# install libary pygame terlebih dahulu
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install','pygame'])

from pygame import gfxdraw
import sys,pygame
pygame.init()

# ukuran screen
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.flip()

# fungsi lingkaran
def circle(radius,offset):
	x,y = 20,radius
	plotCircle(x,y,radius,offset)

# fungsi titik simerti
def symmetry_points(x,y,offset):
	gfxdraw.pixel(screen,x+offset,y+offset,(255,255,255))
	gfxdraw.pixel(screen,-x+offset,y+offset,(255,255,255))
	gfxdraw.pixel(screen,x+offset,-y+offset,(255,255,255))
	gfxdraw.pixel(screen,-x+offset,-y+offset,(255,255,255))
	gfxdraw.pixel(screen,y+offset,x+offset,(255,255,255))
	gfxdraw.pixel(screen,-y+offset,x+offset,(255,255,255))
	gfxdraw.pixel(screen,y+offset,-x+offset,(255,255,255))
	gfxdraw.pixel(screen,-y+offset,-x+offset,(255,255,255))
	pygame.display.flip()

# fungsi plot circle
def plotCircle(x,y,radius,offset):
	d = 5/4.0 - radius
	symmetry_points(x,y,radius+offset)
	while x < y:
		if d < 0:
			x += 1
			d += 2*x + 1
		else:
			x += 1
			y -= 1
			d += 2*(x-y) + 1
		symmetry_points(x,y,radius+offset)

circle(100,25) # circle(radius,<offset from edge>)
pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()