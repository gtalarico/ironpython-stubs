# encoding: utf-8
# module System.Linq.Dynamic calls itself Dynamic
# from Wms.RemotingImplementation, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DynamicClass:
    # no doc
    def ToString(self):
        """ ToString(self: DynamicClass) -> str """
        pass


class DynamicExpression:
    # no doc
    @staticmethod
    def CreateClass(properties):
        """
        CreateClass(*properties: Array[DynamicProperty]) -> Type
        CreateClass(properties: IEnumerable[DynamicProperty]) -> Type
        """
        pass

    @staticmethod
    def Parse(resultType, expression, values):
        """ Parse(resultType: Type, expression: str, *values: Array[object]) -> Expression """
        pass

    @staticmethod
    def ParseLambda(*__args):
        """
        ParseLambda(itType: Type, resultType: Type, expression: str, *values: Array[object]) -> LambdaExpression
        ParseLambda(parameters: Array[ParameterExpression], resultType: Type, expression: str, *values: Array[object]) -> LambdaExpression
        ParseLambda[(T, S)](expression: str, *values: Array[object]) -> Expression[Func[T, S]]
        """
        pass

    __all__ = [
        'CreateClass',
        'Parse',
        'ParseLambda',
    ]


class DynamicProperty:
    """ DynamicProperty(name: str, type: Type) """
    @staticmethod # known case of __new__
    def __new__(self, name, type):
        """ __new__(cls: type, name: str, type: Type) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DynamicProperty) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: DynamicProperty) -> Type

"""



class DynamicQueryable:
    # no doc
    @staticmethod
    def Any(source):
        """ Any(source: IQueryable) -> bool """
        pass

    @staticmethod
    def Count(source):
        """ Count(source: IQueryable) -> int """
        pass

    @staticmethod
    def GroupBy(source, keySelector, elementSelector, values):
        """ GroupBy(source: IQueryable, keySelector: str, elementSelector: str, *values: Array[object]) -> IQueryable """
        pass

    @staticmethod
    def OrderBy(source, ordering, values):
        """
        OrderBy[T](source: IQueryable[T], ordering: str, *values: Array[object]) -> IQueryable[T]
        OrderBy(source: IQueryable, ordering: str, *values: Array[object]) -> IQueryable
        """
        pass

    @staticmethod
    def Select(source, selector, values):
        """ Select(source: IQueryable, selector: str, *values: Array[object]) -> IQueryable """
        pass

    @staticmethod
    def Skip(source, count):
        """ Skip(source: IQueryable, count: int) -> IQueryable """
        pass

    @staticmethod
    def Take(source, count):
        """ Take(source: IQueryable, count: int) -> IQueryable """
        pass

    @staticmethod
    def Where(source, predicate, values):
        """
        Where[T](source: IQueryable[T], predicate: str, *values: Array[object]) -> IQueryable[T]
        Where(source: IQueryable, predicate: str, *values: Array[object]) -> IQueryable
        """
        pass

    __all__ = [
        'Any',
        'Count',
        'GroupBy',
        'OrderBy',
        'Select',
        'Skip',
        'Take',
        'Where',
    ]


class ParseException:
    """ ParseException(message: str, position: int) """
    def ToString(self):
        """ ToString(self: ParseException) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message, position):
        """ __new__(cls: type, message: str, position: int) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ParseException) -> int

"""


    SerializeObjectState = None


