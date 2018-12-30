# -*- coding: utf-8 -*-
# This file is a command-module for Dragonfly by Christo Butcher and Caster by Synkarius
# Created by Vojtěch Drábek on 2018-12
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for generic chessboard input, computer notation and have to
set up the board corners first

"""
# ---------------------------------------------------------------------------
import logging

from dragonfly import Mouse, Function, Choice, Grammar
from dragonfly.actions.action_mouse import get_cursor_position

from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

logger = logging.getLogger(__name__)


class Board():
    left_top = None
    right_bottom = None
    flipped = 0

def flip():
    Board.flipped = 1 - Board.flipped

def calibrate(corner):
    coords = get_cursor_position()
    logger.info(Board)
    if (corner):
        Board.left_top = coords
    else:
        Board.right_bottom = coords

def x_coord(left, width, input, flipped=0):
    x = input if not flipped else 9 - input
    return int(left + (x - 0.5) * width / 8.0)

def y_coord(top, height, input, flipped=0):
    y = input if flipped else 9 - input
    return int(top + (y - 0.5) * height / 8.0)

def move(chess_letter, chess_number, chess_letter2, chess_number2):
    if not Board.right_bottom or not Board.left_top:
        raise Exception("Board not calibrated!")
    logger.info((Board.right_bottom, Board.left_top))
    width = Board.right_bottom[0] - Board.left_top[0]
    height = Board.right_bottom[1] - Board.left_top[1]
    logger.info(str((width, height)))
    x1, y1 = float(chess_letter), float(chess_number)
    logger.info(str((x1, y1)))
    source = (x_coord(Board.left_top[0], width, x1, Board.flipped),
              y_coord(Board.left_top[1], height, y1, Board.flipped))
    logger.info(str(source))
    x2, y2 = float(chess_letter2), float(chess_number2)
    destination = (x_coord(Board.left_top[0], width, x2, Board.flipped),
                   y_coord(Board.left_top[1], height, y2, Board.flipped))
    logger.info(str(destination))
    click_action = "%s, left:down, %s, left:up" % (str(source), str(destination))
    logger.info(click_action)
    Mouse(click_action).execute()

LETTERS = {
            "a | A | arch": "1",
            "b | B | brov": "2",
            "c | C | char": "3",
            "d | D | delta": "4",
            "e | E | echo": "5",
            "f | F | foxy": "6",
            "g | G | goof": "7",
            "h | H | hotel": "8",
        }

NUMBERS = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
        }


class ChessInputRule(MergeRule):

    pronunciation = "chess input"

    mapping = {
        "calibrate <corner> corner":
            R(Function(calibrate)),
        "<chess_letter> <chess_number> <chess_letter2> <chess_number2>":
            R(Function(move)),
        "flip board":
            R(Function(flip))
    }

    extras = [
        Choice("corner", {
            "left top": True,
            "top left": True,
            "right bottom": False,
            "bottom right": False,
        }),
        Choice("chess_letter", LETTERS),
        Choice("chess_letter2", LETTERS),
        Choice("chess_number", NUMBERS),
        Choice("chess_number2", NUMBERS),
    ]

    defaults = {}


# ---------------------------------------------------------------------------
grammar = Grammar(name="chess input")
grammar.add_rule(ChessInputRule())
grammar.load()
