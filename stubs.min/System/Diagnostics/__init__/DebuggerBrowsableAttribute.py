class DebuggerBrowsableAttribute(Attribute, _Attribute):
    """
    Determines if and how a member is displayed in the debugger variable windows. This class cannot be inherited.
    
    DebuggerBrowsableAttribute(state: DebuggerBrowsableState)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, state):
        """ __new__(cls: type, state: DebuggerBrowsableState) """
        pass

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display state for the attribute.

Get: State(self: DebuggerBrowsableAttribute) -> DebuggerBrowsableState

"""


