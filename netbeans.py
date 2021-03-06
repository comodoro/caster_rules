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
        # Debugging From the keystroke sheet
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

        # Debugging windows
        "show variables": R(Key('as-1')),
        "show watches": R(Key('as-2')),
        "show call stack": R(Key('as-3')),
        "show loaded classes": R(Key('as-4')),
        "show breakpoints": R(Key('as-5')),
        "show sessions": R(Key('as-6')),
        "show threads": R(Key('as-7')),
        "show sources": R(Key('as-8')),
        "show debugging": R(Key('as-9')),

        # Window menu tools
        "show projects": R(Key('c-1')),
        "show files": R(Key('c-2')),
        "show favorites": R(Key('c-3')),
        "show services": R(Key('c-5')),
        "show navigator": R(Key('c-7')),
        "show action items": R(Key('c-6')),        
        "show tasks": R(Key('cs-6')),        
        "show output": R(Key('c-4')),        

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
        # The same
        # "add comment lines": R(Key('c-slash')),
        "delete current line": R(Key('c-e')),

        # Navigating through Source Code
        "go to type": R(Key('c-o')),
        "go to file": R(Key('as-o')),
        # Does not work even in netbeans
        # "go to Jay unit test": R(Key('cs-t')),
        "go to source": R(Key('cs-b')),
        "go to declaration": R(Key('c-b')),
        "go to line": R(Key('c-g')),
        "toggle bookmark": R(Key('cs-m')),
        "next bookmark": R(Key('cs-.')),
        "previous bookmark": R(Key('cs-,')),
        "next error": R(Key('c-.')),
        "previous error": R(Key('c-,')),
        "select next element": R(Key('as-.')),
        "select previous element": R(Key('as-,')),
        "select in projects": R(Key('cs-1')),
        "select in files": R(Key('cs-2')),
        "select in favorites": R(Key('cs-3')),
        "matching bracket": R(Key('as-[')),
        "next word match": R(Key('c-k')),
        "previous word match": R(Key('cs-k')),
        "back to last edit": R(Key('a-left')),
        "forward to last edit": R(Key('a-right')),
        "next marked occurrence": R(Key('a-up')),
        "previous marked occurrence": R(Key('a-down')),
    }


def get_rule():
    return NetbeansRule, RuleDetails(name='netbeans', executable=['netbeans', 'netbeans64'], title='Netbeans')