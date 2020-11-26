import os
import unittest
from pathlib import Path

from template import *


def test_reduce_fraction():
    assert reduceFraction(12, 15) == (4, 5)
    assert reduceFraction(3, 7) == (3, 7)
    assert reduceFraction(8, 16) == (1, 2)


def test_magic_dates():
    assert isMagicDate(6, 10, 1960) == True
    assert isMagicDate(3, 4, 2012) == True
    assert isMagicDate(4, 12, 2020) == False


def test_sublist():
    case = unittest.TestCase()
    case.assertCountEqual(sublist(["a", 1]), [[], ["a"], [1], ["a", 1]])
    case.assertCountEqual(
        sublist([1, 2, 3, 4]),
        [
            [],
            [1],
            [2],
            [3],
            [4],
            [1, 2],
            [2, 3],
            [3, 4],
            [1, 2, 3],
            [2, 3, 4],
            [1, 2, 3, 4],
        ],
    )
    case.assertCountEqual(
        sublist(["a", 2, (0, "zero")]),
        [
            [],
            ["a"],
            [2],
            [(0, "zero")],
            ["a", 2],
            [2, (0, "zero")],
            ["a", 2, (0, "zero")],
        ],
    )


def test_pig_latin():
    assert pigLatin("computer") == "omputercay"
    assert pigLatin("think") == "inkthay"
    assert pigLatin("algorithm") == "algorithmway"
    assert pigLatin("office") == "officeway"
    assert pigLatin("Computer") == "Omputercay"
    assert pigLatin("Science!") == "Iencescay!"


def test_morse_code():
    assert morseCode("Hello, World!") == ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
    assert (
        morseCode("Testing, 1, 2, 3, Testing!")
        == "- . ... - .. -. --. .---- ..--- ...-- - . ... - .. -. --."
    )
    assert (
        morseCode("1 is one! 2 is two?")
        == ".---- .. ... --- -. . ..--- .. ... - .-- ---"
    )


def test_int_2_text():
    assert int2Text(142) == "one hundred fourty two"
    assert int2Text(300) == "three hundred"
    assert int2Text(16) == "sixteen"
    assert int2Text(912) == "nine hundred twelve"


def test_missing_comment():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file1 = Path(script_dir, "test_data", "code1.py")
    input_file2 = Path(script_dir, "test_data", "code2.py")
    assert missingComment(input_file1) == ["__init__", "overdrawn"]
    assert missingComment(input_file2) == []


def test_consistent_line_length():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = Path(script_dir, "test_data", "text1.txt")
    assert consistentLineLength(input_file, 50) == [
        "Alice was beginning to get very tired of sitting",
        "by her sister on the bank, and of having nothing",
        "to do: once or twice she had peeped into the book",
        "her sister was reading, but it had no pictures or",
        'conversations in it,"and what is the use of a',
        'book," thought Alice, "without pictures or',
        'conversations?"',
    ]
    assert consistentLineLength(input_file, 20) == [
        "Alice was beginning",
        "to get very tired of",
        "sitting by her",
        "sister on the bank,",
        "and of having",
        "nothing to do: once",
        "or twice she had",
        "peeped into the book",
        "her sister was",
        "reading, but it had",
        "no pictures or",
        "conversations in",
        'it,"and what is the',
        'use of a book,"',
        "thought Alice,",
        '"without pictures or',
        'conversations?"',
    ]


def test_knight():
    assert knight("a1", "c5", 2) == True
    assert knight("c2", "e3", 3) == True
    assert knight("c6", "h1", 3) == False


def test_war_of_species():
    assert warOfSpecies(["XX......", "XX....O.", ".....OOO"]) == [
        "XXX.....",
        "XXX..OOO",
        "XX....O.",
    ]
    assert warOfSpecies(["XX....", "XX....", "OOOOOO"]) == [
        "XXX...",
        "XXOOOO",
        "......",
    ]
    assert warOfSpecies(["XXX...", "XXOOOO", "......"]) == [
        "XX.OOO",
        "XX....",
        "XXOOOO",
    ]
