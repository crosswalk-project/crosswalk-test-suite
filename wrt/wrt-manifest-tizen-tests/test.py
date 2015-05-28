#!/usr/bin/env python
# coding=utf-8
import random
import os
import sys
import unittest
import run_test
import codecs
reload(sys)
sys.setdefaultencoding("utf-8")


class TestCaseUnit(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check1",
                " birds"))

    def test_case_2(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check2",
                "Angrybirds"))

    def test_case_3(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check3",
                "123456birds"))

    def test_case_4(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check4",
                "_a-bbirds"))

    def test_case_5(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check5",
                "<>birds"))

    def test_case_6(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check6",
                ".CAPITALbirds"))

    def test_case_7(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check7",
                "\nbirds"))

    def test_case_8(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check8",
                "*&^%!@#$%^&*()birds"))

    def test_case_9(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check9",
                "+-birds"))

    def test_case_10(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check10",
                "'birds"))

    def test_case_11(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check11",
                "中文birds"))

    def test_case_12(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check12",
                "中文 "))

    def test_case_13(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check13",
                "' "))

    def test_case_14(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check14",
                "+- "))

    def test_case_15(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check15",
                "*&^%!@#$%^&*() "))

    def test_case_16(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check16",
                "\n "))

    def test_case_17(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check17",
                ".CAPITAL "))

    def test_case_18(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check18",
                "<> "))

    def test_case_19(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check19",
                "_a-b "))

    def test_case_20(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check20",
                "123456 "))

    def test_case_21(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check21",
                "Angry "))

    def test_case_22(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check22",
                "  "))

    def test_case_23(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check23",
                " a b"))

    def test_case_24(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check24",
                "Angrya b"))

    def test_case_25(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check25",
                "123456a b"))

    def test_case_26(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check26",
                "_a-ba b"))

    def test_case_27(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check27",
                "<>a b"))

    def test_case_28(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check28",
                ".CAPITALa b"))

    def test_case_29(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check29",
                "\na b"))

    def test_case_30(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check30",
                "*&^%!@#$%^&*()a b"))

    def test_case_31(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check31",
                "+-a b"))

    def test_case_32(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check32",
                "'a b"))

    def test_case_33(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check33",
                "中文a b"))

    def test_case_34(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check34",
                "中文b "))

    def test_case_35(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check35",
                "'b "))

    def test_case_36(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check36",
                "+-b "))

    def test_case_37(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check37",
                "*&^%!@#$%^&*()b "))

    def test_case_38(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check38",
                "\nb "))

    def test_case_39(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check39",
                ".CAPITALb "))

    def test_case_40(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check40",
                "<>b "))

    def test_case_41(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check41",
                "_a-bb "))

    def test_case_42(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check42",
                "123456b "))

    def test_case_43(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check43",
                "Angryb "))

    def test_case_44(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check44",
                " b "))

    def test_case_45(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check45",
                " BIRDS."))

    def test_case_46(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check46",
                "AngryBIRDS."))

    def test_case_47(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check47",
                "123456BIRDS."))

    def test_case_48(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check48",
                "_a-bBIRDS."))

    def test_case_49(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check49",
                "<>BIRDS."))

    def test_case_50(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check50",
                ".CAPITALBIRDS."))

    def test_case_51(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check51",
                "\nBIRDS."))

    def test_case_52(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check52",
                "*&^%!@#$%^&*()BIRDS."))

    def test_case_53(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check53",
                "+-BIRDS."))

    def test_case_54(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check54",
                "'BIRDS."))

    def test_case_55(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check55",
                "中文BIRDS."))

    def test_case_56(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check56",
                "中文asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_57(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check57",
                "'asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_58(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check58",
                "+-asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_59(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check59",
                "*&^%!@#$%^&*()asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_60(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check60",
                "\nasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_61(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check61",
                ".CAPITALasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_62(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check62",
                "<>asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_63(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check63",
                "_a-basdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_64(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check64",
                "123456asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_65(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check65",
                "Angryasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_66(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check66",
                " asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_67(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check67",
                " asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_68(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check68",
                "Angryasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_69(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check69",
                "123456asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_70(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check70",
                "_a-basdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_71(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check71",
                "<>asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_72(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check72",
                ".CAPITALasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_73(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check73",
                "\nasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_74(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check74",
                "*&^%!@#$%^&*()asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_75(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check75",
                "+-asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_76(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check76",
                "'asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_77(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check77",
                "中文asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_78(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check78",
                "中文BIRDS."))

    def test_case_79(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check79",
                "'BIRDS."))

    def test_case_80(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check80",
                "+-BIRDS."))

    def test_case_81(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check81",
                "*&^%!@#$%^&*()BIRDS."))

    def test_case_82(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check82",
                "\nBIRDS."))

    def test_case_83(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check83",
                ".CAPITALBIRDS."))

    def test_case_84(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check84",
                "<>BIRDS."))

    def test_case_85(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check85",
                "_a-bBIRDS."))

    def test_case_86(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check86",
                "123456BIRDS."))

    def test_case_87(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check87",
                "AngryBIRDS."))

    def test_case_88(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check88",
                " BIRDS."))

    def test_case_89(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check89",
                " b "))

    def test_case_90(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check90",
                "Angryb "))

    def test_case_91(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check91",
                "123456b "))

    def test_case_92(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check92",
                "_a-bb "))

    def test_case_93(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check93",
                "<>b "))

    def test_case_94(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check94",
                ".CAPITALb "))

    def test_case_95(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check95",
                "\nb "))

    def test_case_96(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check96",
                "*&^%!@#$%^&*()b "))

    def test_case_97(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check97",
                "+-b "))

    def test_case_98(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check98",
                "'b "))

    def test_case_99(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check99",
                "中文b "))

    def test_case_100(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check100",
                "中文a b"))

    def test_case_101(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check101",
                "'a b"))

    def test_case_102(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check102",
                "+-a b"))

    def test_case_103(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check103",
                "*&^%!@#$%^&*()a b"))

    def test_case_104(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check104",
                "\na b"))

    def test_case_105(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check105",
                ".CAPITALa b"))

    def test_case_106(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check106",
                "<>a b"))

    def test_case_107(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check107",
                "_a-ba b"))

    def test_case_108(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check108",
                "123456a b"))

    def test_case_109(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check109",
                "Angrya b"))

    def test_case_110(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check110",
                " a b"))

    def test_case_111(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check111",
                "  "))

    def test_case_112(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check112",
                "Angry "))

    def test_case_113(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check113",
                "123456 "))

    def test_case_114(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check114",
                "_a-b "))

    def test_case_115(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check115",
                "<> "))

    def test_case_116(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check116",
                ".CAPITAL "))

    def test_case_117(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check117",
                "\n "))

    def test_case_118(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check118",
                "*&^%!@#$%^&*() "))

    def test_case_119(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check119",
                "+- "))

    def test_case_120(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check120",
                "' "))

    def test_case_121(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check121",
                "中文 "))

    def test_case_122(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check122",
                "中文birds"))

    def test_case_123(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check123",
                "'birds"))

    def test_case_124(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check124",
                "+-birds"))

    def test_case_125(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check125",
                "*&^%!@#$%^&*()birds"))

    def test_case_126(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check126",
                "\nbirds"))

    def test_case_127(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check127",
                ".CAPITALbirds"))

    def test_case_128(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check128",
                "<>birds"))

    def test_case_129(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check129",
                "_a-bbirds"))

    def test_case_130(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check130",
                "123456birds"))

    def test_case_131(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check131",
                "Angrybirds"))

    def test_case_132(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check132",
                " birds"))

    def test_case_133(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check133",
                " birds"))

    def test_case_134(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check134",
                "Angrybirds"))

    def test_case_135(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check135",
                "123456birds"))

    def test_case_136(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check136",
                "_a-bbirds"))

    def test_case_137(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check137",
                "<>birds"))

    def test_case_138(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check138",
                ".CAPITALbirds"))

    def test_case_139(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check139",
                "\nbirds"))

    def test_case_140(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check140",
                "*&^%!@#$%^&*()birds"))

    def test_case_141(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check141",
                "+-birds"))

    def test_case_142(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check142",
                "'birds"))

    def test_case_143(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check143",
                "中文birds"))

    def test_case_144(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check144",
                "中文 "))

    def test_case_145(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check145",
                "' "))

    def test_case_146(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check146",
                "+- "))

    def test_case_147(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check147",
                "*&^%!@#$%^&*() "))

    def test_case_148(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check148",
                "\n "))

    def test_case_149(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check149",
                ".CAPITAL "))

    def test_case_150(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check150",
                "<> "))

    def test_case_151(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check151",
                "_a-b "))

    def test_case_152(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check152",
                "123456 "))

    def test_case_153(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check153",
                "Angry "))

    def test_case_154(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check154",
                "  "))

    def test_case_155(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check155",
                " a b"))

    def test_case_156(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check156",
                "Angrya b"))

    def test_case_157(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check157",
                "123456a b"))

    def test_case_158(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check158",
                "_a-ba b"))

    def test_case_159(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check159",
                "<>a b"))

    def test_case_160(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check160",
                ".CAPITALa b"))

    def test_case_161(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check161",
                "\na b"))

    def test_case_162(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check162",
                "*&^%!@#$%^&*()a b"))

    def test_case_163(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check163",
                "+-a b"))

    def test_case_164(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check164",
                "'a b"))

    def test_case_165(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check165",
                "中文a b"))

    def test_case_166(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check166",
                "中文b "))

    def test_case_167(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check167",
                "'b "))

    def test_case_168(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check168",
                "+-b "))

    def test_case_169(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check169",
                "*&^%!@#$%^&*()b "))

    def test_case_170(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check170",
                "\nb "))

    def test_case_171(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check171",
                ".CAPITALb "))

    def test_case_172(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check172",
                "<>b "))

    def test_case_173(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check173",
                "_a-bb "))

    def test_case_174(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check174",
                "123456b "))

    def test_case_175(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check175",
                "Angryb "))

    def test_case_176(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check176",
                " b "))

    def test_case_177(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check177",
                " BIRDS."))

    def test_case_178(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check178",
                "AngryBIRDS."))

    def test_case_179(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check179",
                "123456BIRDS."))

    def test_case_180(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check180",
                "_a-bBIRDS."))

    def test_case_181(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check181",
                "<>BIRDS."))

    def test_case_182(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check182",
                ".CAPITALBIRDS."))

    def test_case_183(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check183",
                "\nBIRDS."))

    def test_case_184(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check184",
                "*&^%!@#$%^&*()BIRDS."))

    def test_case_185(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check185",
                "+-BIRDS."))

    def test_case_186(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check186",
                "'BIRDS."))

    def test_case_187(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check187",
                "中文BIRDS."))

    def test_case_188(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check188",
                "中文asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_189(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check189",
                "'asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_190(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check190",
                "+-asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_191(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check191",
                "*&^%!@#$%^&*()asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_192(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check192",
                "\nasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_193(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check193",
                ".CAPITALasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_194(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check194",
                "<>asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_195(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check195",
                "_a-basdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_196(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check196",
                "123456asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_197(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check197",
                "Angryasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_198(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check198",
                " asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_199(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check199",
                " asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_200(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check200",
                "Angryasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_201(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check201",
                "123456asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_202(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check202",
                "_a-basdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_203(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check203",
                "<>asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_204(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check204",
                ".CAPITALasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_205(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check205",
                "\nasdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_206(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check206",
                "*&^%!@#$%^&*()asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_207(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check207",
                "+-asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_208(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check208",
                "'asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_209(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check209",
                "中文asdfasdfasdfasdfdfghfggfhjhjerewrtrtyyuivghxvasdaetsdfgxcvbrtysadawfasdfasdewrtwer"))

    def test_case_210(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check210",
                "中文BIRDS."))

    def test_case_211(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check211",
                "'BIRDS."))

    def test_case_212(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check212",
                "+-BIRDS."))

    def test_case_213(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check213",
                "*&^%!@#$%^&*()BIRDS."))

    def test_case_214(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check214",
                "\nBIRDS."))

    def test_case_215(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check215",
                ".CAPITALBIRDS."))

    def test_case_216(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check216",
                "<>BIRDS."))

    def test_case_217(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check217",
                "_a-bBIRDS."))

    def test_case_218(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check218",
                "123456BIRDS."))

    def test_case_219(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check219",
                "AngryBIRDS."))

    def test_case_220(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check220",
                " BIRDS."))

    def test_case_221(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check221",
                " b "))

    def test_case_222(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check222",
                "Angryb "))

    def test_case_223(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check223",
                "123456b "))

    def test_case_224(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check224",
                "_a-bb "))

    def test_case_225(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check225",
                "<>b "))

    def test_case_226(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check226",
                ".CAPITALb "))

    def test_case_227(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check227",
                "\nb "))

    def test_case_228(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check228",
                "*&^%!@#$%^&*()b "))

    def test_case_229(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check229",
                "+-b "))

    def test_case_230(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check230",
                "'b "))

    def test_case_231(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check231",
                "中文b "))

    def test_case_232(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check232",
                "中文a b"))

    def test_case_233(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check233",
                "'a b"))

    def test_case_234(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check234",
                "+-a b"))

    def test_case_235(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check235",
                "*&^%!@#$%^&*()a b"))

    def test_case_236(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check236",
                "\na b"))

    def test_case_237(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check237",
                ".CAPITALa b"))

    def test_case_238(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check238",
                "<>a b"))

    def test_case_239(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check239",
                "_a-ba b"))

    def test_case_240(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check240",
                "123456a b"))

    def test_case_241(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check241",
                "Angrya b"))

    def test_case_242(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check242",
                " a b"))

    def test_case_243(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check243",
                "  "))

    def test_case_244(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check244",
                "Angry "))

    def test_case_245(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check245",
                "123456 "))

    def test_case_246(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check246",
                "_a-b "))

    def test_case_247(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check247",
                "<> "))

    def test_case_248(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check248",
                ".CAPITAL "))

    def test_case_249(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check249",
                "\n "))

    def test_case_250(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check250",
                "*&^%!@#$%^&*() "))

    def test_case_251(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check251",
                "+- "))

    def test_case_252(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check252",
                "' "))

    def test_case_253(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check253",
                "中文 "))

    def test_case_254(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check254",
                "中文birds"))

    def test_case_255(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check255",
                "'birds"))

    def test_case_256(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check256",
                "+-birds"))

    def test_case_257(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check257",
                "*&^%!@#$%^&*()birds"))

    def test_case_258(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check258",
                "\nbirds"))

    def test_case_259(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check259",
                ".CAPITALbirds"))

    def test_case_260(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check260",
                "<>birds"))

    def test_case_261(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check261",
                "_a-bbirds"))

    def test_case_262(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check262",
                "123456birds"))

    def test_case_263(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check263",
                "Angrybirds"))

    def test_case_264(self):
        self.assertEqual(
            "Pass",
            run_test.run_test_result(
                "Crosswalk-Manifest-Check264",
                " birds"))

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseUnit)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)
