# -*- coding: utf-8 -*-
# This file is a command-module for Dragonfly by Christo Butcher and castervoice by Synkarius
# Created by Vojtěch Drábek on 2018-05
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Unicode input
Prints Unicode codepoint from spoken hex string
Example: "unicode zero three brov one" prints "α"

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, AppContext, Dictation, Mouse, Key, Repeat, Function, Choice)

from castervoice.lib import context, control
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib import settings
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.merge.state.short import R
from castervoice.lib.const import CCRType

def process_unicode(n1, n2, n3, n4, n5='', n6=''):
    hex = str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6)
    character = eval("u'\u%s'" % hex)
    #Change the paste to Text action when Unicode in Text is supported
    #Invalid codepoint will just throw an error as expected
    context.paste_string_without_altering_clipboard(character)

class UnicodeRule(MergeRule):
    __name__ = "unicode input"
    
    mapping = {
       "unicode <n1> <n2> <n3> <n4> [<n5> [<n6>]]":
            R(Function(process_unicode)),
    }
    choices = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'arch': 'a',
    'brov': 'b',
    'char': 'c',
    'delta': 'd',
    'echo': 'e',
    'foxy': 'f',
    }
    
    extras = [
        Choice("n1", choices),
        Choice("n2", choices),
        Choice("n3", choices),
        Choice("n4", choices),
        Choice("n5", choices),
        Choice("n6", choices),
    ]
    defaults = {
        "n1": '0',
        "n2": '0',
        "n3": '0',
        "n4": '0',
        "n5": '',
        "n6": '',
    }


#---------------------------------------------------------------------------

def get_rule():
    return UnicodeRule, RuleDetails(ccrtype=CCRType.GLOBAL)