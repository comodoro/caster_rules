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
        "run projet": R(Key('f6')),
        "debug projet": R(Key('c-f5')),
        }


def get_rule():
    return NetbeansRule, RuleDetails(name='netbeans', executable=['netbeans', 'netbeans64'], title='Netbeans')