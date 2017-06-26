class IFrameworkInputElement(IInputElement):
    """ Declares a namescope contract for framework elements. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of an element.

Get: Name(self: IFrameworkInputElement) -> str

Set: Name(self: IFrameworkInputElement) = value
"""


