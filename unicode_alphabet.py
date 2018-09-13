# -*- coding: utf-8 -*-
# This file is a command-module for Dragonfly by Christo Butcher and Caster by Synkarius
# Created by Vojtech Drábek on 2018-05
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Unicode alphabet dictation
Enhances built-in Caster alphabet with some accents
Example: "big uniform ring" prints "Ů"

"""
import unicodedata

from dragonfly import Function, Choice, Text, Key

from caster.lib import context, control, alphanumeric
from caster.lib.dfplus.merge.ccrmerger import CCRMerger
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

def get_alphabet_choice(spec):
    return Choice(
        spec, {
            "arch": "a",
            "brov": "b",
            "char": "c",
            "delta": "d",
            "echo": "e",
            "foxy": "f",
            "goof": "g",
            "hotel": "h",
            "India": "i",
            "julia": "j",
            "kilo": "k",
            "Lima": "l",
            "Mike": "m",
            "Novakeen": "n",
            "oscar": "o",
            "prime": "p",
            "Quebec": "q",
            "Romeo": "r",
            "Sierra": "s",
            "tango": "t",
            "uniform": "u",
            "victor": "v",
            "whiskey": "w",
            "x-ray": "x",
            "yankee": "y",
            "Zulu": "z",
        })

def write_letter(big, letter, accent=None):
    if accent:
        if big:
            letter = letter.upper()
        combined_letter = unicodedata.normalize('NFC', letter + accent)
		#Combine only letters that can be combined
        if len(combined_letter) == 1:
            letter = combined_letter 
        context.paste_string_without_altering_clipboard(letter)
    else:
        if big:
            Key("shift:down").execute()
        Text(letter).execute()
        if big:
            Key("shift:up").execute()

class UnicodeAlphabet(MergeRule):
    pronunciation = "unicode alphabet"

    mapping = {
        "[<big>] <letter> [<accent>]":
            R(Function(write_letter, extra={"big", "letter", "accent"}),
              rdescript="Spell"),
    }
    extras = [
        get_alphabet_choice("letter"),
        Choice("big", {
            "big": "big",
        }),
        Choice("accent", {
            "grave": u'\u0300',
            "acute": u'\u0301',
            "circumflex": u'\u0302',
            "tilde": u'\u0303',
            "caron": u'\u030C',
            "ring": u'\u030A',
            "diaresis": u'\u0308',
			#perhaps others, cedilla or ogonek
            #"said Hilda": u'\u0327',
            #"organic": u'\u0328',
        }),
    ]
    defaults = {
        "big": "",
    }


control.nexus().merger.add_global_rule(UnicodeAlphabet())
