#--------------------------------------------
""" INCLUDED MODULES: """
#--------------------------------------------
from arpeggio import *
from arpeggio import RegExMatch as apperggioRegEx


#--------------------------------------------
""" GRAMMAR FUNCTIONS: """
#--------------------------------------------
def number():
    return apperggioRegEx(r'\d+\.\d+|\d+') 
# Sprawdzic czy wedlug UDO .2 to tez liczba
# Aktualnie dziala tylko dla liczb normalnych typu 0.2 itd.

def sign():
    return Optional(["+","-"]),[number,("(", expression, ")")]

def power(): # Zle Dziala !!!!!!!!!!!!!!!!!!!!!
    return sign, ZeroOrMore(["^"], sign)

def multiplicationAndDivision():
    return sign, ZeroOrMore(["*","/"], sign)

def expression():
    return [multiplicationAndDivision, power], ZeroOrMore(["+","-"], [multiplicationAndDivision, power])

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
    
    def visit_sign(self, node, children):
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
        Return the power of number
        """
        if self.debug:
            print("PowerOfNumber {}.".format(children))
        power = children[0]
        for i in range(2, len(children), 2):
            power **= children[i]
        if self.debug:
            print("PowerOfNumber {}.".format(power))
        return power

    def visit_multiplicationAndDivision(self, node, children):
        """
        Divides or Multiplies number
        """
        if self.debug:
            print("DivisonOrMultiplication {}.".format(children))
        divisonOrMultiplication = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "*":
                divisonOrMultiplication *= children[i]
            else:
                divisonOrMultiplication /= children[i]
        if self.debug:
            print("DivisonOrMultiplication = {}.".format(divisonOrMultiplication))
        return divisonOrMultiplication

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
            else:
                expression += children[i]
        if self.debug:
            print("Expression = {}.".format(expression))
        return expression


def main(debug=False):
    print("UDO Interpreter")

    parser = ParserPython(calc, debug=debug)
    
    # Wczytaj plik txt z wyrazeniem
    #inputExpr = "-(4-1)^5+(2+4.67)*5^2+5.89/(0.2+7)"
    #inputExprValue = -(4-1)**5+(2+4.67)*5**2+5.89/(0.2+7)

    inputExpr = "-(4-1)*5+(2+4.67)+5.89/(0.2+7)"
    inputExprValue = -(4-1)*5+(2+4.67)+5.89/(0.2+7)

    parse_tree = parser.parse(inputExpr)
    result = visit_parse_tree(parse_tree,GrammarRulesVisitor(debug=debug))

    print("{} = {}".format(inputExprValue,result))

    # Dodac renderowanie wykreu


if __name__ == "__main__":
    main(debug=True)
    #main(debug=False)
