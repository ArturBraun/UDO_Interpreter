import unittest
from UDO_Interpreter import doTestParsing


# TODO:
# - dopisac testy automatyczne dla sprawdzania poprawnosci generowanych plikow !!!


class TestsUdoInterpreter(unittest.TestCase):
    """
    Tests Udo Interpreter for simple mathematical equasions and simple loop, if statements etc.
    """
    def test1(self):
        udoFileStr = """a = 2*cos(0); 
                        a"""
        self.assertEqual(doTestParsing(udoFileStr), 2)

    #def test2(self):
    #    udoFileStr = """a = "abc";
    #                    b = "cde";
    #                    c = a @ "111" @ b;
    #                    c"""
    #    self.assertEqual(doTestParsing(udoFileStr), "abc111cde")

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

    #def test17(self):
    #    udoFileStr = """a = abs(2 - 2.5) < 1;
    #                    a"""
    #    self.assertEqual(doTestParsing(udoFileStr), 1)

def main():
    unittest.main()

if __name__ == '__main__':
    main()


