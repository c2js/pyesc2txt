#############################################
### Author: Joshua Hui
### Version : 1.0
### Extract text and remove ESC POS printer command Esc2Txt
### MIT License 
###
### ESC POS Command is referring to EPSON & Star Micronics Co., Ltd.
### Dynamic length of command is not support eg: print image
### Eg:
### 
### - 1B 28 42 nL nH k m s v1 v2 c BarCodeData
### - 1B 26 00 n m [a0 a1 a2 d1 d2 ... dk]
### - 1B 26 00 n m 0 [a 0 d1 d2 ... dk]
### - 1B 2E c v h m nL nH d1 d2 ... dk
### - 1B 26 00 n m [a d1 d2 ... dk]
### - 1B 28 5E nL nH d1 ... dk
### - 1B 4B nL nH d1 d2 ... dk
### - 1B 4C nL nH d1 d2 ... dk
### - 1B 59 nL nH d1 d2 ... dk
### - 1B 5A nL nH d1 d2 ... dk
### - 1B 2A m nL nH d1 ... dk
### - 1B 5E m nL nH d1 ... dk
### - 1B 2E 2 v h 1 0 0
#############################################

from collections import defaultdict

  
def nested_dict(n, type):
  if n == 1:
    return defaultdict(type)
  else:
    return defaultdict(lambda: nested_dict(n-1, type))



## only support depth of 5 of esc command
escmap = nested_dict(5, dict)


escmap["1B"]["28"]["63"] = 6
escmap["1B"]["28"]["74"] = 5
escmap["1B"]["28"]["2D"] = 5
escmap["1B"]["44"] = -1
escmap["1B"]["42"] = -1
escmap["1B"]["28"]["43"] = 4
escmap["1B"]["28"]["56"] = 4
escmap["1B"]["28"]["76"] = 4
escmap["1B"]["62"] = -1
escmap["1B"]["28"]["55"] = 3
escmap["1B"]["28"]["47"] = 3
escmap["1B"]["28"]["69"]["01"]["00"] = 1
escmap["1B"]["58"] = 3
escmap["1B"]["3A"]["00"] = 2
escmap["1B"]["24"] = 2
escmap["1B"]["5C"] = 2
escmap["1B"]["63"] = 2
escmap["1B"]["43"]["00"] = 1
escmap["1D"]["56"]["42"]["00"] = 0
escmap["1B"]["66"] = 2
escmap["1B"]["65"] = 2
escmap["1B"]["3F"] = 2
escmap["1B"]["43"] = 1
escmap["1B"]["4E"] = 1
escmap["1B"]["51"] = 1
escmap["1B"]["6C"] = 1
escmap["1B"]["4A"] = 1
escmap["1B"]["33"] = 1
escmap["1B"]["2B"] = 1
escmap["1B"]["41"] = 1
escmap["1B"]["2F"] = 1
escmap["1B"]["61"] = 1
escmap["1B"]["74"] = 1
escmap["1B"]["52"] = 1
escmap["1B"]["25"] = 1
escmap["1B"]["78"] = 1
escmap["1B"]["6B"] = 1
escmap["1B"]["70"] = 1
escmap["1B"]["20"] = 1
escmap["1B"]["21"] = 1
escmap["1B"]["2D"] = 1
escmap["1B"]["53"] = 1
escmap["1B"]["71"] = 1
escmap["1B"]["57"] = 1
escmap["1B"]["77"] = 1
escmap["1B"]["49"] = 1
escmap["1B"]["6D"] = 1
escmap["1B"]["19"] = 1
escmap["1B"]["55"] = 1
escmap["1B"]["73"] = 1
escmap["1B"]["72"] = 1
escmap["1B"]["6A"] = 1
escmap["1B"]["69"] = 0 #1
escmap["1B"]["4F"] = 0
escmap["1B"]["30"] = 0
escmap["1B"]["32"] = 0
escmap["1B"]["31"] = 0
escmap["1B"]["50"] = 0
escmap["1B"]["4D"] = 0
escmap["1B"]["67"] = 0
escmap["1B"]["45"] = 0
escmap["1B"]["46"] = 0
escmap["1B"]["34"] = 0
escmap["1B"]["35"] = 0
escmap["1B"]["47"] = 0
escmap["1B"]["48"] = 0
escmap["1B"]["54"] = 0
escmap["1B"]["0F"] = 0
escmap["1B"]["0E"] = 0
escmap["1B"]["36"] = 0
escmap["1B"]["37"] = 0
escmap["1B"]["38"] = 0
escmap["1B"]["39"] = 0
escmap["1B"]["40"] = 0
escmap["1B"]["23"] = 0
escmap["1B"]["3D"] = 0
escmap["1B"]["3E"] = 0
escmap["1C"]["70"] = 2
escmap["1D"]["21"] = 1
#escmap["0D"] = 0
#escmap["0A"] = 0
escmap["0C"] = 0
escmap["09"] = 0
escmap["0B"] = 0
escmap["08"] = 0
escmap["0F"] = 0
escmap["12"] = 0
escmap["0E"] = 0
escmap["14"] = 0
escmap["07"] = 0
escmap["18"] = 0
escmap["7F"] = 0
escmap["11"] = 0
escmap["13"] = 0

