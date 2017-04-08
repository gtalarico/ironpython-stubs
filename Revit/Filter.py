# encoding: utf-8
# module Revit.Filter calls itself Filter
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FilterRule(object):
    # no doc
    @staticmethod
    def ByRuleType(type, value, parameter):
        """ ByRuleType(type: str, value: object, parameter: Parameter) -> FilterRule """
        pass

    RuleType = None


class OverrideGraphicSettings(object):
    # no doc
    @staticmethod
    def ByProperties(cutFillColor, projectionFillColor, cutLineColor, projectionLineColor, cutFillPattern, projectionFillPattern, cutLinePattern, projectionLinePattern, cutLineWeight, projectionLineWeight):
        """ ByProperties(cutFillColor: Color, projectionFillColor: Color, cutLineColor: Color, projectionLineColor: Color, cutFillPattern: FillPatternElement, projectionFillPattern: FillPatternElement, cutLinePattern: LinePatternElement, projectionLinePattern: LinePatternElement, cutLineWeight: int, projectionLineWeight: int) -> OverrideGraphicSettings """
        pass


class ParameterFilterElement(Element):
    # no doc
    @staticmethod
    def ByRules(name, categories, rules):
        """ ByRules(name: str, categories: IEnumerable[Category], rules: IEnumerable[FilterRule]) -> ParameterFilterElement """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: ParameterFilterElement) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


