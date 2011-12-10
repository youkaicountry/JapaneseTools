#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import R2K as __R2K
from . import K2R as __K2R
from . import tools as __tools
from . import Conjugation as __Conjugation

romajiToKana = __R2K.romajiToKana #takes a string of romaji
kanaToRomaji = __K2R.kanaToRomaji #takes a string of kana

splitRomajiToString = __tools.splitRomajiToString #splits romaji and outputs a space separated string of its constituant parts
splitRomajiToList = __tools.splitRomajiToList     #splits romaji and outputs a list of its constituant parts

conjugateKanaVerb = __Conjugation.conjugateKanaVerb     #conjugates a verb given in kana, and returns a list of possible conjugations
conjugateRomajiVerb = __Conjugation.conjugateRomajiVerb #conjugates a verb given in romaji, and returns a list of possible conjugations

kanaToAllHiragana = __tools.kanaToAllHiragana
kanaToAllKatakana = __tools.kanaToAllKatakana
romajiToAllHiragana = __tools.romajiToAllHiragana
romajiToAllKatakana = __tools.romajiToAllKatakana
