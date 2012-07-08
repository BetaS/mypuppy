#coding: utf8

from mypuppy.src.importer import ENTITY_DB

class Timeline:
    @classmethod
    def write_timeline(cls, user_id, content, lat, lng, img_id=0, visiblity=0):
        meta = cls.build_meta(visiblity)
        ENTITY_DB.insert({"user_id": user_id, "content": content, "lat": lat, "lng": lng, "img_id": img_id, "meta": meta}, tb="timeline")


    @classmethod
    def delete_timeline(cls, content_id):
        pass

    @classmethod
    def build_meta(cls, visiblity):
        result = {"visiblity": visiblity}
        return str(result)