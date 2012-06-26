#coding:utf8
"""
json rpc 를 간소화 해주는 유틸입니다. 
"""
import jsonrpc

__author__ = "peter"
__date__ = "2012/04/02"

from twisted.web import server
from twisted.internet import reactor
from time import time
import utils.src.timeutil as timeutil 
import utils.src.strutil as strutil

from jsonrpc.server import ServerEvents, JSON_RPC
from jsonrpc.proxy import JSONRPCProxy
import socket

class JSONResult:
    def __init__(self, result="ok", code=0, msg="", item=[]):
        self.result = result
        self.code = code
        self.msg = msg

        if type(item) == list:
            self.len = len(item)
            self.items = item
        else:
            self.len = 1
            self.items = item

    def __str__(self):
        result = {
            "result": self.result,
            "code": self.code,
            "time": timeutil.now(),
            "msg": self.msg,
            "length": self.len,
            "items": self.items
        }

        return str(result)

class Event(ServerEvents):
    def findmethod(self, method, args=None, kwargs=None):
        return getattr(self, method)
    
    def callmethod(self, txrequest, rpcrequest, **extra):
        s_time = time()
        rpcrequest.kwargs = strutil.utf8(rpcrequest.kwargs)
        try:
            result = ServerEvents.callmethod(self, txrequest, rpcrequest, **extra)
        except:
            print "ERROR:\t", rpcrequest.method, "\t", rpcrequest.kwargs
            strutil.trace_msg() # 에러 메세지 출력
            return None

        if rpcrequest.method != "is_jsonrpc_alive":
            timeutil.end(s_time, rpcrequest.kwargs, rpcrequest.method)

        return str(result)
    
    def is_jsonrpc_alive(self):
        """ 클라에서 json rpc서버가 살아 있는지 체크 하기 위한 더미 함수""" 
        pass

class Client(JSONRPCProxy):
    def is_alive(self):
        """ josnrpc server 의 is_jsonrpc_alive함수를 콜해봐서 jsonrpc서버가 살아있는지 여부 판단한다.
        """
        try:
            self.call("is_jsonrpc_alive")
            return True
        except:
            return False

class Server:
    """ @summary: json rpc 서버
    """
    def __init__(self, event, port):
        self.port = int(port)
        root = JSON_RPC().customize(event)
        site = server.Site(root)
        reactor.listenTCP(self.port, site)
        self.name = self._name(event)
    
    def _name(self, event):
        name = str(event).replace("<class '__main__.", "").replace("'>", "")
        return name
    
    def run(self):
        print "[+] Start " + self.name + " ", self.port
        reactor.run()

_RPC = ""

def set_rpc(rpc_dict):
    global _RPC
    rpc = rpc_dict["default"]
    host = socket.gethostname()
    if host in rpc_dict:
        rpc = rpc_dict[host]
    _RPC = Client(rpc)

def func(method, req, rpc="", more={}):
    if more:
        req.update(more)
    if rpc:
        return getattr(rpc, method)(**req)
    else:
        return getattr(_RPC, method)(**req)

def get(loc_dict, more={}):
    """ locals()에서 self제거 하고 more가 있으면 합쳐서 리턴하는 함수. rpc 함수에서 주로 사용.
    """
    if "self" in loc_dict:
        loc_dict.pop("self")
    loc_dict.update(more)
    return loc_dict

# 임시코드, 앞으로 삭제 예정임
import xmlrpclib
def get_ip_rpc(url):
    return xmlrpclib.Server(url)

