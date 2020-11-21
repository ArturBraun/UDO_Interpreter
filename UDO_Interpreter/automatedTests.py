import unittest
import difflib
import os

from UDO_Interpreter import doTestParsing, doParsing


def testGeneratedFiles(projectName):
    """
    Tests files that are generated during interpreting UDO script for corectness with proper files.
    """
    udoFilePath = "..\\tests\\" + projectName + "\\"
    udoFileName = projectName + ".udo"
    pathToGeneratePyFiles = "..\\tests\\automatedTests\\"
    testProjectName = "tmpTest"

    doParsing(debug = False, interpreter_debug = False, showDotFile = False, UDO_FilePath = udoFilePath + udoFileName,
        pathToGeneratePyFiles = pathToGeneratePyFiles, printMessages = False)

    generatedFilesNamesEnding = [
        "",
        "_circuit",
        "_excit",
        "_geom_media",
        "_mesh",
        "_ppost",
        "_proj",
        "_runsimul",
        "_setsimul"
        ]

    correctFiles = []
    generatedFiles = []

    for i in range(len(generatedFilesNamesEnding)):
        correctFilePath = udoFilePath + projectName + generatedFilesNamesEnding[i] + ".py"
        generatedFilePath = pathToGeneratePyFiles + projectName + generatedFilesNamesEnding[i] + ".py"

        with open(correctFilePath, "r") as file:
            data = file.read()
            correctFiles.append(data)

        with open(generatedFilePath, "r") as file:
            data = file.read()
            generatedFiles.append(data)

    resultsAreCorrect = True

    for i in range(len(correctFiles)):
        if correctFiles[i] != generatedFiles[i]:
            incorrectFileName = projectName + generatedFilesNamesEnding[i] + "\n"
            spacing = "="*50 + "\n"
            print(spacing + incorrectFileName + spacing)
            diff = difflib.ndiff(correctFiles[i].splitlines(keepends=True),
                        generatedFiles[i].splitlines(keepends=True))
            print(''.join(diff), end="")
            print(spacing + "\n")

            resultsAreCorrect = False

        properFileName = pathToGeneratePyFiles + testProjectName + generatedFilesNamesEnding[i] + ".py"
        if os.path.exists(properFileName):
            os.remove(properFileName)
        os.rename(pathToGeneratePyFiles + projectName + generatedFilesNamesEnding[i] + ".py", properFileName)

    return resultsAreCorrect


class TestsUdoInterpreter(unittest.TestCase):
    """
    Tests Udo Interpreter for simple mathematical equasions and simple loop, if statements etc.
    Checks also generated files corectness.
    """

    # dielf1, cwgheat, rx, threeel, rt2w

    def test_angpc(self):
        print("\nTest of -> angpc")
        result = testGeneratedFiles("angpc")
        self.assertEqual(result, True)

    def test_cube(self):
        print("Test of -> cube")
        result = testGeneratedFiles("cube")
        self.assertEqual(result, True)

    def test_cubeNested(self):
        print("Test of -> cubeNested")
        result = testGeneratedFiles("cubeNested")
        self.assertEqual(result, True)

    def test_cubeNNN(self):
        print("Test of -> cubeNNN")
        result = testGeneratedFiles("cubeNNN")
        self.assertEqual(result, True)

    def test_cylinder(self):
        print("Test of -> cylinder")
        result = testGeneratedFiles("cylinder")
        self.assertEqual(result, True)

    def test_cyv(self):
        print("Test of -> cyv")
        result = testGeneratedFiles("cyv")
        self.assertEqual(result, True)

    def test_cyvr(self):
        print("Test of -> cyvr")
        result = testGeneratedFiles("cyvr")
        self.assertEqual(result, True)

    def test_horn1(self):
        print("Test of -> horn1")
        result = testGeneratedFiles("horn1")
        self.assertEqual(result, True)

    def test_patch2(self):
        print("Test of -> patch2")
        result = testGeneratedFiles("patch2")
        self.assertEqual(result, True)

    def test_rt2w(self):
        print("Test of -> rt2w")
        result = testGeneratedFiles("rt2w")
        self.assertEqual(result, True)

    def test_rx(self):
        print("Test of -> rx")
        result = testGeneratedFiles("rx")
        self.assertEqual(result, True)

    def test_threeel(self):
        print("Test of -> threeel")
        result = testGeneratedFiles("threeel")
        self.assertEqual(result, True)

    def test_tv(self):
        print("Test of -> tv")
        result = testGeneratedFiles("tv")
        self.assertEqual(result, True)

    def test_vtape(self):
        print("Test of -> vtape")
        result = testGeneratedFiles("vtape")
        self.assertEqual(result, True)

    def test_wgtocx1(self):
        print("Test of -> wgtcox1")
        result = testGeneratedFiles("wgtocx1")
        self.assertEqual(result, True)

    # UDO language unit tests

    def test1(self):
        udoFileStr = """a = 2*cos(0); 
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 2)

    def test2(self):
        udoFileStr = """a = "abc";
                        b = "cde";
                        c = a @ "111" @ b;
                        c"""
        self.assertEqual(doTestParsing(udoFileStr), "abc111cde")

    def test3(self):
        udoFileStr = """a = 2;
                        a = 2 * a * 2;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 8)

    def test4(self):
        udoFileStr = """a = -(2*10+2^3-4/(8-6));
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), -26)

    def test5(self):
        udoFileStr = """a = 2;
                        a = a * a;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 4)

    def test6(self):
        udoFileStr = """a = 2;
                        a = -a * a;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), -4)

    def test7(self):
        udoFileStr = """a = 2;
                        if a < 5 do a = 10; endif;
                        a = -a * a;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), -100)

    def test8(self):
        udoFileStr = """a = 2;
                        if a > 5 do a = 10; endif;
                        a = -a * a;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), -4)

    def test9(self):
        udoFileStr = """a = 0;
                        while a < 10 do
                            a++;
                        endwhile;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 10)

    def test10(self):
        udoFileStr = """a = 0;
                        b = 15;
                        while (a < 10) && (b > 11) do
                            a++;
                            b = b - 1;
                        endwhile;
                        b"""
        self.assertEqual(doTestParsing(udoFileStr), 11)

    def test11(self):
        udoFileStr = """a = 2;
                        b = 3;
                        a = a * b;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 6)

    def test12(self):
        udoFileStr = """a = 2;
                        b = 3;
                        c = 4;
                        d = 5;
                        a = a * b * c * d;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 2*3*4*5)

    def test13(self):
        udoFileStr = """a = 2.5*(cos(5.5)^2 + sin(5.5)^2); 
                        b = abs(a - 2.5);
                        c = b < 0.000000001;
                        c"""
        self.assertEqual(doTestParsing(udoFileStr), 1)

    def test14(self):
        udoFileStr = """x = 30;
                        a = (2*tan(x)) / (1 - tan(x)^2);
                        b = (2*sin(x)*cos(x)) / (1 - 2*sin(x)^2);
                        c = abs(a - b);
                        d = c < 0.000000001;
                        d"""
        self.assertEqual(doTestParsing(udoFileStr), 1)

    def test15(self):
        udoFileStr = """a = 1;
                        b = 0;
                        x = ((a || b) && (a && b)) || (a >= b);
                        x"""
        self.assertEqual(doTestParsing(udoFileStr), 1)

    def test16(self):
        udoFileStr = """a = 1;
                        b = 0;
                        x = ((a == b) || (b > a) || ((a+b) > b)) && b;
                        x"""
        self.assertEqual(doTestParsing(udoFileStr), 0)

    def test17(self):
        udoFileStr = """a = "abc";
                        b = "cde";
                        c = a @ b;
                        c"""
        self.assertEqual(doTestParsing(udoFileStr), "abccde")

    def test18(self):
        udoFileStr = """a = "abc";
                        c = "1a1a" @ a;
                        c"""
        self.assertEqual(doTestParsing(udoFileStr), "1a1aabc")

    def test19(self):
        udoFileStr = """a = "abc";
                        c = a @ "1a1a";
                        c"""
        self.assertEqual(doTestParsing(udoFileStr), "abc1a1a")

    def test20(self):
        udoFileStr = """c = "2222bbbb" @ "1a1a";
                        c"""
        self.assertEqual(doTestParsing(udoFileStr), "2222bbbb1a1a")

    def test21(self):
        udoFileStr = """a = "a";
                        b = "b";
                        d = "d";
                        c = a @ b @ "111" @ d @ "111";
                        c"""
        self.assertEqual(doTestParsing(udoFileStr), "ab111d111")

    def test22(self):
        udoFileStr = """str = "abc";
                        a = 2;
                        if str do a = 10; endif;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 10)

    def test23(self):
        udoFileStr = """str = "";
                        a = 2;
                        if str do a = 10; endif;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 2)

    def test24(self):
        udoFileStr = """a = 0;
                        if a do a = 10; endif;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 0)

    def test25(self):
        udoFileStr = """a = "str";
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), "str")

    def test26(self):
        udoFileStr = """a = abs(2 - 2.5) < 1;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 1)

    def test27(self):
        udoFileStr = """a = sin(90) + cos(0.0) <= 1 + 1;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 1)

    def test28(self):
        udoFileStr = """a = sqrt(4) < 1;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 0)

    def test29(self):
        udoFileStr = """a = 0;
                        if a > 1 do 
                            if a > 2 do
                                a = 10; 
                            endif;
                        endif;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 0)

    def test30(self):
        udoFileStr = """a = 3;
                        if a > 1 do 
                            if a > 2 do
                                a = 10; 
                            endif;
                        endif;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 10)

    def test31(self):
        udoFileStr = """a = 10;
                        b = 10;
                        while a > 0 do 
                            a--;
                            while b < 20 do
                                b++;
                            endwhile;
                        endwhile;
                        b"""
        self.assertEqual(doTestParsing(udoFileStr), 20)

    def test32(self):
        udoFileStr = """a = 0;
                        b = 0;
                        c = 0;
                        while a < 10 do 
                            a++;
                            while (b < 10) && (b != 5) do
                                b++;
                                while c < 10 do
                                    c = c + 1;
                                endwhile;
                            endwhile;
                        endwhile;
                        b"""
        self.assertEqual(doTestParsing(udoFileStr), 5)

    def test33(self):
        udoFileStr = """a = 2;
                        if (a < 5) || (a > 1) do a = 10; endif;
                        a = -a * a;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), -100)

    def test34(self):
        udoFileStr = """a = 0;
                        if a do a = 10; endif;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 0)

    def test35(self):
        udoFileStr = """b = 5;
                        a = (b < 10) && (b != 5);
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 0)

    def test36(self):
        udoFileStr = """a = 0;
                        while a < 10 do
	                        ADDLINE(2, 5); 
                            a++;
                        endwhile;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 10)

    def test37(self):
        udoFileStr = """a = .2;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 0.2)

    def test38(self):
        udoFileStr = """a = 2;
                        if a > 1 || a < 0 do
                            a = 5;
                        endif;
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 5)
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()


