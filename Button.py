import pygame

class Button:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)
        self.alpha = 255
        self.fade_speed = 2  # Adjust the fade speed as needed
        self.fade_direction = 1  # 1 for fading in, -1 for fading out

    def draw(self, screen):
        temp_img = self.image.copy()
        temp_img.fill((255, 255, 255, self.alpha), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(temp_img, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
        return False

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        if self.is_hovered():
            self.alpha = max(self.alpha - self.fade_speed, 100)
        else:
            self.alpha = min(self.alpha + self.fade_speed, 255)

        # For other buttons, reset alpha to 255 if not hovered
        if not isinstance(self, CurrentlyPlayingButton) and not self.is_hovered():
            self.alpha = 255

class CurrentlyPlayingButton(Button):
    def __init__(self, image_path, position, size, alt_image_path=None, alt_position=None):
        super().__init__(image_path, position)
        self.size = size
        self.image = pygame.transform.scale(self.image, size)
        self.alt_image_path = alt_image_path
        self.alt_position = alt_position
        self.alt_image = pygame.image.load(alt_image_path) if alt_image_path else None
        self.fade_speed = 2
        self.fade_direction = 1
 #GPT generated
    def update(self):
        self.alpha += self.fade_direction * self.fade_speed
        if self.alpha > 255:
            self.alpha = 255
            self.fade_direction = -1
        elif self.alpha < 0:
            self.alpha = 0
            self.fade_direction = 1

    def draw(self, screen):
        temp_img = self.image.copy()
        temp_img.fill((255, 255, 255, self.alpha), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(temp_img, self.rect)

    def update_alt_image(self, alt_image_path, alt_position):
        if alt_image_path and alt_position:
            self.image = pygame.image.load(alt_image_path)
            self.image = pygame.transform.scale(self.image, self.size)
            self.rect = self.image.get_rect(center=alt_position)