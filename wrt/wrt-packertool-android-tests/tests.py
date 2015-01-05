#!/usr/bin/env python 
# coding=utf-8 
import random,os,sys,unittest,run_app,codecs 
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 
class TestCaseUnit(unittest.TestCase): 
 
  def test_positive_cmd1(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd1-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd1-positive"))

  def test_positive_cmd10(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd10-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd10-positive"))

  def test_positive_cmd100(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd100-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd100-positive"))

  def test_positive_cmd101(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd101-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd101-positive"))

  def test_positive_cmd102(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd102-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd102-positive"))

  def test_positive_cmd103(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd103-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd103-positive"))

  def test_positive_cmd104(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd104-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd104-positive"))

  def test_positive_cmd105(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd105-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd105-positive"))

  def test_positive_cmd106(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd106-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd106-positive"))

  def test_positive_cmd107(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd107-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd107-positive"))

  def test_positive_cmd108(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd108-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd108-positive"))

  def test_positive_cmd109(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd109-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd109-positive"))

  def test_positive_cmd11(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd11-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd11-positive"))

  def test_positive_cmd110(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd110-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd110-positive"))

  def test_positive_cmd111(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd111-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd111-positive"))

  def test_positive_cmd112(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd112-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd112-positive"))

  def test_positive_cmd113(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd113-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd113-positive"))

  def test_positive_cmd114(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd114-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd114-positive"))

  def test_positive_cmd115(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd115-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd115-positive"))

  def test_positive_cmd116(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd116-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd116-positive"))

  def test_positive_cmd117(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd117-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd117-positive"))

  def test_positive_cmd118(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd118-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd118-positive"))

  def test_positive_cmd119(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd119-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd119-positive"))

  def test_positive_cmd12(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd12-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd12-positive"))

  def test_positive_cmd120(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd120-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd120-positive"))

  def test_positive_cmd121(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd121-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd121-positive"))

  def test_positive_cmd122(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd122-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd122-positive"))

  def test_positive_cmd123(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd123-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd123-positive"))

  def test_positive_cmd124(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd124-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd124-positive"))

  def test_positive_cmd125(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd125-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd125-positive"))

  def test_positive_cmd126(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd126-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd126-positive"))

  def test_positive_cmd127(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd127-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd127-positive"))

  def test_positive_cmd128(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd128-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd128-positive"))

  def test_positive_cmd129(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd129-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd129-positive"))

  def test_positive_cmd13(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd13-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd13-positive"))

  def test_positive_cmd130(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd130-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd130-positive"))

  def test_positive_cmd131(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd131-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd131-positive"))

  def test_positive_cmd132(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd132-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd132-positive"))

  def test_positive_cmd133(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd133-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd133-positive"))

  def test_positive_cmd134(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd134-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd134-positive"))

  def test_positive_cmd135(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd135-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd135-positive"))

  def test_positive_cmd136(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd136-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd136-positive"))

  def test_positive_cmd137(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd137-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd137-positive"))

  def test_positive_cmd138(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd138-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd138-positive"))

  def test_positive_cmd139(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd139-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd139-positive"))

  def test_positive_cmd14(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd14-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd14-positive"))

  def test_positive_cmd140(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd140-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd140-positive"))

  def test_positive_cmd141(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd141-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd141-positive"))

  def test_positive_cmd142(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd142-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd142-positive"))

  def test_positive_cmd143(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd143-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd143-positive"))

  def test_positive_cmd144(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd144-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd144-positive"))

  def test_positive_cmd145(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd145-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd145-positive"))

  def test_positive_cmd146(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd146-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd146-positive"))

  def test_positive_cmd147(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd147-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd147-positive"))

  def test_positive_cmd148(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd148-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd148-positive"))

  def test_positive_cmd149(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd149-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd149-positive"))

  def test_positive_cmd15(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd15-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd15-positive"))

  def test_positive_cmd150(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd150-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd150-positive"))

  def test_positive_cmd151(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd151-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd151-positive"))

  def test_positive_cmd152(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd152-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd152-positive"))

  def test_positive_cmd153(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd153-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd153-positive"))

  def test_positive_cmd154(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd154-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd154-positive"))

  def test_positive_cmd155(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd155-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd155-positive"))

  def test_positive_cmd156(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd156-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd156-positive"))

  def test_positive_cmd157(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd157-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd157-positive"))

  def test_positive_cmd158(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd158-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd158-positive"))

  def test_positive_cmd159(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd159-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd159-positive"))

  def test_positive_cmd16(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd16-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd16-positive"))

  def test_positive_cmd160(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd160-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd160-positive"))

  def test_positive_cmd161(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd161-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd161-positive"))

  def test_positive_cmd162(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd162-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd162-positive"))

  def test_positive_cmd163(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd163-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd163-positive"))

  def test_positive_cmd164(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd164-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd164-positive"))

  def test_positive_cmd165(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd165-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd165-positive"))

  def test_positive_cmd166(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd166-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd166-positive"))

  def test_positive_cmd167(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd167-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd167-positive"))

  def test_positive_cmd168(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd168-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd168-positive"))

  def test_positive_cmd169(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd169-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd169-positive"))

  def test_positive_cmd17(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd17-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd17-positive"))

  def test_positive_cmd170(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd170-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd170-positive"))

  def test_positive_cmd171(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd171-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd171-positive"))

  def test_positive_cmd172(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd172-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd172-positive"))

  def test_positive_cmd173(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd173-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd173-positive"))

  def test_positive_cmd174(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd174-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd174-positive"))

  def test_positive_cmd175(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd175-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd175-positive"))

  def test_positive_cmd176(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd176-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd176-positive"))

  def test_positive_cmd177(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd177-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd177-positive"))

  def test_positive_cmd178(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd178-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd178-positive"))

  def test_positive_cmd179(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd179-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd179-positive"))

  def test_positive_cmd18(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd18-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd18-positive"))

  def test_positive_cmd180(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd180-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd180-positive"))

  def test_positive_cmd181(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd181-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd181-positive"))

  def test_positive_cmd182(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd182-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd182-positive"))

  def test_positive_cmd183(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd183-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd183-positive"))

  def test_positive_cmd184(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd184-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd184-positive"))

  def test_positive_cmd185(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd185-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd185-positive"))

  def test_positive_cmd186(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd186-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd186-positive"))

  def test_positive_cmd187(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd187-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd187-positive"))

  def test_positive_cmd188(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd188-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd188-positive"))

  def test_positive_cmd189(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd189-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd189-positive"))

  def test_positive_cmd19(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd19-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd19-positive"))

  def test_positive_cmd190(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd190-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd190-positive"))

  def test_positive_cmd191(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd191-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd191-positive"))

  def test_positive_cmd192(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd192-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd192-positive"))

  def test_positive_cmd193(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd193-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd193-positive"))

  def test_positive_cmd194(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd194-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd194-positive"))

  def test_positive_cmd195(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd195-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd195-positive"))

  def test_positive_cmd196(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd196-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd196-positive"))

  def test_positive_cmd197(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd197-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd197-positive"))

  def test_positive_cmd198(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd198-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd198-positive"))

  def test_positive_cmd199(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd199-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd199-positive"))

  def test_positive_cmd2(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd2-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd2-positive"))

  def test_positive_cmd20(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd20-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd20-positive"))

  def test_positive_cmd200(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd200-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd200-positive"))

  def test_positive_cmd201(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd201-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd201-positive"))

  def test_positive_cmd202(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd202-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd202-positive"))

  def test_positive_cmd203(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd203-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd203-positive"))

  def test_positive_cmd204(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd204-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd204-positive"))

  def test_positive_cmd205(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd205-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd205-positive"))

  def test_positive_cmd206(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd206-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd206-positive"))

  def test_positive_cmd207(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd207-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd207-positive"))

  def test_positive_cmd208(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd208-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd208-positive"))

  def test_positive_cmd209(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd209-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd209-positive"))

  def test_positive_cmd21(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd21-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd21-positive"))

  def test_positive_cmd210(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd210-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd210-positive"))

  def test_negative_cmd211(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd211-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd211-negative"))

  def test_negative_cmd212(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd212-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd212-negative"))

  def test_negative_cmd213(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd213-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd213-negative"))

  def test_negative_cmd214(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd214-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd214-negative"))

  def test_negative_cmd215(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd215-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd215-negative"))

  def test_negative_cmd216(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd216-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd216-negative"))

  def test_negative_cmd217(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd217-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd217-negative"))

  def test_negative_cmd218(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd218-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd218-negative"))

  def test_negative_cmd219(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd219-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd219-negative"))

  def test_positive_cmd22(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd22-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd22-positive"))

  def test_negative_cmd220(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd220-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd220-negative"))

  def test_negative_cmd221(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd221-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd221-negative"))

  def test_negative_cmd222(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd222-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd222-negative"))

  def test_negative_cmd223(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd223-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd223-negative"))

  def test_negative_cmd224(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd224-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd224-negative"))

  def test_negative_cmd225(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd225-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd225-negative"))

  def test_negative_cmd226(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd226-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd226-negative"))

  def test_negative_cmd227(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd227-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd227-negative"))

  def test_negative_cmd228(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd228-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd228-negative"))

  def test_negative_cmd229(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd229-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd229-negative"))

  def test_positive_cmd23(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd23-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd23-positive"))

  def test_negative_cmd230(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd230-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd230-negative"))

  def test_negative_cmd231(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd231-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd231-negative"))

  def test_negative_cmd232(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd232-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd232-negative"))

  def test_negative_cmd233(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd233-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd233-negative"))

  def test_negative_cmd234(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd234-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd234-negative"))

  def test_negative_cmd235(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd235-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd235-negative"))

  def test_negative_cmd236(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd236-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd236-negative"))

  def test_negative_cmd237(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd237-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd237-negative"))

  def test_negative_cmd238(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd238-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd238-negative"))

  def test_negative_cmd239(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd239-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd239-negative"))

  def test_positive_cmd24(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd24-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd24-positive"))

  def test_negative_cmd240(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd240-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd240-negative"))

  def test_negative_cmd241(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd241-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd241-negative"))

  def test_negative_cmd242(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd242-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd242-negative"))

  def test_negative_cmd243(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd243-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd243-negative"))

  def test_negative_cmd244(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd244-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd244-negative"))

  def test_negative_cmd245(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd245-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd245-negative"))

  def test_negative_cmd246(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd246-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd246-negative"))

  def test_negative_cmd247(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd247-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd247-negative"))

  def test_negative_cmd248(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd248-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd248-negative"))

  def test_negative_cmd249(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd249-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd249-negative"))

  def test_positive_cmd25(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd25-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd25-positive"))

  def test_negative_cmd250(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd250-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd250-negative"))

  def test_negative_cmd251(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd251-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd251-negative"))

  def test_negative_cmd252(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd252-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd252-negative"))

  def test_negative_cmd253(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd253-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd253-negative"))

  def test_negative_cmd254(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd254-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd254-negative"))

  def test_negative_cmd255(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd255-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd255-negative"))

  def test_negative_cmd256(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd256-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd256-negative"))

  def test_negative_cmd257(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd257-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd257-negative"))

  def test_negative_cmd258(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd258-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd258-negative"))

  def test_negative_cmd259(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd259-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd259-negative"))

  def test_positive_cmd26(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd26-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd26-positive"))

  def test_negative_cmd260(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd260-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd260-negative"))

  def test_negative_cmd261(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd261-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd261-negative"))

  def test_negative_cmd262(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd262-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd262-negative"))

  def test_positive_cmd27(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd27-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd27-positive"))

  def test_positive_cmd28(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd28-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd28-positive"))

  def test_positive_cmd29(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd29-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd29-positive"))

  def test_positive_cmd3(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd3-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd3-positive"))

  def test_positive_cmd30(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd30-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd30-positive"))

  def test_positive_cmd31(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd31-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd31-positive"))

  def test_positive_cmd32(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd32-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd32-positive"))

  def test_positive_cmd33(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd33-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd33-positive"))

  def test_positive_cmd34(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd34-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd34-positive"))

  def test_positive_cmd35(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd35-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd35-positive"))

  def test_positive_cmd36(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd36-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd36-positive"))

  def test_positive_cmd37(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd37-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd37-positive"))

  def test_positive_cmd38(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd38-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd38-positive"))

  def test_positive_cmd39(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd39-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd39-positive"))

  def test_positive_cmd4(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd4-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd4-positive"))

  def test_positive_cmd40(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd40-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd40-positive"))

  def test_positive_cmd41(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd41-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd41-positive"))

  def test_positive_cmd42(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd42-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd42-positive"))

  def test_positive_cmd43(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd43-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd43-positive"))

  def test_positive_cmd44(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd44-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd44-positive"))

  def test_positive_cmd45(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd45-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd45-positive"))

  def test_positive_cmd46(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd46-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd46-positive"))

  def test_positive_cmd47(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd47-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd47-positive"))

  def test_positive_cmd48(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd48-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd48-positive"))

  def test_positive_cmd49(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd49-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd49-positive"))

  def test_positive_cmd5(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd5-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd5-positive"))

  def test_positive_cmd50(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd50-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd50-positive"))

  def test_positive_cmd51(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd51-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd51-positive"))

  def test_positive_cmd52(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd52-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd52-positive"))

  def test_positive_cmd53(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd53-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd53-positive"))

  def test_positive_cmd54(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd54-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd54-positive"))

  def test_positive_cmd55(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd55-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd55-positive"))

  def test_positive_cmd56(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd56-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd56-positive"))

  def test_positive_cmd57(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd57-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd57-positive"))

  def test_positive_cmd58(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd58-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd58-positive"))

  def test_positive_cmd59(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd59-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd59-positive"))

  def test_positive_cmd6(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd6-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd6-positive"))

  def test_positive_cmd60(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd60-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd60-positive"))

  def test_positive_cmd61(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd61-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd61-positive"))

  def test_positive_cmd62(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd62-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd62-positive"))

  def test_positive_cmd63(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd63-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd63-positive"))

  def test_positive_cmd64(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd64-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd64-positive"))

  def test_positive_cmd65(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd65-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd65-positive"))

  def test_positive_cmd66(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd66-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd66-positive"))

  def test_positive_cmd67(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd67-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd67-positive"))

  def test_positive_cmd68(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd68-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd68-positive"))

  def test_positive_cmd69(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd69-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd69-positive"))

  def test_positive_cmd7(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd7-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd7-positive"))

  def test_positive_cmd70(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd70-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd70-positive"))

  def test_positive_cmd71(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd71-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd71-positive"))

  def test_positive_cmd72(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd72-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd72-positive"))

  def test_positive_cmd73(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd73-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd73-positive"))

  def test_positive_cmd74(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd74-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd74-positive"))

  def test_positive_cmd75(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd75-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd75-positive"))

  def test_positive_cmd76(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd76-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd76-positive"))

  def test_positive_cmd77(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd77-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd77-positive"))

  def test_positive_cmd78(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd78-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd78-positive"))

  def test_positive_cmd79(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd79-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd79-positive"))

  def test_positive_cmd8(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd8-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd8-positive"))

  def test_positive_cmd80(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd80-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd80-positive"))

  def test_positive_cmd81(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd81-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd81-positive"))

  def test_positive_cmd82(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd82-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd82-positive"))

  def test_positive_cmd83(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd83-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd83-positive"))

  def test_positive_cmd84(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd84-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd84-positive"))

  def test_positive_cmd85(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd85-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd85-positive"))

  def test_positive_cmd86(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd86-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd86-positive"))

  def test_positive_cmd87(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd87-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd87-positive"))

  def test_positive_cmd88(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd88-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd88-positive"))

  def test_positive_cmd89(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd89-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd89-positive"))

  def test_positive_cmd9(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd9-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd9-positive"))

  def test_positive_cmd90(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd90-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd90-positive"))

  def test_positive_cmd91(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd91-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd91-positive"))

  def test_positive_cmd92(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd92-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd92-positive"))

  def test_positive_cmd93(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd93-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd93-positive"))

  def test_positive_cmd94(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd94-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd94-positive"))

  def test_positive_cmd95(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd95-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd95-positive"))

  def test_positive_cmd96(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd96-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd96-positive"))

  def test_positive_cmd97(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd97-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd97-positive"))

  def test_positive_cmd98(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd98-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd98-positive"))

  def test_positive_cmd99(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd99-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd99-positive"))

if __name__ == '__main__':
    unittest.main()