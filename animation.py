from typing import Tuple
from pygame.sprite import Sprite

class AnimationListener:
    def on_animation_start():
        pass
    def on_animation_update():
        pass
    def on_animation_end():
        pass

class Animation:
    def __init__(self, frames: Tuple[Sprite]) -> None:
        self.key_frames = frames
        self.frame_duration = 10
        self.delta = 0;
        self.animation_listener = None
        
    def get_current_frame(self) -> Sprite:
        total = len(self.key_frames) * self.frame_duration
        current_index = (self.delta % total) // self.frame_duration
        return self.key_frames[current_index]
    
    
    
    def set_animation_listener(self, listener: AnimationListener):
        self.mAnimationListener = listener
    
    def update(self):
        self.delta += 1;
        
