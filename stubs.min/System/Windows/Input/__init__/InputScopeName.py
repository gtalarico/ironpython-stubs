class InputScopeName(object, IAddChild):
    """
    Defines a name for text input patterns.
    
    InputScopeName()
    InputScopeName(nameValue: InputScopeNameValue)
    """
    def AddChild(self, value):
        """
        AddChild(self: InputScopeName, value: object)
            Adds a child object to this System.Windows.Input.InputScopeName.
        
            value: The object to be added as the child of this System.Windows.Input.InputScopeName.
        """
        pass

    def AddText(self, name):
        """
        AddText(self: InputScopeName, name: str)
            Adds a text string as a child of this System.Windows.Input.InputScopeName.
        
            name: The text added to the System.Windows.Input.InputScopeName.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nameValue=None):
        """
        __new__(cls: type)
        __new__(cls: type, nameValue: InputScopeNameValue)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    NameValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the input scope name value which modifies how input from alternative input methods is interpreted.

Get: NameValue(self: InputScopeName) -> InputScopeNameValue

Set: NameValue(self: InputScopeName) = value
"""


