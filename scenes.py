
from pygame import sprite
from pygame.sprite import LayeredDirty
from pygame.surface import Surface
from pygame.event import Event
from pygame.surface import Surface
from obstacle import *

class CollisionCallback:
    def collision(o1: Sprite, o2: Sprite) -> bool:
        return False

class Scenes:
    def __init__(self, rect: Rect) -> None:
        self.rect = rect
        self.surface = Surface(rect.width, rect.height)
        self.obstacle_group = LayeredDirty()
        self.active_hero = Hero()
        self.collisioncallback = None
        
    def set_collisioncallback(self, callback: CollisionCallback):
        self.collisioncallback = callback
        
    def update(self):
        self.active_hero.update()
        self.obstacle_group.update()
    
    def __check_collisiom(self):
        if self.collisioncallback:
            collided_obstacles = sprite.spritecollide(self.active_hero, self.obstacle_group)
            for obstacle in collided_obstacles:
                self.collisioncallback.collision(self.active_hero, obstacle)
    
    def render(self, screen: Surface):
        image = FileUtils.get_image("background.png")
        self.surface.blit(image)
        self.obstacle_group.draw(self.surface)
        hero = self.active_hero
        self.surface.blit(hero.image, hero.rect, hero.source_rect)
        screen.blit(self.surface, self.rect)
    
    def dispatch_event(self, event:Event):
        if event == pygame.MOUSEBUTTONDOWN:
            o = self.obstacle_group.get_sprites_at(event.pos)
            
        