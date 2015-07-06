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

  def test_negative_cmd161(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd161-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd161-negative"))

  def test_negative_cmd162(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd162-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd162-negative"))

  def test_negative_cmd163(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd163-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd163-negative"))

  def test_negative_cmd164(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd164-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd164-negative"))

  def test_negative_cmd165(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd165-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd165-negative"))

  def test_negative_cmd166(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd166-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd166-negative"))

  def test_negative_cmd167(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd167-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd167-negative"))

  def test_negative_cmd168(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd168-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd168-negative"))

  def test_negative_cmd169(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd169-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd169-negative"))

  def test_positive_cmd17(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd17-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd17-positive"))

  def test_negative_cmd170(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd170-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd170-negative"))

  def test_negative_cmd171(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd171-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd171-negative"))

  def test_negative_cmd172(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd172-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd172-negative"))

  def test_negative_cmd173(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd173-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd173-negative"))

  def test_negative_cmd174(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd174-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd174-negative"))

  def test_negative_cmd175(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd175-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd175-negative"))

  def test_negative_cmd176(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd176-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd176-negative"))

  def test_negative_cmd177(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd177-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd177-negative"))

  def test_negative_cmd178(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd178-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd178-negative"))

  def test_negative_cmd179(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd179-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd179-negative"))

  def test_positive_cmd18(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd18-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd18-positive"))

  def test_negative_cmd180(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd180-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd180-negative"))

  def test_negative_cmd181(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd181-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd181-negative"))

  def test_negative_cmd182(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd182-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd182-negative"))

  def test_negative_cmd183(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd183-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd183-negative"))

  def test_negative_cmd184(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd184-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd184-negative"))

  def test_negative_cmd185(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd185-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd185-negative"))

  def test_negative_cmd186(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd186-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd186-negative"))

  def test_negative_cmd187(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd187-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd187-negative"))

  def test_negative_cmd188(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd188-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd188-negative"))

  def test_negative_cmd189(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd189-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd189-negative"))

  def test_positive_cmd19(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd19-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd19-positive"))

  def test_negative_cmd190(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd190-negative", "/opt/wrt-packertool-android-tests/apks/arm/cmd190-negative"))

  def test_positive_cmd2(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd2-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd2-positive"))

  def test_positive_cmd20(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd20-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd20-positive"))

  def test_positive_cmd21(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd21-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd21-positive"))

  def test_positive_cmd22(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd22-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd22-positive"))

  def test_positive_cmd23(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd23-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd23-positive"))

  def test_positive_cmd24(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd24-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd24-positive"))

  def test_positive_cmd25(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd25-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd25-positive"))

  def test_positive_cmd26(self):
     self.assertEqual("PASS", run_app.tryRunApp("cmd26-positive", "/opt/wrt-packertool-android-tests/apks/arm/cmd26-positive"))

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