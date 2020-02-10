import pygame, random

pygame.init()
clock = pygame.time.Clock()
WIDTH,HEIGHT = (500,500)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

class Snake:
        x = 100
        y = 100
        x_vel = 0
        y_vel = 0
        body = []
        score = 0
        def snake_move(self):                
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                        if self.x_vel == -20 and len(self.body) > 1:
                                                pass
                                        else:
                                                self.x_vel = 20
                                                self.y_vel = 0
                                                
                                if event.key == pygame.K_LEFT:
                                        if self.x_vel == 20 and len(self.body) > 1:
                                                pass
                                        else:
                                                self.x_vel = -20
                                                self.y_vel = 0
                                if event.key == pygame.K_DOWN:
                                        if self.y_vel == -20 and len(self.body) > 1:
                                                pass
                                        else:
                                                self.x_vel = 0
                                                self.y_vel = 20
                                if event.key == pygame.K_UP:
                                        if self.y_vel == 20 and len(self.body) > 1:
                                                pass
                                        else:
                                                self.x_vel = 0
                                                self.y_vel = -20

                self.x += self.x_vel
                self.y += self.y_vel

                

        def snake_display(self):
                xy = []
                xy.insert(0,self.x)
                xy.insert(1,self.y)
                self.body.insert(0,xy)
                del self.body[self.score+1:]
                for xny in self.body:
                        pygame.draw.rect(screen,GREEN,[xny[0],xny[1],20,20])  
                                
        def snake_colision(self):                
                if self.x < 0 or self.x > WIDTH-20 or self.y < 0 or self.y > HEIGHT-20:
                        return True
                for idx,xny in enumerate(self.body):
                        if self.x == xny[0] and self.y == xny[1] and idx > 0:
                                return True
                                        
                
class Apple:

        x = 200
        y = 200              
        def apple_spawn(self,other):
                if self.x == other.x and self.y == other.y:
                        self.x = random.randrange(0,WIDTH-20,20)
                        self.y = random.randrange(0,HEIGHT-20,20)
                        other.score += 1
                pygame.draw.rect(screen,RED,[self.x,self.y,20,20])
                
                
def game_over(player):
        print ("Your score was",player.score)
        main()

def quit():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
        
def main():
        global player
        pygame.display.set_caption("SNAAAAAAKE")
        player = Snake()
        apple = Apple()
        
        while True:
                quit()

                clock.tick(4+player.score)
                screen.fill((12,35,64))
                
                player.snake_move()
                player.snake_display()
                done = player.snake_colision()
                if done == True:
                        game_over(player)
                apple.apple_spawn(player)
                pygame.display.update()

if __name__ == "__main__":
        main()
