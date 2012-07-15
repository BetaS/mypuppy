__author__ = 'newmoni'

import hashlib
import time, threading

SESSION_EXPIRED_TIME = 600

class Session:
    def __init__(self):
        self.sessions = {}
        threading.Thread(target=self.update).run()

    @staticmethod
    def _get_session():
        return hashlib.sha256(str(time.time())).hexdigest()

    def add(self, user_id, device_id):
        now = time.time()
        key = Session._get_session()

        self.sessions[key] = {
            "user_id": user_id,
            "device_id": device_id,
            "time": now,
            "expired_time": now + SESSION_EXPIRED_TIME
        }

        return key

    def find(self, key):
        if self.sessions.has_key(key):
            now = time.time()

            session = self.sessions[key]

            session["expired_time"] = now + SESSION_EXPIRED_TIME
            return session['user_id']
        else:
            return -1

    def show(self, device_id=""):
        if device_id == "":
            print device_id,":",self.sessions[device_id]
        else:
            for k, v in self.sessions:
                print k,":",v

    def update(self):
        while True:
            now = time.time()

            for k, v in self.sessions:
                if (now-self.sessions[k]['time']) <= 0:
                    self.delete(k)

            time.sleep(30)

    def size(self):
        return len(self.sessions)

    def clear(self):
        self.sessions = {}

    def delete(self, key):
        del self.sessions[key]

