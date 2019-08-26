# encoding: utf-8
# module Wms.RemotingObjects.DataFlow calls itself DataFlow
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DataFlowObject:
    """
    DataFlowObject[T]()
    DataFlowObject[T](subject: T)
    """
    def AddError(self, error, details=None):
        """
        AddError(self: DataFlowObject[T], error: Error) -> DataFlowObject[T]
        AddError(self: DataFlowObject[T], error: str) -> DataFlowObject[T]
        AddError(self: DataFlowObject[T], error: str, details: str) -> DataFlowObject[T]
        """
        pass

    def AddQuestion(self, *__args):
        """
        AddQuestion(self: DataFlowObject[T], question: Question) -> DataFlowObject[T]
        AddQuestion(self: DataFlowObject[T], key: str, question: str) -> DataFlowObject[T]
        AddQuestion(self: DataFlowObject[T], key: str, question: str, details: str) -> DataFlowObject[T]
        AddQuestion(self: DataFlowObject[T], key: str, question: str, possibleAnswers: AnswerOptionsEnum) -> DataFlowObject[T]
        AddQuestion(self: DataFlowObject[T], key: str, question: str, details: str, possibleAnswers: AnswerOptionsEnum) -> DataFlowObject[T]
        """
        pass

    def AddWarning(self, *__args):
        """
        AddWarning(self: DataFlowObject[T], key: str, text: str, allowRetry: bool) -> DataFlowObject[T]
        AddWarning(self: DataFlowObject[T], warning: Warning) -> DataFlowObject[T]
        """
        pass

    def IsValid(self):
        """ IsValid(self: DataFlowObject[T]) -> bool """
        pass

    def IsVirgin(self):
        """ IsVirgin(self: DataFlowObject[T]) -> bool """
        pass

    def SetFailureResult(self):
        """ SetFailureResult(self: DataFlowObject[T]) -> DataFlowObject[T] """
        pass

    def SetResult(self, result):
        """ SetResult(self: DataFlowObject[T], result: DataFlowResultEnum) -> DataFlowObject[T] """
        pass

    def SetSuccessResult(self):
        """ SetSuccessResult(self: DataFlowObject[T]) -> DataFlowObject[T] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, subject=None):
        """
        __new__(cls: type)
        __new__(cls: type, subject: T)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Errors(self: DataFlowObject[T]) -> Errors

Set: Errors(self: DataFlowObject[T]) = value
"""

    Questions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Questions(self: DataFlowObject[T]) -> Questions

Set: Questions(self: DataFlowObject[T]) = value
"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Result(self: DataFlowObject[T]) -> DataFlowResultEnum

Set: Result(self: DataFlowObject[T]) = value
"""

    Subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Subject(self: DataFlowObject[T]) -> T

Set: Subject(self: DataFlowObject[T]) = value
"""

    Warnings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Warnings(self: DataFlowObject[T]) -> Warnings

Set: Warnings(self: DataFlowObject[T]) = value
"""


    Instance = DataFlowObject()
    """hardcoded/returns an instance of the class"""

class DataFlowResultEnum:
    """
    Result types of Wms.RemotingObjects.DataFlow object.
    
    enum DataFlowResultEnum, values: Failure (0), Success (1), SuccessWithWarning (3), Unspecified (256), UserInputRequired (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Failure = None
    Success = None
    SuccessWithWarning = None
    Unspecified = None
    UserInputRequired = None
    value__ = None

    Instance = DataFlowResultEnum()
    """hardcoded/returns an instance of the class"""

class IDataFlowObject:
    # no doc
    def IsValid(self):
        """ IsValid(self: IDataFlowObject[T]) -> bool """
        pass

    def IsVirgin(self):
        """ IsVirgin(self: IDataFlowObject[T]) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Errors(self: IDataFlowObject[T]) -> Errors

Set: Errors(self: IDataFlowObject[T]) = value
"""

    Questions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Questions(self: IDataFlowObject[T]) -> Questions

Set: Questions(self: IDataFlowObject[T]) = value
"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: IDataFlowObject[T]) -> DataFlowResultEnum

Set: Result(self: IDataFlowObject[T]) = value
"""

    Subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Subject(self: IDataFlowObject[T]) -> T

Set: Subject(self: IDataFlowObject[T]) = value
"""

    Warnings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Warnings(self: IDataFlowObject[T]) -> Warnings

Set: Warnings(self: IDataFlowObject[T]) = value
"""


    Instance = IDataFlowObject()
    """hardcoded/returns an instance of the class"""

