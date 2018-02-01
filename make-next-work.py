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

def make_post(screen):
    """Сделать заглушку для вёрстки"""



def do_magic():
    """Сделать все дела~~"""
    makedirs('public/images/screenshots', exist_ok=True)
    makedirs('_posts', exist_ok=True)
    screen = random_screenshot()
    move_screenshot(screen)
    make_post(screen)

if __name__ == '__main__':
    do_magic()
