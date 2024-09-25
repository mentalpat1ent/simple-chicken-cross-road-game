import pygame

import sys


class game:
    
    def __init__(self):
        
        pygame.init()

        pygame.display.set_caption('cross road')

        self.var = True
        
        self.screen = pygame.display.set_mode((800, 500))
        
        
        self.end = pygame.image.load('images/cross road.png')
        self.end = pygame.transform.scale(self.end, (800, 500))

        self.clock = pygame.time.Clock()
        
        self.rand = False

        self.img = pygame.image.load('images/background.png')
        self.img = pygame.transform.scale(self.img, (800, 500))

        self.chicken = pygame.image.load('images/chicken.png')

        self.car_1 = pygame.image.load('images/Car.png')
        self.car_2 = pygame.image.load('images/Black_viper.png')
        self.car_3 = pygame.image.load('images/Mini_truck.png')
        self.car_4 = pygame.image.load('images/taxi.png')
        self.car_5 = pygame.image.load('images/Police.png')
        self.car_6 = pygame.image.load('images/Audi.png')
        self.car_7 = pygame.image.load('images/truck.png')


        self.car_1 = pygame.transform.scale(self.car_1, (53, 103))
        self.car_2 = pygame.transform.scale(self.car_2, (53, 103))
        self.car_3 = pygame.transform.scale(self.car_3, (53, 103))
        self.car_4 = pygame.transform.scale(self.car_4, (53, 103))
        self.car_5 = pygame.transform.scale(self.car_5, (53, 123))
        self.car_6 = pygame.transform.scale(self.car_6, (53, 103))
        self.car_7 = pygame.transform.scale(self.car_7, (63, 133))
        self.chicken = pygame.transform.scale(self.chicken, (40, 40))

        self.rect_1 = self.chicken.get_rect()
        self.rect_2 = self.car_1.get_rect()
        self.rect_3 = self.car_2.get_rect()
        self.rect_4 = self.car_3.get_rect()
        self.rect_5 = self.car_4.get_rect()
        self.rect_6 = self.car_5.get_rect()
        self.rect_7 = self.car_6.get_rect()
        self.rect_8 = self.car_7.get_rect()

        self.rect_1.topleft = (50, 200)
        self.rect_2.topleft = (200, 100)
        self.rect_3.topleft = (320, 350)
        self.rect_4.topleft = (440, 100)
        self.rect_5.topleft = (550, 50)
        self.rect_6.topleft = (320, 100)
        self.rect_7.topleft = (200, 400)
        self.rect_8.topleft = (550, 300)
        

    def run(self):
        while True:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.rect_1.y -= 30
                    if event.key == pygame.K_s:
                        self.rect_1.y += 30
                    if event.key == pygame.K_d:
                        self.rect_1.x += 30
                    if event.key == pygame.K_a:
                        self.rect_1.x -= 30
                    if event.key == pygame.K_x:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        self.rect_1.topleft = (50, 100)
                        self.var = True
                        
            if self.var:
                self.screen.blit(self.img, (0, 0))            
                self.screen.blit(self.car_1, self.rect_2)
                self.screen.blit(self.car_2, self.rect_3)
                self.screen.blit(self.car_3, self.rect_4)
                self.screen.blit(self.car_4, self.rect_5)
                self.screen.blit(self.car_5, self.rect_6)
                self.screen.blit(self.car_6, self.rect_7)
                self.screen.blit(self.car_7, self.rect_8)
                self.screen.blit(self.chicken, self.rect_1)
                
                self.rect_2.y -= 3
                self.rect_3.y -= 2
                self.rect_4.y += 3
                self.rect_5.y += 2
                self.rect_6.y -= 2
                self.rect_7.y -= 3
                self.rect_8.y +=2
                
                if self.rect_2.y <= -100:
                    self.rect_2.y = 600
                if self.rect_3.y <= -100:
                    self.rect_3.y = 600
                if self.rect_4.y >= 600:
                    self.rect_4.y = -100
                if self.rect_5.y >= 600:
                    self.rect_5.y = -100
                if self.rect_6.y <= -100:
                    self.rect_6.y = 600
                if self.rect_7.y <= -100:
                    self.rect_7.y = 600
                if self.rect_8.y >= 600:
                    self.rect_8.y = -100

                if self.rect_1.colliderect(self.rect_2):
                    self.var = False
                if self.rect_1.colliderect(self.rect_3):
                    self.var = False
                if self.rect_1.colliderect(self.rect_4):
                    self.var = False
                if self.rect_1.colliderect(self.rect_5):
                    self.var = False
                if self.rect_1.colliderect(self.rect_6):
                    self.var = False
                if self.rect_1.colliderect(self.rect_7):
                    self.var = False
                if self.rect_1.colliderect(self.rect_8):
                    self.var = False
                    
                    
            else:
                self.screen.blit(self.end, (0, 0))
                if self.rand:
                    self.var = True
                              
                        
                        
            pygame.display.update()
            self.clock.tick(60)
        
game().run()            
            