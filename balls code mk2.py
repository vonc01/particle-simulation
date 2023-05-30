import pygame
import random
#import numpy as np
import math



        
def checkcirclecollide(x1, y1, r1, x2, y2, r2):
    distX = x1 - x2
    distY = y1 - y2
    distance = math.sqrt( (distX * distX) + (distY * distY) )

    return (distance <= (r1 + r2))    

def ballcollision(m1, m2, v1, v2):
    v2f = (2*m1*v1 + m2*v2 - m1*v2) / (m1+m2)
    v1f = (m1*v1 + m2*v2 - m2*v2f)/m1
    return v1f, v2f

def inelasticCollision(m1, m2, v1, v2):
    vf = ((v1*m1)+v2*m2)/(m1+m2)
    return vf

def seperate_balls(ball, other):
    angle = -math.atan2(ball.y - other.y, ball.x - other.x)
    
    distX = ball.x - other.y
    distY = ball.y - other.y
    distance = math.sqrt((distX * distX) + (distY * distY))
    diffR = ball.r + other.r - distance                      
    
    diffR *= 0.5
    
    ball.x += math.cos(angle) * diffR
    ball.y += math.sin(angle) * diffR
    
    other.x -= math.cos(angle) * diffR
    other.y -= math.sin(angle) * diffR
    

class Ball:
    def __init__(self, x, y, vx, vy, r, m, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.m = m

        self.color = color
        
    def change_attribute(self, x=None, y=None, vx=None, vy=None, r=None, m=None):
        if x!=None: self.x = x
        if y!=None: self.y = y
        if vx!=None: self.vx = vx
        if vy!=None: self.vy = vy
        if r!=None: self.r = r
        if m!=None: self.m = m        

        
pygame.init()
screen = pygame.display.set_mode((750, 750))

x, y = random.randint(15, 715), random.randint(15, 715)
vx, vy = random.randint(-5,5), random.randint(-5,5)

animationTimer = pygame.time.Clock()
balls = []
num_balls = 200

for x in range(num_balls):
    balls.append(Ball(random.randint(15, 715), random.randint(15, 715), random.randint(-5, 5), random.randint(-5, 5), 5, 10, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            break

    for ball in balls:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.r)
        
        if (ball.x <= 0) or (ball.x >= 750):
            ball.change_attribute(vx = -ball.vx)

                  
            
        if (ball.y <= 0) or (ball.y >= 750):
            ball.change_attribute(vy = -ball.vy)
            

        """for other in balls:
            if other != ball and checkcirclecollide(ball.x, ball.y, ball.r, other.x, other.y, other.r):
                
                
                #probability = random.randint(1, 5)
                #radius = 1
                if(probability == 1):
                    x = ball.x
                    y= ball.y
                    m1 = ball.m
                    m2 = other.m
                    v1x = ball.vx
                    v1y = ball.vy
                    v2x = other.vx
                    v2y = other.vy
                    radius = other.r + radius
                    balls.remove(sent)
                    balls.remove(other)
                    vfx = inelasticCollision(m1, m2, v1x, v2x)
                    vfy = inelasticCollision(m1, m2, v1y, v2y)
                    balls.append(Ball(x, y, vfx, vfy, radius, (m1+m2), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
                    
                    
                else:
                    new_v1x, new_v2x = ballcollision(ball.m, other.m, ball.vx, other.vx)
                    new_v1y, new_v2y = ballcollision(ball.m, other.m, ball.vy, other.vy)
                    ball.change_attribute(vx = new_v1x, vy = new_v1y)
                    other.change_attribute(vx = new_v2x, vy = new_v2y)"""
                    
                
        for other in balls:
                if other != ball and checkcirclecollide(ball.x, ball.y, ball.r, other.x, other.y, other.r):
                    new_v1x, new_v2x = ballcollision(ball.m, other.m, ball.vx, other.vx)
                    new_v1y, new_v2y = ballcollision(ball.m, other.m, ball.vy, other.vy)
                    ball.change_attribute(vx = new_v1x, vy = new_v1y)
                    other.change_attribute(vx = new_v2x, vy = new_v2y)
                    
                
        ball.change_attribute(x = ball.x+ball.vx, y = ball.y+ball.vy)
    animationTimer.tick(100)
    pygame.display.update()
    screen.fill((0, 0, 0))        