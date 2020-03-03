#--------------------------------------------
""" INCLUDED MODULES: """
#--------------------------------------------
import math

#--------------------------------------------
""" CLASSES: """
#--------------------------------------------

class MathematicalFunctions:
    def __init__(self):
        self.functionsNames = {
            "nothing" : "do_nothing",
            "sin" : "do_sin",
            "cos" : "do_cos",
            "tan" : "do_tan",
            "asin" : "do_sin",
            "acos" : "do_acos",
            "atan" : "do_atan",
            "atan2" : "do_atan2",
            "log" : "do_log",
            "logd" : "do_logd",
            "exp" : "do_exp",
            "sqrt" : "do_sqrt",
            "abs" : "do_abs",
            "sgn" : "do_sgn",
            "int" : "do_int",
            "frac" : "do_frac",
            "rand" : "do_rand",
            "srand" : "do_srand"
            }

    def callFunction(self, stringWith_UDO_FunctionName = "nothing", **kwargs):
        return getattr(self, self.functionsNames[stringWith_UDO_FunctionName])(**kwargs)

    def do_nothing(self, **kwargs):
        pass

    def do_sin(self, **kwargs):
        return math.sin(kwargs["child"])

    def do_cos(self, **kwargs):
        return math.cos(kwargs["child"])

    def do_tan(self, **kwargs):
        return math.tan(kwargs["child"])

    def do_asin(self, **kwargs):
        return math.asin(kwargs["child"])

    def do_acos(self, **kwargs):
        return math.acos(kwargs["child"])

    def do_atan(self, **kwargs):
        return math.atan(kwargs["child"])

    def do_atan2(self, **kwargs):
        return math.atan2(kwargs["child"])

    def do_log(self, **kwargs):
        return math.log(kwargs["child"])

    def do_logd(self, **kwargs):
        return math.log10(kwargs["child"]) #Co robi funkcja logd() w UDO ????

    def do_exp(self, **kwargs):
        return math.exp(kwargs["child"])

    def do_sqrt(self, **kwargs):
        return math.sqrt(kwargs["child"])

    def do_abs(self, **kwargs):
        return math.fabs(kwargs["child"])

    def do_sgn(self, **kwargs):
        pass

    def do_int(self, **kwargs):
        pass

    def do_frac(self, **kwargs):
        pass

    def do_rand(self, **kwargs):
        pass

    def do_srand(self, **kwargs):
        pass

class LogicalOperators:
    def __init__(self):
        self.functionsNames = {
            "nothing" : "do_nothing",
            "&&" : "do_logicalAnd",
            "||" : "do_logicalOr",
            "==" : "do_equalTo",
            "!=" : "do_differentThan",
            "<" : "do_lessThan",
            ">" : "do_greaterThan",
            "<=" : "do_lessOrEqualTo",
            "=<" : "do_lessOrEqualTo",
            ">=" : "do_greaterOrEqualTo",
            "=>" : "do_greaterOrEqualTo"
            }

    def callFunction(self, stringWithLogicalOperator = "nothing", **kwargs):
        return getattr(self, self.functionsNames[stringWithLogicalOperator])(**kwargs)

    def do_nothing(self, **kwargs):
        pass

    def do_logicalAnd(self, **kwargs):
        return kwargs["value1"] and kwargs["value2"]

    def do_logicalOr(self, **kwargs):
        return kwargs["value1"] or kwargs["value2"]

    def do_equalTo(self, **kwargs):
        return kwargs["value1"] == kwargs["value2"]

    def do_differentThan(self, **kwargs):
        return kwargs["value1"] != kwargs["value2"]

    def do_lessThan(self, **kwargs):
        return kwargs["value1"] < kwargs["value2"]

    def do_greaterThan(self, **kwargs):
        return kwargs["value1"] > kwargs["value2"]

    def do_lessOrEqualTo(self, **kwargs):
        return kwargs["value1"] <= kwargs["value2"]

    def do_greaterOrEqualTo(self, **kwargs):
        return kwargs["value1"] >= kwargs["value2"]



