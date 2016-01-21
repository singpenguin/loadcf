#-*- coding:utf-8 -*-


import json
import sys

_this = sys.modules[__name__]

class Storage(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return '<storage %s >' % dict.__repr__(self)

def load(path):
    with open(path, "rb") as f:
        cont = f.read()
        if type(cont) == bytes:
            cont = cont.decode("utf-8")
        res = json.loads(cont)
        if type(res) == dict:
            dic = Storage()
            resolve(res, dic)
            for k,v in dic.items():
                setattr(_this, k, v)
            res = None
        else:
            raise Exception("Current only support dict type")

def resolve(res, dic):
    for k,v in res.items():
        if type(v) == dict:
            dic[k] = Storage(v)
            resolve(v, dic[k])
        else:
            dic[k] = v
