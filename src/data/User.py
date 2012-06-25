#coding: utf-8

from mypuppy.src.importer import ENTITY_DB

class User:
    def __init__(self):
        ENTITY_DB.set_tb('user')


