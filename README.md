# loadcf
It is a python config file loader. It convert config item to python module item, then you can import and use it direct.
Support Python2.7, Python3.5

# Usage

  """
  {"debug": true, "items": [1, 2, 3, 4], "mysql": {"slave": {"db": "postgresql", "user": "root"}, "name": "mysql", "db": "blog", "port": 3306}}
  """

  import loadcf
  loadcf.load("config file path")
  from loadcf import *

  print(debug)
  print(mysql.slave)
  print(mysql.slave.user)
