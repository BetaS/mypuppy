#coding: utf-8

import sys
from optparse import OptionParser
from utils.src.importer import utest, dictutil
import mypuppy.src.rpc.rpcutil as rpcutil
from rpcutil import JSONResult

from mypuppy.src.data.User import User

DEBUG   = 0
PROMPT  = 1
ERROR   = 2

class RPCServer(rpcutil.Event):
    # User RPC
    def userLogin(self, email, passwd):
        result = User.login(email, passwd)
        if len(result) > 0:
            return JSONResult(result="ok", item=result[0])
        else:
            return JSONResult(result="error", code=DEBUG, msg="Can't find User")

    def userAuthenticate(self, authkey):
        result = User.authenticate(authkey)
        if len(result) > 0:
            return JSONResult(result="ok", item=result[0])
        else:
            return JSONResult(result="error", code=DEBUG, msg="Can't find User")

    def userCheckEmail(self, email):
        return JSONResult(result="ok", item={"check": User.check_email_valid(email)})

    def userRegister(self, email, passwd, name, birth, gender):
        id, authkey = User.register(email, passwd, name, birth, gender)
        if id > 0:
            return JSONResult(result="ok", item={"id": id, "authkey": authkey})
        else:
            return JSONResult(result="error", code=PROMPT, msg="Can't Register User")

    # Timeline RPC
    def timelineWrite(self, uid, text, img="", lat=0.0, lng=0.0, meta={}):
        pass
    def timelineDelete(self, uid, timeline_id):
        pass


if __name__ == "__main__":
    usage_str = "%prog [options]\nDescription: RPC Server Daemon."
    parser = OptionParser(usage=usage_str.decode("utf-8"))
    parser.add_option("--port", default="5300", help="port number")
    (options, args) = parser.parse_args()
    rpc = rpcutil.Server(RPCServer, options.port)
    rpc.run()


