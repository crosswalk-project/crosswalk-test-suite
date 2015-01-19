#!/usr/bin/env python 
# coding=utf-8 
import random,os,sys,unittest,run_app,codecs 
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 
class TestCaseUnit(unittest.TestCase): 
 
  def test_positive_manifest1(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest1-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest1-positive"))

  def test_positive_manifest10(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest10-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest10-positive"))

  def test_positive_manifest100(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest100-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest100-positive"))

  def test_positive_manifest101(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest101-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest101-positive"))

  def test_positive_manifest102(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest102-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest102-positive"))

  def test_positive_manifest103(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest103-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest103-positive"))

  def test_positive_manifest104(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest104-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest104-positive"))

  def test_positive_manifest105(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest105-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest105-positive"))

  def test_positive_manifest106(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest106-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest106-positive"))

  def test_positive_manifest107(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest107-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest107-positive"))

  def test_positive_manifest108(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest108-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest108-positive"))

  def test_positive_manifest109(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest109-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest109-positive"))

  def test_positive_manifest11(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest11-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest11-positive"))

  def test_positive_manifest110(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest110-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest110-positive"))

  def test_positive_manifest111(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest111-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest111-positive"))

  def test_positive_manifest112(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest112-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest112-positive"))

  def test_positive_manifest113(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest113-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest113-positive"))

  def test_positive_manifest114(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest114-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest114-positive"))

  def test_positive_manifest115(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest115-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest115-positive"))

  def test_positive_manifest116(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest116-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest116-positive"))

  def test_positive_manifest117(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest117-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest117-positive"))

  def test_positive_manifest118(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest118-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest118-positive"))

  def test_positive_manifest119(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest119-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest119-positive"))

  def test_positive_manifest12(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest12-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest12-positive"))

  def test_positive_manifest120(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest120-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest120-positive"))

  def test_positive_manifest121(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest121-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest121-positive"))

  def test_positive_manifest122(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest122-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest122-positive"))

  def test_positive_manifest123(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest123-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest123-positive"))

  def test_positive_manifest124(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest124-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest124-positive"))

  def test_positive_manifest125(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest125-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest125-positive"))

  def test_positive_manifest126(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest126-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest126-positive"))

  def test_positive_manifest127(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest127-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest127-positive"))

  def test_positive_manifest128(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest128-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest128-positive"))

  def test_positive_manifest129(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest129-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest129-positive"))

  def test_positive_manifest13(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest13-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest13-positive"))

  def test_positive_manifest130(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest130-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest130-positive"))

  def test_positive_manifest131(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest131-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest131-positive"))

  def test_positive_manifest132(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest132-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest132-positive"))

  def test_positive_manifest133(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest133-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest133-positive"))

  def test_positive_manifest134(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest134-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest134-positive"))

  def test_positive_manifest135(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest135-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest135-positive"))

  def test_positive_manifest136(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest136-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest136-positive"))

  def test_positive_manifest137(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest137-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest137-positive"))

  def test_positive_manifest138(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest138-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest138-positive"))

  def test_positive_manifest139(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest139-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest139-positive"))

  def test_positive_manifest14(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest14-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest14-positive"))

  def test_positive_manifest140(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest140-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest140-positive"))

  def test_positive_manifest141(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest141-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest141-positive"))

  def test_positive_manifest142(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest142-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest142-positive"))

  def test_positive_manifest143(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest143-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest143-positive"))

  def test_positive_manifest144(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest144-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest144-positive"))

  def test_positive_manifest145(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest145-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest145-positive"))

  def test_positive_manifest146(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest146-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest146-positive"))

  def test_positive_manifest147(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest147-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest147-positive"))

  def test_positive_manifest148(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest148-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest148-positive"))

  def test_positive_manifest149(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest149-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest149-positive"))

  def test_positive_manifest15(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest15-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest15-positive"))

  def test_positive_manifest150(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest150-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest150-positive"))

  def test_positive_manifest151(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest151-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest151-positive"))

  def test_positive_manifest152(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest152-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest152-positive"))

  def test_positive_manifest153(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest153-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest153-positive"))

  def test_positive_manifest154(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest154-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest154-positive"))

  def test_positive_manifest155(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest155-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest155-positive"))

  def test_positive_manifest156(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest156-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest156-positive"))

  def test_positive_manifest157(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest157-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest157-positive"))

  def test_positive_manifest158(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest158-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest158-positive"))

  def test_positive_manifest159(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest159-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest159-positive"))

  def test_positive_manifest16(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest16-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest16-positive"))

  def test_positive_manifest160(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest160-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest160-positive"))

  def test_positive_manifest161(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest161-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest161-positive"))

  def test_positive_manifest162(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest162-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest162-positive"))

  def test_positive_manifest163(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest163-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest163-positive"))

  def test_positive_manifest164(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest164-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest164-positive"))

  def test_positive_manifest165(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest165-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest165-positive"))

  def test_positive_manifest166(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest166-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest166-positive"))

  def test_positive_manifest167(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest167-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest167-positive"))

  def test_positive_manifest168(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest168-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest168-positive"))

  def test_positive_manifest169(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest169-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest169-positive"))

  def test_positive_manifest17(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest17-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest17-positive"))

  def test_positive_manifest170(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest170-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest170-positive"))

  def test_positive_manifest171(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest171-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest171-positive"))

  def test_positive_manifest172(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest172-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest172-positive"))

  def test_positive_manifest173(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest173-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest173-positive"))

  def test_positive_manifest174(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest174-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest174-positive"))

  def test_positive_manifest175(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest175-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest175-positive"))

  def test_positive_manifest176(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest176-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest176-positive"))

  def test_positive_manifest177(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest177-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest177-positive"))

  def test_positive_manifest178(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest178-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest178-positive"))

  def test_positive_manifest179(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest179-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest179-positive"))

  def test_positive_manifest18(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest18-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest18-positive"))

  def test_positive_manifest180(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest180-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest180-positive"))

  def test_positive_manifest181(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest181-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest181-positive"))

  def test_positive_manifest182(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest182-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest182-positive"))

  def test_positive_manifest183(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest183-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest183-positive"))

  def test_positive_manifest184(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest184-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest184-positive"))

  def test_positive_manifest185(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest185-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest185-positive"))

  def test_positive_manifest186(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest186-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest186-positive"))

  def test_positive_manifest187(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest187-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest187-positive"))

  def test_positive_manifest188(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest188-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest188-positive"))

  def test_positive_manifest189(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest189-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest189-positive"))

  def test_positive_manifest19(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest19-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest19-positive"))

  def test_positive_manifest190(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest190-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest190-positive"))

  def test_positive_manifest191(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest191-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest191-positive"))

  def test_positive_manifest192(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest192-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest192-positive"))

  def test_positive_manifest193(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest193-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest193-positive"))

  def test_positive_manifest194(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest194-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest194-positive"))

  def test_positive_manifest195(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest195-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest195-positive"))

  def test_positive_manifest196(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest196-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest196-positive"))

  def test_positive_manifest197(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest197-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest197-positive"))

  def test_positive_manifest198(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest198-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest198-positive"))

  def test_positive_manifest199(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest199-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest199-positive"))

  def test_positive_manifest2(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest2-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest2-positive"))

  def test_positive_manifest20(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest20-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest20-positive"))

  def test_positive_manifest200(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest200-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest200-positive"))

  def test_positive_manifest201(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest201-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest201-positive"))

  def test_positive_manifest202(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest202-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest202-positive"))

  def test_positive_manifest203(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest203-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest203-positive"))

  def test_positive_manifest204(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest204-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest204-positive"))

  def test_positive_manifest205(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest205-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest205-positive"))

  def test_positive_manifest206(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest206-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest206-positive"))

  def test_positive_manifest207(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest207-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest207-positive"))

  def test_positive_manifest208(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest208-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest208-positive"))

  def test_positive_manifest209(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest209-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest209-positive"))

  def test_positive_manifest21(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest21-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest21-positive"))

  def test_positive_manifest210(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest210-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest210-positive"))

  def test_positive_manifest211(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest211-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest211-positive"))

  def test_positive_manifest212(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest212-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest212-positive"))

  def test_positive_manifest213(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest213-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest213-positive"))

  def test_positive_manifest214(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest214-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest214-positive"))

  def test_positive_manifest215(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest215-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest215-positive"))

  def test_positive_manifest216(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest216-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest216-positive"))

  def test_positive_manifest217(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest217-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest217-positive"))

  def test_positive_manifest218(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest218-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest218-positive"))

  def test_positive_manifest219(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest219-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest219-positive"))

  def test_positive_manifest22(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest22-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest22-positive"))

  def test_positive_manifest220(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest220-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest220-positive"))

  def test_positive_manifest221(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest221-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest221-positive"))

  def test_positive_manifest222(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest222-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest222-positive"))

  def test_positive_manifest223(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest223-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest223-positive"))

  def test_positive_manifest224(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest224-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest224-positive"))

  def test_positive_manifest225(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest225-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest225-positive"))

  def test_positive_manifest226(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest226-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest226-positive"))

  def test_positive_manifest227(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest227-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest227-positive"))

  def test_positive_manifest228(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest228-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest228-positive"))

  def test_positive_manifest229(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest229-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest229-positive"))

  def test_positive_manifest23(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest23-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest23-positive"))

  def test_positive_manifest230(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest230-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest230-positive"))

  def test_positive_manifest231(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest231-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest231-positive"))

  def test_positive_manifest232(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest232-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest232-positive"))

  def test_positive_manifest233(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest233-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest233-positive"))

  def test_positive_manifest234(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest234-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest234-positive"))

  def test_positive_manifest235(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest235-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest235-positive"))

  def test_positive_manifest236(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest236-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest236-positive"))

  def test_positive_manifest237(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest237-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest237-positive"))

  def test_positive_manifest238(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest238-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest238-positive"))

  def test_positive_manifest239(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest239-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest239-positive"))

  def test_positive_manifest24(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest24-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest24-positive"))

  def test_positive_manifest240(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest240-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest240-positive"))

  def test_positive_manifest241(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest241-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest241-positive"))

  def test_positive_manifest242(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest242-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest242-positive"))

  def test_positive_manifest243(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest243-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest243-positive"))

  def test_positive_manifest244(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest244-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest244-positive"))

  def test_positive_manifest245(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest245-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest245-positive"))

  def test_positive_manifest246(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest246-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest246-positive"))

  def test_positive_manifest247(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest247-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest247-positive"))

  def test_positive_manifest248(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest248-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest248-positive"))

  def test_positive_manifest249(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest249-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest249-positive"))

  def test_positive_manifest25(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest25-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest25-positive"))

  def test_positive_manifest250(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest250-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest250-positive"))

  def test_positive_manifest251(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest251-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest251-positive"))

  def test_positive_manifest252(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest252-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest252-positive"))

  def test_positive_manifest253(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest253-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest253-positive"))

  def test_positive_manifest254(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest254-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest254-positive"))

  def test_positive_manifest255(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest255-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest255-positive"))

  def test_positive_manifest256(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest256-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest256-positive"))

  def test_positive_manifest257(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest257-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest257-positive"))

  def test_positive_manifest258(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest258-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest258-positive"))

  def test_positive_manifest259(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest259-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest259-positive"))

  def test_positive_manifest26(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest26-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest26-positive"))

  def test_positive_manifest260(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest260-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest260-positive"))

  def test_positive_manifest261(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest261-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest261-positive"))

  def test_positive_manifest262(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest262-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest262-positive"))

  def test_positive_manifest263(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest263-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest263-positive"))

  def test_negative_manifest264(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest264-negative", "/opt/wrt-manifest-android-tests/apks/x86/manifest264-negative"))

  def test_negative_manifest265(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest265-negative", "/opt/wrt-manifest-android-tests/apks/x86/manifest265-negative"))

  def test_negative_manifest266(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest266-negative", "/opt/wrt-manifest-android-tests/apks/x86/manifest266-negative"))

  def test_positive_manifest27(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest27-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest27-positive"))

  def test_positive_manifest28(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest28-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest28-positive"))

  def test_positive_manifest29(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest29-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest29-positive"))

  def test_positive_manifest3(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest3-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest3-positive"))

  def test_positive_manifest30(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest30-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest30-positive"))

  def test_positive_manifest31(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest31-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest31-positive"))

  def test_positive_manifest32(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest32-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest32-positive"))

  def test_positive_manifest33(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest33-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest33-positive"))

  def test_positive_manifest34(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest34-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest34-positive"))

  def test_positive_manifest35(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest35-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest35-positive"))

  def test_positive_manifest36(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest36-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest36-positive"))

  def test_positive_manifest37(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest37-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest37-positive"))

  def test_positive_manifest38(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest38-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest38-positive"))

  def test_positive_manifest39(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest39-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest39-positive"))

  def test_positive_manifest4(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest4-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest4-positive"))

  def test_positive_manifest40(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest40-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest40-positive"))

  def test_positive_manifest41(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest41-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest41-positive"))

  def test_positive_manifest42(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest42-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest42-positive"))

  def test_positive_manifest43(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest43-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest43-positive"))

  def test_positive_manifest44(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest44-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest44-positive"))

  def test_positive_manifest45(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest45-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest45-positive"))

  def test_positive_manifest46(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest46-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest46-positive"))

  def test_positive_manifest47(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest47-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest47-positive"))

  def test_positive_manifest48(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest48-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest48-positive"))

  def test_positive_manifest49(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest49-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest49-positive"))

  def test_positive_manifest5(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest5-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest5-positive"))

  def test_positive_manifest50(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest50-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest50-positive"))

  def test_positive_manifest51(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest51-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest51-positive"))

  def test_positive_manifest52(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest52-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest52-positive"))

  def test_positive_manifest53(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest53-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest53-positive"))

  def test_positive_manifest54(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest54-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest54-positive"))

  def test_positive_manifest55(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest55-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest55-positive"))

  def test_positive_manifest56(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest56-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest56-positive"))

  def test_positive_manifest57(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest57-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest57-positive"))

  def test_positive_manifest58(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest58-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest58-positive"))

  def test_positive_manifest59(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest59-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest59-positive"))

  def test_positive_manifest6(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest6-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest6-positive"))

  def test_positive_manifest60(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest60-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest60-positive"))

  def test_positive_manifest61(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest61-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest61-positive"))

  def test_positive_manifest62(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest62-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest62-positive"))

  def test_positive_manifest63(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest63-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest63-positive"))

  def test_positive_manifest64(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest64-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest64-positive"))

  def test_positive_manifest65(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest65-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest65-positive"))

  def test_positive_manifest66(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest66-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest66-positive"))

  def test_positive_manifest67(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest67-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest67-positive"))

  def test_positive_manifest68(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest68-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest68-positive"))

  def test_positive_manifest69(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest69-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest69-positive"))

  def test_positive_manifest7(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest7-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest7-positive"))

  def test_positive_manifest70(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest70-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest70-positive"))

  def test_positive_manifest71(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest71-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest71-positive"))

  def test_positive_manifest72(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest72-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest72-positive"))

  def test_positive_manifest73(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest73-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest73-positive"))

  def test_positive_manifest74(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest74-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest74-positive"))

  def test_positive_manifest75(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest75-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest75-positive"))

  def test_positive_manifest76(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest76-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest76-positive"))

  def test_positive_manifest77(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest77-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest77-positive"))

  def test_positive_manifest78(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest78-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest78-positive"))

  def test_positive_manifest79(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest79-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest79-positive"))

  def test_positive_manifest8(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest8-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest8-positive"))

  def test_positive_manifest80(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest80-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest80-positive"))

  def test_positive_manifest81(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest81-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest81-positive"))

  def test_positive_manifest82(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest82-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest82-positive"))

  def test_positive_manifest83(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest83-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest83-positive"))

  def test_positive_manifest84(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest84-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest84-positive"))

  def test_positive_manifest85(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest85-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest85-positive"))

  def test_positive_manifest86(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest86-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest86-positive"))

  def test_positive_manifest87(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest87-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest87-positive"))

  def test_positive_manifest88(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest88-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest88-positive"))

  def test_positive_manifest89(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest89-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest89-positive"))

  def test_positive_manifest9(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest9-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest9-positive"))

  def test_positive_manifest90(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest90-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest90-positive"))

  def test_positive_manifest91(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest91-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest91-positive"))

  def test_positive_manifest92(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest92-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest92-positive"))

  def test_positive_manifest93(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest93-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest93-positive"))

  def test_positive_manifest94(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest94-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest94-positive"))

  def test_positive_manifest95(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest95-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest95-positive"))

  def test_positive_manifest96(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest96-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest96-positive"))

  def test_positive_manifest97(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest97-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest97-positive"))

  def test_positive_manifest98(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest98-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest98-positive"))

  def test_positive_manifest99(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest99-positive", "/opt/wrt-manifest-android-tests/apks/x86/manifest99-positive"))

if __name__ == '__main__':
    unittest.main()