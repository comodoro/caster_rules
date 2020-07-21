# -*- coding: utf-8 -*-
# This file is a command-module for Dragonfly by Christo Butcher and castervoice by Synkarius
# Created by Vojtech Drábek on 2020-06-19
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Netbeans
"""
from dragonfly import Key, MappingRule

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R
class NetbeansRule(MappingRule):
    pronunciation = "net beans"

    mapping = {
        # Debugging
        "debug project": R(Key('c-f5')),
        "debug file": R(Key('cs-f5')),
        "debug test": R(Key('cs-f6')),
        "stop debugging": R(Key('s-f5')),
        "step out": R(Key('f7')),
        "run to cursor": R(Key('f4')),
        "continue": R(Key('f5')),
        "go to called method": R(Key('ca-up')),
        "go to calling method": R(Key('ca-down')),
        "evaluate expression": R(Key('c-f9')),
        "breakpoint": R(Key('c-f8')),
        "new breakpoinr": R(Key('cs-f8')),
        "new watch": R(Key('cs-f7')),

        # Compiling, Testing, and Running
        "compile": R(Key('f9')),
        "build main project": R(Key('f11')),
        "clean and build": R(Key('s-f11')),
        "set request parameters": R(Key('c-q')),
        "create unit test": R(Key('cs-u')),
        "unit test file": R(Key('c-f6')),
        "unit test project": R(Key('a-f6')),
        "run main project": R(Key('f6')),
        "run file": R(Key('s-f6')),

        # Coding in Java
        "generate code": R(Key('a-insert')),
        "fix all imports": R(Key('cs-i')),
        "fix import": R(Key('as-i')),
        "format selection": R(Key('as-f')),
        #"shift line <direction>": R(Key('as-')),
        "rectangular selection": R(Key('cs-r')),
        "copy line up": R(Key('cs-up')),
        "copy line down": R(Key('cs-down')),
        "inspect members": R(Key('c-f12')),
        "inspect hierarchy": R(Key('a-f12')),
        "remove comment lines": R(Key('cs-c')),
        "add comment lines": R(Key('c-slash')),
        "delete current line": R(Key('c-e')),
    }


def get_rule():
    return NetbeansRule, RuleDetails(name='netbeans', executable=['netbeans', 'netbeans64'], title='Netbeans')