class DebuggerDisplayAttribute(Attribute, _Attribute):
    """
    Determines how a class or field is displayed in the debugger variable windows.
    
    DebuggerDisplayAttribute(value: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: str) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name to display in the debugger variable windows.

Get: Name(self: DebuggerDisplayAttribute) -> str

Set: Name(self: DebuggerDisplayAttribute) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the attribute's target.

Get: Target(self: DebuggerDisplayAttribute) -> Type

Set: Target(self: DebuggerDisplayAttribute) = value
"""

    TargetTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type name of the attribute's target.

Get: TargetTypeName(self: DebuggerDisplayAttribute) -> str

Set: TargetTypeName(self: DebuggerDisplayAttribute) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string to display in the type column of the debugger variable windows.

Get: Type(self: DebuggerDisplayAttribute) -> str

Set: Type(self: DebuggerDisplayAttribute) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the string to display in the value column of the debugger variable windows.

Get: Value(self: DebuggerDisplayAttribute) -> str

"""


