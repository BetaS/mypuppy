#coding: utf8

from mypuppy.src.importer import ENTITY_DB

SHARE_PRIVATE, SHARE_FRIENDS, SHARE_GROUPS, SHARE_ALL = range(4)

class Timeline:

    def __init__(self, id=-1):
        self.id = id
        self.owner = -1
        self.content = ""
        self.loc = {"addr": "null","lat": 0.0, "lng": 0.0}
        self.share = SHARE_ALL
        self.dist = 500
        self.replys = []
        self.likes = []

        if id >= 0:
            #Load from DB
            pass

    def set_contents(self, contents):
        self.content = contents

    def set_location(self, address, latitude, longitude):
        self.loc = {"addr": address, "lat": latitude, "lng": longitude}

    def set_distance(self, dist):
        self.dist = dist

    def set_share_private(self):
        self.set_share(SHARE_PRIVATE)
    def set_share_friends(self):
        self.set_share(SHARE_FRIENDS)
    def set_share_groups(self):
        self.set_share(SHARE_GROUPS)
    def set_share_all(self):
        self.set_share(SHARE_ALL)
    def set_share(self, share):
        self.share = share

    def save(self):
        #Save to DB
        pass

    @classmethod
    def write_timeline(cls, user_id, content, lat, lng, img_id=0, visiblity=0):
        meta = cls.build_meta(visiblity)
        ENTITY_DB.insert({"user_id": user_id, "content": content, "lat": lat, "lng": lng, "img_id": img_id, "meta": meta}, tb="timeline")

    @classmethod
    def edit_timeline(cls, asd):
        pass

    @classmethod
    def delete_timeline(cls, content_id):
        pass

    @classmethod
    def build_meta(cls, visiblity):
        result = {"visiblity": visiblity}
        return str(result)