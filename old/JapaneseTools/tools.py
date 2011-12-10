#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import R2K
from . import K2R

vtable = [True, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False]

def isRomaji(string):
   if string.strip()[0].isalpha():
      return True
   else:
      return False
   
def isVowel(c):
  return vtable[c - 65]

def isConsonant(c):
  return not(isVowel(c))

#will convert to all kana from kanji or whatever
def japaneseToKana(input):
   return input

def kanaToAllHiragana(input):
   out = K2R.kanaToRomaji(input)
   out = romajiToAllHiragana(out)
   return R2K.romajiToKana(out)

def kanaToAllKatakana(input):
   out = K2R.kanaToRomaji(input)
   out = romajiToAllKatakana(out)
   return R2K.romajiToKana(out)

def romajiToAllHiragana(input):
   return input.lower()

def romajiToAllKatakana(input):
   return input.upper()

def splitRomajiToString(input):
   l = splitRomajiToList(input)
   out = ""
   for x in l:
      out += x + " "
   return out.strip()

def splitRomajiToList(input):
  paren = 0
  i = 0
  endloop = False
  out = []
  last = 0
  sb = ""
  while True:
      if i >= len(input) : break
      while True:
          if input[i] == ' ':
              if len(sb) > 0:
                  out.append(sb)
                  sb = "" 
              i += 1
              break
          if input[i] == 'n' or input[i] == "N":
              sb += input[i]
              if i >= len(input)-1:
                  out.append(sb)
                  sb = ""
                  i += 2
                  break
              if input[i+1] == ' ' or input[i+1] == "'":
                  out.append(sb)
                  i += 2
                  sb = ""
                  break
              else:
                  if isConsonant(ord(input[i+1])) and not (input[i+1] == "y" or input[i+1] == "Y"):
                      out.append(sb)
                      i += 1
                      sb = ""
                      break
                  i += 1
          # misc cases
          if input[i] == '"' or input[i] == "'":
              if len(sb) > 0 : out.append(sb)
              sb = ""
              if paren == 0:
                  out.append('->')
                  paren = 1
                  i += 1
                  break
              else:
                  out.append('<-')
                  paren = 0
                  i += 1
                  break
          if not input[i].isalpha():
            out.append(input[i])
            i += 1
            sb = ""
            break

          # vowel handling
          endloop = False
          last = 95
          while True:
              if endloop : break
              while True:
                  if input[i] == ' ':
                      if len(sb) > 0:
                          out.append(sb)
                          sb = "" 
                      i += 1
                      break
                  if isVowel(ord(input[i])):
                      sb += input[i]
                      out.append(sb)
                      sb = ""
                      i += 1
                      endloop = True
                      break
                  if isConsonant(ord(input[i])):
                      if ord(input[i]) == last:
                          sb = ""
                          if ord(input[i]) < 90:
                              out.append("_TSU_")
                          else:
                              out.append("_tsu_")
                      sb += input[i]
                      last = ord(input[i])
                      i += 1
                      break
                  break
          break
  #out.encode('utf-8')
   
  out2 = []
  for x in out:
   if x[0].isupper():
      out2.append(x.upper())
   elif x[0].islower():
      out2.append(x.lower())
   else:
      out2.append(x)
  return out2
