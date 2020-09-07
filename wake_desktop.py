# -*- coding: utf-8 -*-
# This file is a command-module for Dragonfly by Christo Butcher and castervoice by Synkarius
# Created by Vojtech Drábek on 2020-08-12
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
A Wake On LAN rule adapted for Caster
"""
import socket
import threading
import time

from dragonfly import Function, Key, MappingRule, RunCommand, StartApp

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

from personal import NETWORK, DESKTOP, DESKTOP_MAC, TERMINAL
from wol import wake

def ping(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def my_wake():
    wake(NETWORK, DESKTOP_MAC)

class WakeChecker(threading.Thread):
    def __init__(self, host, port, action):
        self._timer = None
        self._host = host
        self._port = port
        self._action = action
        self._running = True
        super(WakeChecker, self).__init__()

    def start(self):
        print("Sending Wake On LAN to %s" % DESKTOP_MAC)
        super(WakeChecker, self).start()
    
    def check(self):
        if ping(self._host, self._port):
            self._running = False
            self._action.execute()
    
    def run(self):
        while self._running:
            time.sleep(10)
            self.check()


class NetWakeRule(MappingRule):
    pronunciation = "net wake rule"
    args = TERMINAL.extend(['ssh', DESKTOP])
    checker = WakeChecker(DESKTOP, 22,  StartApp(*TERMINAL))
    mapping = {
        "wake desktop": R(Function(my_wake) + Function(checker.start))
    }

def get_rule():
    return NetWakeRule, RuleDetails(name="Net Wake Rule")