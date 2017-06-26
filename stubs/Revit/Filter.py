# encoding: utf-8
# module Revit.Filter calls itself Filter
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FilterRule(object):
    """ Revit Filter Rule """
    @staticmethod
    def ByRuleType(type, value, parameter):
        """
        ByRuleType(type: str, value: object, parameter: Parameter) -> FilterRule
        
            Create a new Filter Rule
        
            type: Filter Rule Type
            value: Value to check
            parameter: Parameter to filter
        """
        pass

    RuleType = None


class OverrideGraphicSettings(object):
    """ Override Graphic Settings """
    @staticmethod
    def ByProperties(cutFillColor, projectionFillColor, cutLineColor, projectionLineColor, cutFillPattern, projectionFillPattern, cutLinePattern, projectionLinePattern, cutLineWeight, projectionLineWeight):
        """
        ByProperties(cutFillColor: Color, projectionFillColor: Color, cutLineColor: Color, projectionLineColor: Color, cutFillPattern: FillPatternElement, projectionFillPattern: FillPatternElement, cutLinePattern: LinePatternElement, projectionLinePattern: LinePatternElement, cutLineWeight: int, projectionLineWeight: int) -> OverrideGraphicSettings
        
            Create a OverrideGraphicSettings element
        
            cutFillColor: Fill color
            projectionFillColor: Projection color
            cutLineColor: Cut line color
            projectionLineColor: Projection line color
            cutFillPattern: Cut fill pattern
            projectionFillPattern: Projection fill pattern
            cutLinePattern: Cut line pattern
            projectionLinePattern: Projection line pattern
            cutLineWeight: Cut line weight
            projectionLineWeight: Projection line weight
            Returns: OverrideGraphicSettings
        """
        pass


class ParameterFilterElement(Element, IDisposable, IGraphicItem, IFormattable):
    """ Parameter Filter Element """
    @staticmethod
    def ByRules(name, categories, rules):
        """ ByRules(name: str, categories: IEnumerable[Category], rules: IEnumerable[FilterRule]) -> ParameterFilterElement """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: ParameterFilterElement) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


