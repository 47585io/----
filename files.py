import pygame.image
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.sprite import Sprite
from animation import Animation

class R:
    pictures_directory = "res/pictures/"
    animation_directory = "res/animation/"
    class pictures:
        class background:
            sky = "pictures/sky.png"
            meadow = "pictures/meadow.png"
            mountain = "pictures/mountain.png"
        
    class animation:
        hero_run = "hero_run.txt"
        hero_jump = "hero_jump.txt"
        hero_down = "hero_down.txt"
#end define

class FileUtils:
    _path_to_image = dict()
    
    @classmethod
    def get_image(cls, path: str) -> Surface:
        path = R.pictures_directory + path 
        image = cls._path_to_image.get(path)
        if(image is None):
            image = pygame.image.load(path)
            cls._path_to_image[path] = image
        return image
    
    @classmethod
    def get_animation(cls, path: str) -> Animation:
        path = R.animation_directory + path
        text = open(path).read()
        frames = list()
        for line in text.splitlines():
            args = line.split(",")
            index = 0;
            while index < len(args):
                args[index] = args[index].strip()
                index += 1
            sprite = Sprite()
            sprite.image = FileUtils.get_image(args[0])
            sprite.rect = Rect(int(args[1]), int(args[2]), int(args[3]), int(args[4]))
            frames.append(sprite)
        return Animation(tuple(frames))
        