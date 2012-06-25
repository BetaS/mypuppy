#coding: utf-8

import sys
from optparse import OptionParser
from utils.src.importer import rpcutil, utest, dictutil

class RPCServer(rpcutil.Event):
    # User RPC
    def user_login(self):
        pass

if __name__ == "__main__":
    usage_str = "%prog [options]\nDescription: RPC Server Daemon."
    parser = OptionParser(usage=usage_str.decode("utf-8"))
    parser.add_option("--port", default="5300", help="port number")
    (options, args) = parser.parse_args()
    rpc = rpcutil.Server(RPCServer, options.port)
    rpc.run()


