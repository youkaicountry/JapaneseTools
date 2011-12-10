#!/usr/bin/env python
# -*- coding: utf-8 -*-

import JapaneseTools

"""a = JapaneseTools.romajiToKana("ryouko ha suiseiseki ni asobimashita.")
print len(a)
print a

b = JapaneseTools.kanaToRomaji(a)
print len(b)
print b

c = JapaneseTools.splitRomajiToString("atai ha baka ja nai yo. 'akakute kurokute unyu'. 'tenki ga''ii' kara sanpo shimashou. chotto. son'ara.")
print c"""

d = JapaneseTools.conjugateRomajiVerb("utau", "v3", "v2")
print(d)

e = JapaneseTools.romajiToKana("chiruno")
print(e)
e = JapaneseTools.kanaToAllKatakana(e)
print(e)

f = JapaneseTools.romajiToKana("utau")
f = JapaneseTools.conjugateKanaVerb(f, "v3", "v2")
print(f[0])

#print JapaneseTools.
