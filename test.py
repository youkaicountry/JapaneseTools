import Tester
import JapaneseTools
import collections

def rtok():
   tests = collections.OrderedDict()
   tests["boku"] = "ぼく"
   tests["atai"] = "あたい"
   tests["shinbun"] = "しんぶん"
   tests["shin'osaka"] = "しんおさか"
   tests["NEISEN"] = "ネイセン"
   tests["tewi"] = "てゐ"
   tests["HANYU-"] = "ハニュー"
   for x in tests:
      result = JapaneseTools.Conversion.convert(x, sourcetype="r", targettype="k")
      if result != tests[x]: return Tester.Result(False, "Failed on '" + x + "'") 
   return Tester.Result(True, "All Romaji to Kana worked properly")
   
def getType():
   tests = []
   tests.append(["anata ha BAKA desu.", "r"])
   tests.append(["あなたはバカです。", "k"])
   tests.append([["a", "na", "ta", "ha", "ba", "ka", "de", "su", "."], "i"])
   for x in tests:
      result = JapaneseTools.Conversion.getType(x[0])
      if result != x[1]: return Tester.Result(False, "Failed on " + str(x))
   
   return Tester.Result(True, "All Types were properly detected")
   
def ktor():
   tests = collections.OrderedDict()
   tests["ぼく"] = "boku"
   tests["あたい"] = "atai"
   tests["しんぶん"] = "shin'bun'"
   tests["しんおさか"] = "shin'osaka"
   tests["ネイセン"] = "NEISEN'"
   tests["てゐ"] = "tewi"
   tests["ハニュー"] = "HANYU-"
   for x in tests:
      result = JapaneseTools.Conversion.convert(x, sourcetype="k", targettype="r")
      if result != tests[x]: return Tester.Result(False, "Failed on '" + x + "'")
   return Tester.Result(True, "All Kana to Romaji worked properly")
   

#TODO : Make n/n' more intelligent in the k to r converter                               
#print(JapaneseTools.Conversion.convert("しんぶん", targettype="r"))

#print(JapaneseTools.Conversion.convert("ハニュー", targettype="r"))
   
t = Tester.Tester()
t.addTest("Romaji To Kana", "Tests Romaji to Kana conversion", rtok)
t.addTest("Type Detection", "Tests the capacity to determine the type of a string", getType)
t.addTest("Kana To Romaji", "Tests Kana to Romaji conversion", ktor)

Tester.makeGUI(t)

t.doAllTests()

print("t")

r = t.getAllTests()
for x in r:
   print(str(x))
   print("")
