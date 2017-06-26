class DebuggerTypeProxyAttribute(Attribute, _Attribute):
    """
    Specifies the display proxy for a type.
    
    DebuggerTypeProxyAttribute(type: Type)
    DebuggerTypeProxyAttribute(typeName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, typeName: str)
        """
        pass

    ProxyTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type name of the proxy type.

Get: ProxyTypeName(self: DebuggerTypeProxyAttribute) -> str

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target type for the attribute.

Get: Target(self: DebuggerTypeProxyAttribute) -> Type

Set: Target(self: DebuggerTypeProxyAttribute) = value
"""

    TargetTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the target type.

Get: TargetTypeName(self: DebuggerTypeProxyAttribute) -> str

Set: TargetTypeName(self: DebuggerTypeProxyAttribute) = value
"""


