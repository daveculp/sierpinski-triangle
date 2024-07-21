#Si ple script that uses a chaos algorithm to plot Sierpienski's triangle
 
import pygame, random, sys, time

def scaleRange(oldMax, oldMin, oldValue, newMax, newMin):
    return(((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin)) + newMin

def restrict(val, minval, maxval):
    if val < minval: return minval
    if val > maxval: return maxval
    return val 
 
 
#change these to suit your screen
SCREEN_WIDTH = 4800
SCREEN_HEIGHT = 3200
 
num_iterations = int(input("How many iterations do you want? "))
 
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill( (0,0,0) )
 
ax = 0
ay = SCREEN_HEIGHT
bx = SCREEN_WIDTH
by = SCREEN_HEIGHT
cx = SCREEN_WIDTH/2
cy = 0
 
px = ax
py = ay
 
print( "Calculating, please wait......\n\n")
start = time.process_time()
for n in range(1, num_iterations+1):
 
    vx = random.randrange(0,3)
    if vx == 0:
        r = 255
        g = scaleRange(0, SCREEN_WIDTH, px, 0,255)
        b = scaleRange(0, SCREEN_HEIGHT, py, 0,255)
        rgb = r,g,b
        px = (px + ax) / 2
        py = (py + ay) / 2
        
    elif vx == 1:
        #rgb = restrict(px,0,255),restrict(py,0,255),255
        b = 255
        g = scaleRange(0, SCREEN_WIDTH, px, 0,255)
        r = scaleRange(0, SCREEN_HEIGHT, py, 0,255)
        rgb = r,g,b
        px = (px + bx) / 2
        py = (py + by) / 2
        
    else:
        #rgb = restrict(px,0,255),255,restrict(py,0,255)
        g = 255
        r = scaleRange(0, SCREEN_WIDTH, px, 0,255)
        b = scaleRange(0, SCREEN_HEIGHT, py, 0,255)
        rgb = r,g,b
        px = (px + cx) / 2
        py = (py + cy) / 2
 
    screen.set_at( (int(px), int(py)), rgb )
    #if n%10000 == 0: sys.stdout.write('.')
    #if n%100000 == 0: print '|'+str(n)+'\n'
end = time.process_time()
pygame.display.update()
pygame.image.save(screen, "sier screenshot.jpeg")
 
print( "\nDone! in ", end-start,"seconds")
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
