# -*- coding: utf-8 -*-
def toIF(inp):
  paren = 0
  i = 0
  endloop = False
  out = []
  last = 0
  sb = ""
  while True:
      if i >= len(inp) : break
      while True:
          if inp[i] == ' ':
              if len(sb) > 0:
                  out.append(sb)
                  sb = "" 
              i += 1
              break
          if inp[i] == 'n' or inp[i] == "N":
              sb += inp[i]
              if i >= len(inp)-1:
                  out.append(sb)
                  sb = ""
                  i += 2
                  break
              if inp[i+1] == ' ' or inp[i+1] == "'":
                  out.append(sb)
                  i += 2
                  sb = ""
                  break
              else:
                  if __isConsonant(ord(inp[i+1])) and not (inp[i+1] == "y" or inp[i+1] == "Y"):
                      out.append(sb)
                      i += 1
                      sb = ""
                      break
                  i += 1
          # misc cases
          if inp[i] == '"' or inp[i] == "'":
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
          if not inp[i].isalpha():
            out.append(inp[i])
            i += 1
            sb = ""
            break

          # vowel handling
          endloop = False
          last = 95
          while True:
              if endloop : break
              while True:
                  if inp[i] == ' ':
                      if len(sb) > 0:
                          out.append(sb)
                          sb = "" 
                      i += 1
                      break
                  if __isVowel(ord(inp[i])):
                      sb += inp[i]
                      out.append(sb)
                      sb = ""
                      i += 1
                      endloop = True
                      break
                  if __isConsonant(ord(inp[i])):
                      if ord(inp[i]) == last:
                          sb = ""
                          if ord(inp[i]) < 90:
                              out.append("_TSU_")
                          else:
                              out.append("_tsu_")
                      sb += inp[i]
                      last = ord(inp[i])
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

vtable = [True, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False]

def __isRomaji(string):
   if string.strip()[0].isalpha():
      return True
   else:
      return False
   
def __isVowel(c):
  return vtable[c - 65]

def __isConsonant(c):
  return not(__isVowel(c))
