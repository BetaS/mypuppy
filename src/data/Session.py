__author__ = 'newmoni'

import time, threading

class Session:
    def __init__(self):
        self.sessions = {}
        threading.Thread(target=self.update).run()

    def add(self, user_id, device_id, ip):
        if self.sessions.has_key(device_id):
            return -1
        else:
            self.sessions[device_id] = {
                "user_id": user_id,
                "ip": ip,
                "time": time.time()
            }

        return 0

    def find(self, device_id):
        if self.sessions.has_key(device_id):
            now = time.time()
            session = self.sessions['device_id']
            session["time"] = now+600
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

    def delete(self, device_id):
        del self.sessions[device_id]

