from pygame.sprite import Sprite
from pygame.surface import Surface
from animation import Animation

class Obstacle:
    def __init__(self) -> None:
        self.current_sprite = Sprite()
        self.active_animation = None
    
    def start_animation(self, animation: Animation) -> None:
        self.active_animation = animation
    
    def get_sprite(self) -> Sprite:
        return self.current_sprite
    
    def update(self):
        pass
    
    def draw(self, scenes: Surface) -> None:
        if self.active_animation:
            self.active_animation.update()
            sprite = self.active_animation.get_current_frame()
            self.current_sprite.image = sprite.image
            self.current_sprite.rect.width = sprite.rect.width
            self.current_sprite.rect.height = sprite.rect.width
            scenes.blit(sprite.image, self.current_sprite, sprite)