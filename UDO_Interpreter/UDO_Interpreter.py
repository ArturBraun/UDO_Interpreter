#--------------------------------------------
""" INCLUDED MODULES: """
#--------------------------------------------
from arpeggio import *
from arpeggio import RegExMatch as apperggioRegEx
from arpeggio.export import PTDOTExporter
from graphviz import Source

#--------------------------------------------
""" GRAMMAR FUNCTIONS: """
#--------------------------------------------
def number():
    return apperggioRegEx(r'\d+\.\d+|\d+') 
# Sprawdzic czy wedlug UDO .2 to tez liczba
# Aktualnie dziala tylko dla liczb normalnych typu 0.2 itd.

def withSign():
    return Optional(["+","-"]),[number,("(", expression, ")")]

def power():
    return withSign, ZeroOrMore(["^"], withSign)

def multiplicationOrDivision():
    return power, ZeroOrMore(["*","/"], power)

def expression():
    return multiplicationOrDivision, ZeroOrMore(["+","-"], multiplicationOrDivision)

def calc(): 
    return OneOrMore(expression), EOF


#--------------------------------------------
""" CLASSES AND MAIN FUNCTION: """
#--------------------------------------------

class GrammarRulesVisitor(PTNodeVisitor):
    def visit_number(self, node, children):
        """
        Converts Node value to float
        """
        if self.debug:
            print("Converting {}.".format(node.value))
        return float(node.value)
    
    def visit_withSign(self, node, children):
        """
        Applies a sign to expression or number
        """
        if self.debug:
            print("NumberWithSign {}.".format(children))
        if len(children) == 1:
            return children[0]
        sign = -1 if children[0] == "-" else 1
        return sign * children[-1]

    def visit_power(self, node, children):
        """
        Raises number to Power
        """
        if self.debug:
            print("Power {}.".format(children))
        power = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "^":
                power **= children[i]
        if self.debug:
            print("Power = {}.".format(power))
        return power
    
    def visit_multiplicationOrDivision(self, node, children):
        """
        Divides or Multiplies number
        """
        if self.debug:
            print("MultiplicationOrDivision {}.".format(children))
        multiplicationOrDivision = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "*":
                multiplicationOrDivision *= children[i]
            elif children[i-1] == "/":
                multiplicationOrDivision /= children[i]
        if self.debug:
            print("MultiplicationOrDivision = {}.".format(multiplicationOrDivision))
        return multiplicationOrDivision

    def visit_expression(self, node, children):
        """
        Adds or substracts numbers.
        """
        if self.debug:
            print("Expression {}.".format(children))
        expression = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "-":
                expression -= children[i]
            elif children[i-1] == "+":
                expression += children[i]
        if self.debug:
            print("Expression = {}.".format(expression))
        return expression


def doParsing(debug = False, showDotFile = False, UDO_FilePath = ""):
    print("UDO Interpreter")
    
    if UDO_FilePath:
        try:
            UDO_File = open(UDO_FilePath)

        except FileNotFoundError:
            print("Error -> Cannot find the file in given directory!")

        else:
            UDO_FileContent = UDO_File.read()

            parser = ParserPython(calc, debug=debug)
            parse_tree = parser.parse(UDO_FileContent)
            result = visit_parse_tree(parse_tree,GrammarRulesVisitor(debug=debug))

            inputExprValue = -(-3*2**2)*4-5**2*6-8*(2-3**2)*2**2+(-2-3**2)**2*2**3

            print("{} = {}".format("Python value","Calculated result from parser"))
            print("{} = {}".format(inputExprValue,result))

            if showDotFile:
                PTDOTExporter().exportFile(parse_tree,"UDO_InterpreterParseTree.dot")    
                s = Source.from_file("UDO_InterpreterParseTree.dot")
                s.view()

        finally:
            UDO_File.close()

    else:
        print("Error -> File Path is empty!")


def main():
    doParsing(debug = False, showDotFile = True, UDO_FilePath = "udo_file_1.txt")

if __name__ == "__main__":
    main()
