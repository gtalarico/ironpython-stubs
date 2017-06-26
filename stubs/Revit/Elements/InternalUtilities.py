# encoding: utf-8
# module Revit.Elements.InternalUtilities calls itself InternalUtilities
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ElementQueries(object):
    # no doc
    @staticmethod
    def AtLevel(arg):
        """ AtLevel(arg: Level) -> IList[Element] """
        pass

    @staticmethod
    def OfCategory(category):
        """ OfCategory(category: Category) -> IList[Element] """
        pass

    @staticmethod
    def OfElementType(elementType):
        """ OfElementType(elementType: Type) -> IList[Element] """
        pass

    @staticmethod
    def OfFamilyType(familyType):
        """ OfFamilyType(familyType: FamilyType) -> IList[Element] """
        pass

    __all__ = [
        'AtLevel',
        'OfCategory',
        'OfElementType',
        'OfFamilyType',
    ]


class ElementUtils(object):
    """ ElementUtils() """
    @staticmethod
    def GetConvertedParameterValue(param, value):
        """ GetConvertedParameterValue(param: Parameter, value: float) -> float """
        pass

    @staticmethod
    def GetParameterValue(param):
        """
        GetParameterValue(param: Parameter) -> object
        
            Get a revit parameters value
        
            param: Revit parameter
        """
        pass

    @staticmethod
    def SetParameterValue(param, value):
        """ SetParameterValue(param: Parameter, value: str)SetParameterValue(param: Parameter, value: bool)SetParameterValue(param: Parameter, value: int)SetParameterValue(param: Parameter, value: float)SetParameterValue(param: Parameter, value: Element) """
        pass

    @staticmethod
    def UpdateLevelName(name):
        """
        UpdateLevelName(name: str) -> str
        
            This function checks if the name ends with "(num)". Here num is a integer.
            
                     If yes, it will replace "(num)" with "(num+1)". Here num+1 is the form 
             of the
                    evaluated integer. Otherwise, it will append "(1)" at the 
             end of the name.
                    For example:
                    This function will 
             change the name from "abc(2)" to "abc(3)",
                    from "abc" to "abc(1)".
        """
        pass


class TransformUtils(object):
    """ TransformUtils() """
    @staticmethod
    def ExtractEularAnglesFromTransform(transform, angles):
        """ ExtractEularAnglesFromTransform(transform: Transform) -> Array[float] """
        pass


