#!/usr/bin/env python
# -*- coding: utf-8 -*-

#verb forms:
#utau
#v3     - dictionary form (utau)
#v2     - masu stem       (utai)
#v2masu - masu form       (utaimasu)

from . import R2K
from . import K2R
from . import tools

#each of these should take a kana list, and return a list of all candidates
def __V3ToV2(kanalist):
   if len(kanalist) < 2:
      return kanalist
   if kanalist == ["su","ru"]:
      return [["shi"]]
   if kanalist == ["ku","ru"]:
      return [["ki"]]
   t = kanalist[-2][-1]
   if t == "e" or t == "i":
      if kanalist[-1] == "ru":
         return [kanalist[:-1]]
   out = kanalist
   out[-1] = out[-1][:-1] + "i"
   return [out]

def __V2MASUToV2(kanalist):
   return [kanalist[:-2]]

def __V2ToV3(kanalist):
   return

def __V2ToV2MASU(kanalist):   
   return

def conjugateKanaVerb(verb, currentform, targetform):
   out = conjugateRomajiVerb(K2R.kanaToRomaji(tools.kanaToAllHiragana(verb)), currentform, targetform)
   out2 = []
   for x in out:
      out2.append(tools.R2K.romajiToKana(x))
   return out2

#conjugates a verb given in a romaji string from current form to target form
def conjugateRomajiVerb(verb, currentform, targetform):
   
   kl = tools.splitRomajiToList(tools.romajiToAllHiragana(verb))
   a = currentform.lower()
   b = targetform.lower()
   
   #TODO: after each step consolidate entries that are the same (actually, use a set)
   clist = [kl]
   for x in steps[(a, b)]:
      temp = []
      for y in clist:
         temp += x(y)
      clist = temp
   out = []
   sb = ""
   for x in clist:
      sb = ""
      for y in x:
         sb += y
      out.append(sb)
      
   return out

steps = {}
steps[("v3", "v2")] = [__V3ToV2]
steps[("v3", "v2masu")] = [__V3ToV2, __V2ToV2MASU]
steps[("v2masu", "v3")] = [__V2MASUToV2, __V2ToV3]
