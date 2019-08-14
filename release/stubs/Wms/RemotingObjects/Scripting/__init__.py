from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.Scripting calls itself Scripting
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GetScriptArgs():
    """ GetScriptArgs() """
    Instance = GetScriptArgs
    """hardcoded/returns an instance of the class"""
    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Active(self: GetScriptArgs) -> Nullable[bool]

Set: Active(self: GetScriptArgs) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Filter(self: GetScriptArgs) -> str

Set: Filter(self: GetScriptArgs) = value
"""

    Hook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Hook(self: GetScriptArgs) -> str

Set: Hook(self: GetScriptArgs) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: GetScriptArgs) -> int

Set: Id(self: GetScriptArgs) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: GetScriptArgs) -> str

Set: Name(self: GetScriptArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ZoneId(self: GetScriptArgs) -> int

Set: ZoneId(self: GetScriptArgs) = value
"""



class PythonError():
    """
    PythonError(message: str, span: SourceSpan, errorCode: int, severity: ErrorSeverity)
    PythonError()
    """
    Instance = PythonError
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, message=None, span=None, errorCode=None, severity=None):
        """
        __new__(cls: type, message: str, span: SourceSpan, errorCode: int, severity: ErrorSeverity)
        __new__(cls: type)
        """
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ErrorCode(self: PythonError) -> int

Set: ErrorCode(self: PythonError) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Message(self: PythonError) -> str

Set: Message(self: PythonError) = value
"""

    Severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Severity(self: PythonError) -> ErrorSeverity

Set: Severity(self: PythonError) = value
"""

    Span = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Span(self: PythonError) -> SourceSpan

Set: Span(self: PythonError) = value
"""


    ErrorSeverity = None


class ScriptSnippet():
    """ ScriptSnippet() """
    Instance = ScriptSnippet
    """hardcoded/returns an instance of the class"""
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: ScriptSnippet) -> str

Set: Description(self: ScriptSnippet) = value
"""

    Script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Script(self: ScriptSnippet) -> str

Set: Script(self: ScriptSnippet) = value
"""



class SourceLocation():
    """
    SourceLocation()
    SourceLocation(index: int, line: int, column: int)
    """
    Instance = SourceLocation
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def Compare(left, right):
        """ Compare(left: SourceLocation, right: SourceLocation) -> int """
        pass

    def Equals(self, obj):
        """ Equals(self: SourceLocation, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: SourceLocation) -> int """
        pass

    def ToString(self):
        """ ToString(self: SourceLocation) -> str """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, index=None, line=None, column=None):
        """
        __new__(cls: type)
        __new__(cls: type, index: int, line: int, column: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Column(self: SourceLocation) -> int

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Index(self: SourceLocation) -> int

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsValid(self: SourceLocation) -> bool

"""

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Line(self: SourceLocation) -> int

"""


    Invalid = None
    MinValue = None
    None_ =None


class SourceSpan():
    """
    SourceSpan()
    SourceSpan(start: SourceLocation, end: SourceLocation)
    """
    Instance = SourceSpan
    """hardcoded/returns an instance of the class"""
    def Equals(self, obj):
        """ Equals(self: SourceSpan, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: SourceSpan) -> int """
        pass

    def ToString(self):
        """ ToString(self: SourceSpan) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, start=None, end=None):
        """
        __new__(cls: type)
        __new__(cls: type, start: SourceLocation, end: SourceLocation)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: End(self: SourceSpan) -> SourceLocation

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsValid(self: SourceSpan) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Length(self: SourceSpan) -> int

"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Start(self: SourceSpan) -> SourceLocation

"""


    Invalid = None
    None_ =None


class ZoneScript(DbObject):
    """ ZoneScript() """
    Instance = ZoneScript
    """hardcoded/returns an instance of the class"""
    def Clone(self):
        """ Clone(self: ZoneScript) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Active(self: ZoneScript) -> bool

Set: Active(self: ZoneScript) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: ZoneScript) -> str

Set: Description(self: ZoneScript) = value
"""

    HasScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasScript(self: ZoneScript) -> bool

"""

    Hook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Hook(self: ZoneScript) -> str

Set: Hook(self: ZoneScript) = value
"""

    HookSourceVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HookSourceVersion(self: ZoneScript) -> int

Set: HookSourceVersion(self: ZoneScript) = value
"""

    HookVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HookVersion(self: ZoneScript) -> int

Set: HookVersion(self: ZoneScript) = value
"""

    HookVersionDifference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HookVersionDifference(self: ZoneScript) -> bool

Set: HookVersionDifference(self: ZoneScript) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: ZoneScript) -> int

Set: Id(self: ZoneScript) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: ZoneScript) -> str

Set: Name(self: ZoneScript) = value
"""

    ScriptToExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ScriptToExecute(self: ZoneScript) -> str

Set: ScriptToExecute(self: ZoneScript) = value
"""

    TreeOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TreeOrder(self: ZoneScript) -> int

Set: TreeOrder(self: ZoneScript) = value
"""

    TreePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TreePath(self: ZoneScript) -> str

Set: TreePath(self: ZoneScript) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ZoneId(self: ZoneScript) -> int

Set: ZoneId(self: ZoneScript) = value
"""



class ZoneScripts(FindableList):
    """ ZoneScripts() """
    Instance = ZoneScripts
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[ZoneScript]) -> ZoneScripts """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'Name'
    ValueMember = 'Id'


# variables with complex values

