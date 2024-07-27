from pygame.rect import Rect
from pygame.sprite import AbstractGroup, DirtySprite
from pygame.surface import Surface
from pygame.event import Event
from animation import Animation
from files import *

class Obstacle(DirtySprite):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.active_animation = None
    
    def start_animation(self, animation: Animation):
        animation.restart()
        self.active_animation = animation
    
    def update(self):
        super().update()
        if self.active_animation:
            self.active_animation.update()
            sprite = self.active_animation.get_current_frame()
            self.image = sprite.image
            self.rect.width = sprite.rect.width
            self.rect.height = sprite.rect.height
            self.source_rect = sprite.rect
    
    def collision(self, other: 'Obstacle'):
        pass
    
    def handle_event(self, event: Event) -> bool:
        return False
    
class Hero(Obstacle):
    def __init__(self) -> None:
        super().__init__()
        self.active_animation = FileUtils.get_animation(R.animation.hero_run)