#coding: utf-8
from utils.src.importer import dbutil, crawlutil, timeutil, strutil, dictutil
from utils.src.dbutil import DB
from mypuppy.src.data.Session import Session
import atexit
ENTITY_DB   = DB('mypuppy', 'soajdajddl', "127.0.0.1:5432", 'mypuppy', "user", 1)
def _db_exit():
    ENTITY_DB.close()
    print "EXIT OK!"

_SESSION = Session()
global _SESSION

atexit.register(_db_exit)