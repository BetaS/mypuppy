__author__ = 'newmoni'

import utils.src.timeutil as timeutil

class Session:
    def __init__(self):
        self.sessions = {}

    def add(self, user_id, device_id, ip):
        if self.sessions.has_key(device_id):
            return -1
        else:
            self.sessions[device_id] = {
                "user_id": user_id,
                "ip": ip,
                "time": timeutil.now()
            }

        return 0

    def find(self, device_id):
        if self.sessions.has_key(device_id):
            now = timeutil.now()
            session = self.sessions['device_id']
            if session["time"]+30:
                return session['user_id']
        else:
            return -1

    def delete(self, device_id):
        pass

