# -*- coding: utf-8 -*-
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Unicode input

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, AppContext, Dictation, Mouse, Key, Repeat, Paste, Function, Choice)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

def process_unicode(n1, n2, n3, n4):
    hex = str(n1) + str(n2) + str(n3) + str(n4)
    print(hex)
    Paste(eval("u'\u%s'" % hex)).execute()

class UnicodeRule(MergeRule):
    pronunciation = "unicode input"
    
    mapping = {
       "unicode <n1> <n2> <n3> <n4>":
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
    ]
    defaults = {
        "n1": '0',
        "n2": '0',
        "n3": '0',
        "n4": '0',
    }


#---------------------------------------------------------------------------

control.nexus().merger.add_global_rule(UnicodeRule())