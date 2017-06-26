class IViewSheetSet:
    """ This interface represents a selected set of views/sheets which will be used for printing. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The views.

Get: Views(self: IViewSheetSet) -> ViewSet

Set: Views(self: IViewSheetSet) = value
"""


