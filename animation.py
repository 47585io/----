from typing import Tuple
from pygame.sprite import Sprite

class AnimationListener:
    def animation_start():
        pass
    def animation_update():
        pass
    def animation_end():
        pass

class Animation:
    def __init__(self, frames: Tuple[Sprite]) -> None:
        self.keyframes = frames
        self.frame_duration = 10
        self.delta = 0;
        self.animationlistener = None
        
    def get_current_frame(self) -> Sprite:
        total = len(self.keyframes) * self.frame_duration
        current_index = (self.delta % total) // self.frame_duration
        return self.keyframes[current_index]
    
    def get_frame_count(self) -> int:
        return len(self.keyframes)
    
    def get_frame_at(self, index: int) -> Sprite:
        return self.keyframes[index]
    
    def get_animation_duration(self) -> int:
        return self.get_frame_count() * self.frame_duration
    
    def set_animationlistener(self, listener: AnimationListener) -> None:
        self.animationlistener = listener
    
    def restart(self) -> None:
        self.delta = 0
    
    def update(self) -> None:
        self.delta += 1;
        if self.animationlistener:
            if self.delta % self.frame_duration == 0:
                self.animationlistener.animation_update()
            if self.delta % self.get_animation_duration() == 0:
                self.animationlistener.animation_end()