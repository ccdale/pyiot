#!/usr/bin/env python3

import sys

# import pyiot

from pyiot import errorNotify
from pyiot import errorRaise

from pyiot.listener import ListeningThing


def send():
    try:
        pass
    except Exception as e:
        pyiot.errorNotify(sys.exc_info()[2], e)


if __name__ == "__main__":
    # print(dir())
    # print(dir(__builtins__))
    lt = ListeningThing(host="127.0.0.1")
    print(lt.getState())
    print(lt.switchState())
    print(lt.getState())

    # playing around with class variables (not instance variables)
    # print(f"object state is: {lt.getState()}")
    # lt2 = ListeningThing(host="example.com")
    # lt2.defaultport = 12345
    # print(f"lt2 def port: {lt2.defaultport}")
    # lt3 = ListeningThing(host="another.host")
    # print(f"lt3 port: {lt3.defaultport}")
    # ListeningThing.defaultport = 12388
    # lt4 = ListeningThing()
    # print(f"lt port: {lt.defaultport}")
    # print(f"lt2 port: {lt2.defaultport}")
    # print(f"lt3 port: {lt3.defaultport}")
    # print(f"lt4 port: {lt4.defaultport}")
    #
    # shows that changing the class level variable where it hasn't been explicitly
    # changed by an instance of the class, changes it for all RUNNING instances.
