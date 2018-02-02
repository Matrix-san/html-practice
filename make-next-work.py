#!/usr/bin/env python3

from glob import glob
from random import choice
from shutil import move
from os import makedirs
from os.path import basename
from datetime import datetime

SOURCE_DIRECTORY = "_todo"

def today():
    """Вернуть сегодняшнюю дату"""
    return datetime.now().strftime('%F')

def screenshots():
    """Вернуть список сделанных скриншотов"""
    return glob(SOURCE_DIRECTORY+'/*.jpg') + glob(SOURCE_DIRECTORY+'/*.png')

def random_screenshot():
    """Получить случайный скриншот"""
    return choice(screenshots())

def move_screenshot(screen):
    """Перенести скриншот на постоянное место"""
    move(screen, 'public/images/screenshots/'+basename(screen))

def screen_to_slug(screen):
    """Получить название из пути"""
    return basename(screen).replace('.jpg', '').replace('.png', '')


def template_for(screen):
    """Получить шаблон заглушки для скрина"""
    tpl = ("---\n"
           "layout: work\nscreenshot: {file} \n"
           "---\n\n"
           "<style>\n.{name} {{ \n    border: 1px solid red;\n}}\n</style>\n\n\n"
           "<div class='{name}'>\n    Change Me\n</div>")

    return tpl.format(name=screen_to_slug(screen), file=basename(screen))

def filename(name):
    """Вернуть имя файла для поста"""
    return '_posts/{}-{}.html'.format(today(), name)

def make_post(screen):
    """Сделать заглушку для вёрстки"""
    name = screen_to_slug(screen)
    body = template_for(screen)
    open(filename(name), 'w').write(body)


def do_magic():
    """Сделать все дела~~"""
    makedirs('public/images/screenshots', exist_ok=True)
    makedirs('_posts', exist_ok=True)
    screen = random_screenshot()
    move_screenshot(screen)
    make_post(screen)

if __name__ == '__main__':
    do_magic()
