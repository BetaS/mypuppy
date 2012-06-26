#coding: utf-8

from mypuppy.src.importer import ENTITY_DB
import hashlib as hashlib

class User:

    @classmethod
    def register(cls, email, passwd, name, birth, gender):
        authkey = hashlib.sha256(email+"+"+passwd).digest()
        ENTITY_DB.insert({"email": email, "passwd": passwd, "authkey": authkey, "name": name, "gender": gender, "birth": birth}, tb="user")

        return ENTITY_DB.get_id({"email": email}, tb="user"), authkey

    @classmethod
    def check_email_valid(cls, email):
        if ENTITY_DB.get_id(where={"email": email}, tb="user") == 0:
            return True
        else:
            return False

    @classmethod
    def login(cls, authkey):
        return ENTITY_DB.select_dict(['id', 'name'], {"authkey": authkey}, tb="user")

    @classmethod
    def authenticate(cls, email, passwd):
        return ENTITY_DB.get_id(where={"email": email, "passwd": passwd}, field="authkey", tb="user")


