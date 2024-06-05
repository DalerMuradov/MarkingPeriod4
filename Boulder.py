import pygame

class Boulder:
    def __init__(self, screen):
        self.screen = screen
        self.image_index = 0
        self.images = [
            pygame.image.load("Boulder1.png"),
            pygame.image.load("Boulder2.png"),
        ]
        self.images = [pygame.transform.scale(image, (image.get_width() , image.get_height())) for image in self.images]
        self.rect = self.images[self.image_index].get_rect()
        self.rect.bottomleft = (0, screen.get_height())
        self.move_boulder = False
        self.image_change_delay = 10
        self.delay_counter = 0

    def update(self):
        if self.move_boulder:
            self.rect.move_ip(1, -1)
            if self.rect.top <= 0 and self.rect.right >= self.screen.get_width()+120:
                self.rect.bottomleft = (0, self.screen.get_height())
                return True
        return False

    def draw(self):
        self.screen.blit(self.images[self.image_index], self.rect)

    def startMoving(self):
        self.move_boulder = True

    def stopMoving(self):
        self.move_boulder = False

    def cycleImages(self):
        if self.delay_counter <= 0 and self.move_boulder:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.rect = self.images[self.image_index].get_rect(center=self.rect.center)
            self.delay_counter = self.image_change_delay
        elif self.move_boulder:
            self.delay_counter -= 1
