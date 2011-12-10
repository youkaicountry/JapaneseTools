# -*- coding: utf-8 -*-
from . import i, j, k, r, gtype

#converts the given object to the type listed
def convert(object, sourcetype=None, targettype="k"):
   if sourcetype == None:
      return convertSpecific(object, getType(object), targettype)
   return convertSpecific(object, sourcetype, targettype)

#converts the given object that is type sourcetype to tyoe targettype
def convertSpecific(object, sourcetype, targettype):
   s = gtype.standardizeType(sourcetype)
   t = gtype.standardizeType(targettype)
   #print(s, t)
   if s == t: return object
   iter = ctable[(s, t)]
   out = object
   for x in iter:
      out = x(out)
   return out

#returns the type of the object
def getType(object):
   return gtype.getType(object)

#flips character set using the given rules 
#i->k, j->r, k->r, r->k
def flipType(object):
   return

#converts to all hiragana
def lower(object):
   return 

#converts to all katakana
def upper(object):
   return

#conversion table
ctable = {}
ctable[("k", "r")] = [k.toIF, i.toRomaji] #d
ctable[("k", "i")] = [k.toIF] #d
#ctable[("k", "j")] = [k.toIF, i.toJapanese]
ctable[("r", "k")] = [r.toIF, i.toKana]
ctable[("r", "i")] = [r.toIF]
#ctable[("r", "j")] = [r.toIF, i.toJapanese]
#ctable[("j","k")] = [j.toIF, i.toKana]
#ctable[("j","i")] = [j.toIF]
#ctable[("j","r")] = [j.toIF, i.toRomaji]
ctable[("i","r")] = [i.toRomaji] #d
#ctable[("i","j")] = [i.toJapanese]
ctable[("i","k")] = [i.toKana] #d
