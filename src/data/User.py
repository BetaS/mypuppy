#coding: utf8

from mypuppy.src.importer import _SESSION, ENTITY_DB
import hashlib as hashlib

class User:
    @classmethod
    def register(cls, email, passwd, name, birth, gender):
        passwd = hashlib.md5(passwd).hexdigest()
        authkey = hashlib.sha256(email+"+"+passwd).hexdigest()
        ENTITY_DB.insert({"email": email, "passwd": passwd, "authkey": authkey, "name": name, "gender": gender, "birth": birth}, tb="user")

        return ENTITY_DB.get_id({"email": email}, tb="user"), authkey

    @classmethod
    def check_email_valid(cls, email):
        if ENTITY_DB.get_id(where={"email": email}, tb="user") == 0:
            return True
        else:
            return False

    @classmethod
    def authenticate(cls, authkey):
        return ENTITY_DB.select_dict(['id', 'name'], {"authkey": authkey}, tb="user")

    @classmethod
    def login(cls, email, passwd):
        passwd = hashlib.md5(passwd).hexdigest()
        return ENTITY_DB.select_dict(['id', 'authkey', 'name'], {"email": email, "passwd": passwd}, tb="user")


