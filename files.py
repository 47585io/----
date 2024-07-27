import pygame.image
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.sprite import Sprite
from animation import Animation
from typing import Tuple, Dict

class R:
    pictures_directory = "res/pictures/"
    animation_directory = "res/animation/"
    class pictures:
        class background:
            sky = "pictures/sky.png"
            meadow = "pictures/meadow.png"
            mountain = "pictures/mountain.png"
        hero_run = "hero_run.png"
        hero_jump = "hero_jump.png"
        hero_down = "hero_down.png"
        
    class animation:
        hero_run = "hero_run.txt"
        hero_jump = "hero_jump.txt"
        hero_down = "hero_down.txt"
#end define

class FileUtils:
    __path_to_data:Dict[str, object] = dict()
    
    @classmethod
    def get_image(cls, path: str) -> Surface:
        path = R.pictures_directory + path 
        image = cls.__path_to_data.get(path)
        if(image is None):
            image = pygame.image.load(path)
            cls.__path_to_data[path] = image
        return image
    
    @classmethod
    def get_animation(cls, path: str) -> Animation:
        path = R.animation_directory + path
        frames = cls.__path_to_data.get(path)
        if(frames is None):
            frames = cls.creat_frames(path)
            cls.__path_to_data[path] = frames
        return Animation(frames)
    
    @classmethod
    def creat_frames(cls, path: str) -> Tuple[Sprite]:
        text = open(path).read()
        frames = list()
        for line in text.splitlines():
            args = line.split(",")
            index = 0;
            while index < len(args):
                args[index] = args[index].strip()
                index += 1
            sprite = Sprite()
            sprite.image = cls.get_image(args[0])
            sprite.rect = Rect(int(args[1]), int(args[2]), int(args[3]), int(args[4]))
            frames.append(sprite)
        return tuple(frames)