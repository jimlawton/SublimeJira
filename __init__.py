import sys
import os
import ssl


plugin = os.path.abspath(os.path.split(__file__)[0])
libpath = os.path.join(plugin, 'lib')


if not plugin in sys.path:
  sys.path.append(plugin)

if not libpath in sys.path:
  sys.path.append(libpath)

VERSION = '0.1.4'

import requests

def plugin_loaded():
    from imp import reload
    reload(requests)
