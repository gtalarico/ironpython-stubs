class IWin32Window:
    """ Provides an interface to expose Win32 HWND handles. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the handle to the window represented by the implementer.

Get: Handle(self: IWin32Window) -> IntPtr

"""


